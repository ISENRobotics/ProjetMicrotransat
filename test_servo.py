# First we must import PyBBIO: 
from bbio import *
# Then we can import Servo:
from bbio.libraries.Servo import *

# Create an instance of the Servo object:
servo1 = Servo(PWM1A)
servo2 = Servo(PWM1B)
# We could have left out the PWM pin here and used 
# Servo.attach(PWM1A) in setup() instead.

def setup():
  # Nothing to do here
  pass

def loop():
  #for angle in range(45):  # 0-180 degrees
   # servo1.write(angle)
    #delay(15)

  #for angle in range(45, 0, -1):  # 180-0 degrees
    #servo1.write(angle)
    #delay(15)
  servo1.write(120)
  #servo2.write(135)
  #angle = servo2.read()
  #print(angle)
run(setup, loop)
