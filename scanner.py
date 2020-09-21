#A big thank you to Adrian (PyImageSearch), who supplied an excellent QR code scanner tutorial

from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import cv2
#Shutting down the stream correctly
def stop():
        cv2.destroyAllWindows()
        stream.stop()

#decrytping the value of the QR code
def decrypt(message):
        message = list(message)
        cracked = []
        for counter in range (0, len(message)):
                encoded = ord(message[counter]) - 5
                cracked.append(chr(encoded))
        cracked = ''.join(cracked)
        return cracked



# declare the stream variable and warm up the webcamera
stream = VideoStream(src=0).start()

# check every frame of the video stream
flag = True
while flag == True:
	# check the stream frame and set the maximum search width to 500 px
	frame = stream.read()
	frame = imutils.resize(frame, width=500)

	# look for a QR code in the frame
	finder = pyzbar.decode(frame)

	for QRcode in finder:
		# decode the barcode data and covert it into string
		name = QRcode.data.decode("utf-8")
		name = decrypt(name)

		# draw the QRcode data and QRcode type on the image
		stop()
		flag = False
		
	# show the output frame
	cv2.imshow("QRcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		exit()
database_recieve = name
