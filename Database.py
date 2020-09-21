#Tutor assistant database file, by Cyani
#This is the main program. All other programs written are run from here
#Thank you to Python Central for teaching me how to use basic database operations in python using sqlite3
#Credit is also given in each file where due

#Throught the program, procedures beggining with "a" are admin, "t" are teacher, and "s" are students
#For example, where you see accesslevel =='a', it means if the current user is an admin

#If you are struggling to understand the database sections, I reccomend to read through Python Central's sqlite3 tutorial
#Basically, db is the current accessed database, commit means save changes, and close is used to close the connection.
#From there, it is basically SQL

#import pdb; pdb.set_trace()

try:
    import sqlite3
    import time
    import datetime
except:
    print("Please ensure you have the sqlite3, time, and datetime modules installed")


#This is used to see if all the nessasary databases are present in the folder
#If they are, an error will be raised, hence the except
#If they are not, they are created
def tableCheck():
    try:
        db = sqlite3.connect('sdb.db')
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT, 
                              class TEXT, email TEXT unique, Homework TEXT, content TEXT)
        ''')
        db.commit()
        db.close()
        print("student database not found\nstudent database created")
        
    except:
        db.close()
        print("student database found")

    try:
        db = sqlite3.connect('tdb.db')
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE teachers(id INTEGER PRIMARY KEY, name TEXT, 
                              class TEXT, email TEXT unique)
        ''')
        db.commit()
        db.close()
        print("teacher database not found\nteacher database created")
        
    except:
        db.close()
        print("teacher database found")
    
    try:
        db = sqlite3.connect('adb.db')
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE admins(id INTEGER PRIMARY KEY, name TEXT, 
                      class TEXT, email TEXT unique)
        ''')
        db.commit()

        
        #An admin is created so the program can be used right away
        cursor.execute('''INSERT INTO admins(name)
                VALUES(?)''', ("admin",)
               )
        db.commit()
        db.close()
        print("admin database not found\nadmin database created")
        
    except:
        db.close()
        print("admin database found")

    try:
        db = sqlite3.connect('ddb.db')
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE detention(id INTEGER PRIMARY KEY, name TEXT, 
                      class TEXT, reason TEXT)
        ''')
        db.commit()
        db.close()
        print("detention database not found\ndetention database created\n")
    except:
        db.close()
        print("detention database found\n") 



#Checks which students are in detention
def checkDetention():
    if accesslevel == "a":
        db = sqlite3.connect('ddb.db')
        cursor = db.cursor()
        cursor.execute('''SELECT name,reason FROM detention''')

    #Teachers are only allowed to see students in their class who are in detention    
    elif accesslevel == "t":
        db = sqlite3.connect('tdb.db')
        cursor = db.cursor()
        cursor.execute('''SELECT class FROM teachers WHERE name=?''', (users_name,))
        obtained = cursor.fetchone()

        if obtained == None:
            print("You are not assigned to a class, so you cannot view your pupils in detention")
        else:
            obtained = obtained[0]
            db.close()
            db = sqlite3.connect('ddb.db')
            cursor = db.cursor()
            cursor.execute('''SELECT name,reason FROM detention WHERE class =? ''', (obtained,))

            
    names = cursor.fetchall()
    #It is possible to get None or [] if the detention is emtpy depending on what access level is calling the procedure
    if names in [None,[]]:
        print("No one is in detention")
    else:
        for x in names:
            print(x[0] + "is in detention for " + x[1])
    db.close()
        


#Add a student to detention
def addToDetention():
        #Which student gets put into detention
        name = input("What is the name of the student you would like to put into detention?\n")
        reason = input("What is the reason you have added the pupil to the detention list?\n:")
        if accesslevel == "t":
            #Get the teacher's class
            db = sqlite3.connect('tdb.db')
            cursor = db.cursor()
            cursor.execute('''SELECT class FROM teachers WHERE name=?''', (users_name,))
            classname = cursor.fetchone()
            if classname == None:
                print("You are not assigned to a class, so cannot give any students detention (can only give detention to your own studetns) ")
            else:
                #Find the students
                classname = classname[0]
                db.close()
                db = sqlite3.connect('sdb.db')
                cursor = db.cursor()
                #Check student is in the class
                cursor.execute('''SELECT name FROM students WHERE class=?, name=?''', (classname,name,))
                name = cursor.fetchone()
                if name == None:
                    print("This student is not in your class, so you cannot give them detention")
                else:
                    name = name[0]
                    db.close()
                    db = sqlite3.connect('ddb.db')
                    cursor = db.cursor()
                    cursor.execute('''INSERT INTO detention(name, class, reason)
                                   VALUES(?,?,?)''', (name, classname, reason))
                    db.commit()
                    db.close()
                    print(name + " have been added to the detention list")
            
        elif accesslevel == "a":
            #Get the class of the student
            db = sqlite3.connect('sdb.db')
            cursor = db.cursor()
            cursor.execute('''SELECT class FROM students WHERE name=?''', (name,))
            classname = cursor.fetchone()
            db.close()

            #If the student isnt found, say so
            if classname == None:
                print("This student was not found")
            else:
                #Add the student to the detention list
                classname = classname[0]
                db = sqlite3.connect('ddb.db')
                cursor = db.cursor()
                cursor.execute('''INSERT INTO detention(name, class, reason)
                  VALUES(?,?,?)''', (name, classname, reason))
                db.commit()
                db.close()
                print(name + " has been added to the detention list")
            


#Remove a student from detention
def removeFromDetention():
    db = sqlite3.connect('ddb.db')
    cursor = db.cursor()
    #Who is getting out of detention
    del_name = input("Enter the full name of the student you would like to delete\n:")
    cursor.execute('''SELECT name FROM detention WHERE name=?''', (del_name,))
    del_name = cursor.fetchone()
    #If they are not on the detetnion list, say so
    if del_name == None:
        print("This student is not in detention")
    else:
        #Remove the specified student from the detention list
        del_name = del_name[0]
        cursor.execute('''DELETE FROM detention WHERE name = ? ''', (del_name,))
        db.commit()
        db.close()
        print(del_name, " has been removed from the detention database")
    


#Change the Homework status. This is also used to create Homework        
def updateHomework():
    year = int(input("What year is the Homework due? (for 2019, type \"2019\")\n:"))
    month = int(input("What month is the Homework due? (for January, type \"1\")\n:"))
    day = int(input("What day of the month is the Homework due? (for the 15th, type \"15\")\n:"))
    date = datetime.date(year, month, day)
    Homework = input("What is the Homework that you have assigned?\n")

    if accesslevel == "t":
        #Find the teacher's class
        db = sqlite3.connect('tdb.db')
        cursor = db.cursor()
        cursor.execute('''SELECT class FROM teachers WHERE name=?''', (users_name,))
        classfind = cursor.fetchone()[0]
        db.close()
        
        #Set the Homework to all students currently in the teachers class
        db = sqlite3.connect('sdb.db')
        cursor = db.cursor()
        cursor.execute('''UPDATE students SET Homework = ?, content = ? WHERE class = ? ''',
     (date, Homework, classfind))
        db.commit()
        db.close()
        
        print("Homework has been updated for", date, "and it is to do", Homework)
        
    if accesslevel == "a":
        #Assign the Homework to all students currently in the inputted class
        classHomework = input("What class is this for?\n:")
        db = sqlite3.connect('sdb.db')
        cursor = db.cursor()
        cursor.execute('''UPDATE students SET Homework = ?, content = ? WHERE class = ? ''',
     (date, Homework, classHomework))
        db.commit()
        db.close()
        
        print("Homework has been updated for", date, "and it is to do", Homework)
        

#This is the homework checking procedure    
def checkHomework():
    #If the user is a student, select their Homework
    if accesslevel == "s":
        db = sqlite3.connect('sdb.db')
        cursor = db.cursor()
        cursor.execute('''SELECT Homework FROM students WHERE name=?''', (users_name,))

    #If the user is a teacher, find out the teacher's class and check the Homework for that class
    elif accesslevel == "t":
        db = sqlite3.connect('tdb.db')
        cursor = db.cursor()
        cursor.execute('''SELECT class FROM teachers WHERE name=?''', (users_name,))
        obtained = cursor.fetchone()
        db.close()
        if obtained == None:
            print("You are not currently assigned to a class. You cannot assign Homework for a class that does not exist.")
        else:
            obtained = obtained[0]
            #get the assigned Homework for the class
            db = sqlite3.connect('sdb.db')
            cursor = db.cursor()
            cursor.execute('''SELECT Homework FROM students WHERE class=?''', (obtained,))
            
    elif accesslevel == "a":
        class_option = input("Which class would you like to check? (for class 1A, type \"1A\", case sensitive)\n:")
        db = sqlite3.connect('sdb.db')
        cursor = db.cursor()
        cursor.execute('''SELECT Homework FROM students WHERE class=?''', (class_option,))
        
    student = cursor.fetchone()

    db.close()
    if student == None:
        print("No Homework")
        if accesslevel != 's':
            print("This can occur if there are no students in your class or the class does not exist")

    else:
        #Calculate how many days until Homework is due
        classfind = student[0]
        year = int(classfind[0:4])
        month = int(classfind[5:7])
        day = int(classfind[8:])
        date = datetime.date(year,month, day)
        cyear = year - int(datetime.date.today().strftime("%Y"))
        days = int((365*cyear) + int(date.strftime("%j")))
        current = int(days) - int(datetime.date.today().strftime("%j"))
        #If Homework is due today, ask the student if they have done it
        if current <= 0:
            if current == 0:
                print("Homework is due today")
            else:
                print("Homework is overdue")
            if accesslevel == "s":
                Homework = input("Do you have your Homework to hand in? yes (y) or no (n)\n:").lower()
                if Homework == "y":
                    print("Please hand in your Homework to the teacher, they will delete the Homework status from your acoount")

                #If not, add them to the detention list    
                elif Homework == "n":
                    reason = "This student did not do their assigned Homework"
                    db = sqlite3.connect('sdb.db')
                    cursor = db.cursor()
                    cursor.execute('''SELECT class FROM students WHERE name=?''', (users_name,))
                    classname = cursor.fetchone()
                    classname = classname[0]
                    db.close()
                    db = sqlite3.connect('ddb.db')
                    cursor = db.cursor()
                    cursor.execute('''INSERT INTO detention(name, class, reason)
                      VALUES(?,?,?)''', (users_name, classname, reason))
                    db.commit()
                    db.close()
                    print("You have been added to the detention list")
                
        #If Homework is due in the future, say how many days until it is due 
        elif current > 0:
            print("Homework is due in ", current, " days")
            
        #Just to be sure!
        else:
            print("Error")
            
    
#Add a teacher to the database (admin only)
def addTeacher():
    #Get the teacher's infomation
    fname = input('Enter teacher\'s first name:\n')
    lname = input('Enter teacher\'s last name:\n')
    class_set = input('Enter teacher\'s set:\n')
    #Combine the teachers first and last name, and set up email
    name = fname + " " + lname
    email = name + class_set + "@school.com"
    #add to the teacher database
    db = sqlite3.connect('tdb.db')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO teachers(name, class, email)
                  VALUES(?,?,?)''', (name,class_set, email))
    db.commit()
    print(fname + " " + lname + " has been added to the teacher database")
    db.close()
    

#Find what student has what teacher
def findStudentsTeacher():
    student_name = input("What is the students name?\n:")
    #Find the student inputted
    db = sqlite3.connect('sdb.db')
    cursor = db.cursor()
    cursor.execute('''SELECT class FROM students WHERE name=?''', (student_name,))
    classfind = cursor.fetchone()
    db.close()
    #If the student doesn't have a teacher/not added, say so
    if classfind == None:
        print("This student does not have a teacher yet")
    else:
        #Otherwise, find the teacher in the students class
        classfind = classfind[0]
        db = sqlite3.connect('tdb.db')
        cursor = db.cursor()
        cursor.execute('''SELECT name FROM teachers WHERE class=?''', (classfind,))
        name = cursor.fetchone()
        if name == None:
            print("This student's class has not been assigned a teacher yet!")
        else:
            print(name[0], "is the teacher of", student_name)
        
                   

#Add student to the database (admin only)
def addStudent():
    #Get students infomation
    fname = input('Enter student\'s first name:\n')
    lname = input('Enter student\'s last name:\n')
    class_set = input('Enter student\'s set:\n')
    #Set up full name and email address
    name = fname + " " + lname
    email = name + class_set + "@school.com"
    #Add them to the student database
    db = sqlite3.connect('sdb.db')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO students(name, class, email)
                  VALUES(?,?,?)''', (name,class_set, email))
    db.commit()
    db.close()
    print(fname + " " + lname + " has been added to the student database")
    

#Delete a student from the database (admin only)
def deleteStudent():
    #enter student name to be deleted
    del_name = input("Enter the full name of the student you would like to delete\n:")
    #delete that student
    db = sqlite3.connect('sdb.db')
    cursor = db.cursor()
    cursor.execute('''DELETE FROM students WHERE name = ? ''', (del_name,))
    db.commit()
    db.close()
    db = sqlite3.connect('ddb.db')
    cursor = db.cursor()
    cursor.execute('''DELETE FROM detention WHERE name = ? ''', (del_name,))
    db.commit()
    db.close()
    print(del_name, "has been removed from the student database")

#Delete a teacher from the database (admin only)
def deleteTeacher():
    #enter teacher name to be deleted
    del_name = input("Enter the full name of the student you would like to delete\n:")
    #delete that teacher
    db = sqlite3.connect('tdb.db')
    cursor = db.cursor()
    cursor.execute('''DELETE FROM teachers WHERE name = ? ''', (del_name,))
    db.commit()
    db.close()
    print(del_name, "has been removed from the teacher database")


#delete a students Homework    
def deleteHomework():
    db = sqlite3.connect('sdb.db')
    cursor = db.cursor()
    if accesslevel == "t":
        #Set the Homework to empty string
        cursor.execute('''UPDATE students SET Homework = ? WHERE teachers = ? ''',
     ("", users_name))

    elif accesslevel == "a":
        del_name = input("Enter the class of the set Homework you would like to delete\n:")
        #Set the Homework to empty string
        cursor.execute('''UPDATE students SET Homework = ? WHERE class = ? ''',
     ("", del_name))
    db.commit()
    db.close()
    

#Find a student's infomation    
def find():
    #What student's info needs to be found
    student_name = input("What is the students full name?\n:")
    db = sqlite3.connect('sdb.db')
    cursor = db.cursor()
    #If a student wants another students info, make sure it is not sensitive (basically only show the students contact infomation provided by the school)
    if accesslevel == "s":
        cursor.execute('''SELECT email FROM students WHERE name=?''', (student_name,))
    else:
        cursor.execute('''SELECT id, email, Homework FROM students WHERE name=?''', (student_name,))    
    student = cursor.fetchone()
    if student == None:
        print("That student was not found")
    else:
        print(student)
    

#describes what keypress achieves what task
def helpMe():
    choices = {
        #Admins can:
        'a': {
        's':"add a student",
        't':"add a teacher",
        'd':"delete a student",
        'p':"delete a teacher",
        },

        #Admins and teachers can:
        't':{
        'l':"find a students teacher",
        'u':"update Homework",
        'e':"add to detention",
        'r':"remove from detention",
        'k':"check detention",
        'i':"delete Homework",
        },

        #All users can:
        's':{
        'f':"find a student's infomation",
        'c':"check Homework"
        }
        }
    #Create empty list and add options depending on access level
    options = []
    if accesslevel == 'a':
        options += list(choices['a'].items())
        options += list(choices['t'].items())
    if accesslevel == 't':
        options += list(choices['t'].items())
    options += list(choices['s'].items())

    #print all possible keypresses with their corrisponding action (obviously not unexpected keypresses)
    for x in options:
        print("Press " + x[0] + " to " + x[1])

#Where the user can choose what action they want to do
def menu():
    choice = input("What would you like to do?(press h for help)\n:").lower()
    #If the users chooses q, return false to stop the while loop
    if choice == 'q':
        return False
    #empty#
    #added single run
    #multi run
    choices = {
        #Admins can:
        'a': {
        's':addStudent,#
        't':addTeacher,#
        'd':deleteStudent,
        'p':deleteTeacher,
        },

        #Admins and teachers can:
        't':{
        'l':findStudentsTeacher,#Do with student, but without teacher
        'u':updateHomework,
        'e':addToDetention,
        'r':removeFromDetention,
        'k':checkDetention,
        'i':deleteHomework,
        },

        #All users can:
        's':{
        'f':find,
        'c':checkHomework,
        'h':helpMe
        }
        }

    #If an option is not in an accesslevel section, it will raise an error because it does not exist
    #Goes on to check all accesslevels that the user can access
    try:
        choices['s'][choice]()
    except:
        if accesslevel in ['t','a']:
            try:
                choices['t'][choice]()
            except:
                if accesslevel == 't':
                    print("Invalid Input")
                else:
                    try:
                        choices['a'][choice]()
                    except:
                        print("Invalid Input")
    #If the user dosent quit, keep the while loop going
    return True




def start():
    #The username and access level needs to be accessed througout the program
    global accesslevel
    global users_name
    try:
        import Motion
    except:
        print("The motion sensors failed. Please ensure you are using the raspberry pi, have the correct modules installed, and the components are properly connected to the correct pins")
        print("Launching login GUI")

    try:
        import login
    except:
        print("login gui failed. Please ensure you have the correct modules installed")

    try:
        import scanner
    except:
        print("QR code scanner failed. Please ensure you have a compatible camera plugged in and the correct modules installed")
        print("For security reasons, you cannot proceed")
        return False
    users_name = scanner.database_recieve



    #The following code checks if the person is in the database
    db = sqlite3.connect('sdb.db')
    cursor = db.cursor()
    cursor.execute('''SELECT id FROM students WHERE name=?''', (users_name,))
    result = cursor.fetchone()
    db.close()
    if result == None:
        db = sqlite3.connect('tdb.db')
        cursor = db.cursor()
        cursor.execute('''SELECT id FROM teachers WHERE name=?''', (users_name,))
        result = cursor.fetchone()
        db.close()
        if result == None:
            db = sqlite3.connect('adb.db')
            cursor = db.cursor()
            cursor.execute('''SELECT id FROM admins WHERE name=?''', (users_name,))
            result = cursor.fetchone()
            db.close()
            if result == None:
                print("\nYou are not in the database, so you cannot access this programme!")
                return False
            else:
                accesslevel = "a"
                print("Welcome", users_name + ". Your current status is administrator. If you believe this is an error, contact an administrator")
                return True
        else:
            accesslevel = "t"
            print("Welcome", users_name + ". Your current status is teacher. If you believe this is an error, contact an administrator")
            return True
    else:
        accesslevel = "s"
        print("\nWelcome", users_name + ". Your current status is student. If you believe this is an error, contact an administrator\n\n")
        checkHomework()
        return True































tableCheck()
stop = start()
while stop:
    stop = menu()
print("Goodbye!")
