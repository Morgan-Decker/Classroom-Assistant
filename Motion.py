#Thank you to freenove for demonstrating how one motion sensor would be operated
import RPi.GPIO as GPIO
import pygame
pygame.init()
#hello = pygame.mixer.Sound("/home/pi/Morgan Project/Hello.wav")
#goodbye = pygame.mixer.Sound("/home/pi/Morgan Project/Goodbye.wav")

#Define which sensor/led belongs to which pin
GreetingGoodbyeLED = 12 
GreetingGoodbyeSensor = 11    

GoodbyeLED = 16
GoodbyeSensor = 13


#Numbering the breadboard, defining inputs and outputs
def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(GreetingGoodbyeLED, GPIO.OUT)
	GPIO.setup(GreetingGoodbyeSensor, GPIO.IN)
	GPIO.setup(GoodbyeLED, GPIO.OUT)
	GPIO.setup(GoodbyeSensor, GPIO.IN)

#Searching for motion        
def loop():
	while True:
		if GPIO.input(GreetingGoodbyeSensor)==GPIO.HIGH:
			GPIO.output(GreetingGoodbyeLED,GPIO.HIGH)
			hello.play()

		elif GPIO.input(GoodbyeSensor)==GPIO.HIGH:
			GPIO.output(GoodbyeLED,GPIO.HIGH)
			goodbye.play()
			
		else :
			GPIO.output(GreetingGoodbyeLED,GPIO.LOW)
			
#shutting down the program
def destroy():
	GPIO.cleanup()                     

#The start of the program
if __name__ == '__main__':    
	setup()
	
	#Ctrl-c will stop the program 
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
