import pyrebase
import serial
import time

# Firebase Configuration
config = {
  "apiKey": "AIzaSyDCcups_RmevmotsihjLB1E8gmWOIHfKbU",
  "authDomain": "home-6bb0a.firebaseapp.com",
  "databaseURL": "https://home-6bb0a.firebaseio.com",
  "storageBucket": "home-6bb0a.appspot.com",
  "messagingSenderId": "776927881717"
}


# Initializing Firebase
firebase = pyrebase.initialize_app(config)
db = firebase.database()


# Serial Configuration
ser = serial.Serial('/dev/ttyUSB0')

#Initializing Serial
ser.open()
ser.isOpen()



# Keep updating Firebase values
while True:
	
	led_1 = db.child("Leds").child("Led_1").get()

	if led_1.val() == "ON":
		serial_input = "On"
		#db.child("Leds").child("Led_1").set("OFF")

	else:
		serial_input = "Off"
		#db.child("Leds").child("Led_1").set("ON")
		
	ser.write(input)

	time.sleep(1)

