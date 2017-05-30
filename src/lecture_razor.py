# serial_echo.py - Alexander Hiam - 4/15/12
#
# Prints all incoming data on Serial2 and echos it back.
#
# Serial2 TX = pin 21 on P9 header
# Serial2 RX = pin 22 on P9 header
#
# This example is in the public domain

from bbio import *
#def setup():
#	Serial1.begin(57600,timeout=1)
#	chaine = ''
#	pass
#def loop():
#	chaine = ''
#	for i in range(0,22):
#       		data = Serial1.read()
#       		chaine += data
#	print chaine
    # And write it back to the serial port:
#	Serial1.write(data)
  	# And a little delay to keep the Beaglebone happy:
#	delay(200)
#	return data

#run(setup,loop)

def setup():
  # Start Serial2 at 9600 baud:
  #Serial1.begin(57600)
  pass

def loop():
	Serial1.begin(57600)
	if (Serial1.available()):
    # There's incoming data
    		data = ''
    		for i in range(50):
      # If multiple characters are being sent we want to catch
      # them all, so add received byte to our data string and 
      # delay a little to give the next byte time to arrive:
      			data += Serial1.read()
      			delay(5)

    # Print what was sent:
#        print ("Data received:\n  '%s'" % data)
        	f = open("razor_data","w")
        	f.write(data)
        	f.close()
        	Serial1.end()
    # And write it back to the serial port:
    		#Serial1.write(data)
  # And a little delay to keep the Beaglebone happy:
  	#delay(200)
	
run(setup, loop)
