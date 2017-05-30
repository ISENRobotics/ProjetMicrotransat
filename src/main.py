from threading import Thread
import time
import os
import sys

class choix(Thread):

    def __init__(self,fonction):
        Thread.__init__(self)
	self.fonction = fonction

    def run(self):
        #Code a executer pendant l'execution du thread.
	if(self.fonction == "capteur"):
         os.system("python main_capteur.py")

	elif(self.fonction == "nav"):
         os.system("python main_nav.py " + nom_fichier)



if __name__ == '__main__':
    for arg in sys.argv:
            nom_fichier = arg
#    nom_fichier = "mission_isen.txt"
    os.system("python create_map.py " + nom_fichier)
    thread_nav = choix("nav")
    thread_capteur = choix("capteur")
    
    thread_capteur.start()
    thread_nav.start()
    
    thread_capteur.join() 
    thread_nav.join()
