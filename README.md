# Classroom-Assistant
First of all, I am aware that the following guide is not clear and poorly formatted. This will be fixed as soon as possible

Disclaimer:
This program was not made by a professional. 
There are many bad practices used in this program, alot of which I have fixed (trust me)
This is because this was originally designed and built while I was learning to program
This being said, any advice or constructive critism would be greatly appriciated :)
Use at your own risk

(I have written a paper about the development of this project, which is available upon request (does not include latest updates))



This program is used for teachers who have a class and do not want to undertake the repetitive tasks at the beggining of the class.

For full functionality, a rasperry pi is required. This program can still be run without it, although the Motion.py file will not work.

# Basic program run through:
1.Motion sensors detect movement (i.e someone entering the class)
2.login GUI launched
3.QR code scanner scans student/teacher/admin QR code
4.They are logged into the program to do their nessasary tasks


# All possible operations
Admin:
's':addStudent	
't':addTeacher	
'd':deleteStudent 
'p':deleteTeacher

Teacher:
'l':findStudentsTeacher, 
'u':updatePrep, 
'e':addToDetention, 
'r':removeFromDetention, 
'k':checkDetention, 
'i':deletePrep,

Student:
'f':find,
'c':checkPrep,
'h':helpMe, 
quit

Any user can use "Student" operations, "Admin" can use all operations.

# Notes:
- Homework is only assigned to students which are currently in the class. New students will not be given any homework currently assigned

- This program is not sutible for teachers/students in multiple classes

- Teachers can only see/give their own students (in) detention, admins can see/give all students (in) detention

- Homework can only be assigned one at a time (no multiple homeworks for different dates)


# Future changes to this program:

High priority:
-add encryption in the scanner phase, or at least increased security
-If prep is handed in, prep automatically deleted (should really by changed by a setting)
-There is repeated code
-When removing a someone from the database/removing from detention, check if they were in the database to begin with and display a different message if not
-Dont allow homework to be made for a class that dosent exist
-for the try-excepts in menu, add feature to tell if it was a keypress error or an error in the procedure
-more helpful communication between the computer and the user

Medium priority:
-Have all of the users infomation ready loaded, so no need to repeat database operations (such as classroom a person belongs to)
-students can hand in prep early
find() print more user friendly infomation
-In addToDetention, check if student is found before asking for detention reason
-for deleteHomework, communicate if the inputted class in present in the database/prep is actually deleted
-checkprep more helpful error messages

Low priority:
-organise procedures to make sense to the user (IE all prep related procedures listed next to each other)
-Create gui for the database (at least change colour of terminal based on user preference, access level)
-spell check program
-messaging system between admins, teachers, and students
-further options for users, such as colour and detention length
-only allow users to type one leter, then auto-enter


#Credit
I have given credit to sources of helpful infomation while building this project within the code files. Those thanks will be moved to this section as soon as possibke






