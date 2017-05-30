from bbio import *

pot1 = AIN1 # pin 40 on header P9 

def setup():
  # Nothing to do here
  pass

def loop():
  direction = 0
  # Get the ADC values:
  val1 = analogRead(pot1)
  # And convert to voltages:
  voltage1 = inVolts(val1)
  #print voltage1
  if voltage1 >= 0 and voltage1 <= 0.02:
        #print "Facing East"
	direction = 90
  elif voltage1 >= 0.03 and voltage1 <= 0.04:
        #print "Facing South-East"
	direction = 135
  elif voltage1 >= 0.06 and voltage1 <= 0.07:
        #print "Facing South"
        direction = 180
  elif voltage1 >= 0.12 and voltage1 <= 0.15:
        #print "Facing North-East"
        direction = 45
  elif voltage1 >= 0.22 and voltage1 <= 0.24:
        #print "Facing South-West"
        direction = 225
  elif voltage1 >= 0.43 and voltage1 <= 0.44:
        #print "Facing North"
        direction = 0
  elif voltage1 >= 0.75 and voltage1 <= 0.77:
        #print "Facing North-West"
        direction = 315
  elif voltage1 >= 1.17:
        #print "Facing West"
        direction = 270
  else:
	#print "I'm lost :("
        direction = 400
 
  
  f = open('girouette_data','w')
  dir = str(direction)
  f.write(dir)
  f.close()
# Start the loop:
run(setup, loop)
