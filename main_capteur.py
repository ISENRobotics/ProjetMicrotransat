from threading import Thread
import time
import os

class choix(Thread):

    def __init__(self,fonction):
        Thread.__init__(self)
	self.fonction = fonction

    def run(self):
        #Code a executer pendant l'execution du thread.
	if(self.fonction == "razor"):
	        os.system("python lecture_razor.py")
		f_razor = open("razor_data")
		yaw = f_razor.read()
		f_razor.close()

		print(yaw)

	elif(self.fonction == "gps"):
		os.system("python gpsData.py")
		f_gps = open("gps_data")
		gps = f_gps.read()
		gps_split = gps.split("/")
		lat = gps_split[0]
		long = gps_split[1]
		f_gps.close()

		print(lat,long)

	elif(self.fonction == "girouette"):
		os.system("python lecture_girouette.py")
		f_gir = open("girouette_data")
		direction = f.read()
		f_gir.close()

		print(direction)

thread_razor = choix("razor")
thread_gps = choix("gps")
thread_girouette = choix("girouette")

thread_razor.start()
thread_gps.start()
thread_girouette.start()

thread_razor.join()
thread_gps.join() 
thread_girouette.join()
