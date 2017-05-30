import numpy as np
from suivi_trajectoire import *
from wrc_jawad import *
import matplotlib.pyplot as plt
import utm
import sys
import os
from bbio.libraries.Servo import *
import time

def evol_voilier(theta, v, w, delta_s, delta_r):
    dotX = (v*cos(theta), v*sin(theta), w, fs*sin(delta_s)-fr*sin(delta_r)-v, (1-cos(delta_s))*fs-cos(delta_r)*fr-w, cos(theta+delta_s)-v*sin(delta_s),v*sin(delta_r))
    
    return dotX

if __name__ == '__main__':
    
    #Choix de la mission
    for arg in sys.argv:
        nom_fichier = arg
    path = nom_fichier.split(".")
    #TESTS
#    pos_bat = [389193,5362474,389200,5362469,389201,5362460,389208,5362454]
    
    #CLEAR LOGS
    log_capteur = open("log_capteur", "w")
    log_gps = open("log_gps", "w")
       
    fic_min = open(path[0] + "/minimum","r")
    content_min = fic_min.read()
    fic_min.close()
    val_min = content_min.split("/")
    xmin = float(val_min[0])
    ymin = float(val_min[1])
    #Defintion des servomoteurs
    servo1 = Servo(PWM1A)
    servo2 = Servo(PWM1B)
    servo3 = Servo(PWM2A)
    
    #Position voilier
 
    try:
	gps_data = open("gps_data","r")
	gps = gps_data.readline()
    	gps_data.close()
   	gps_val = gps.split("/")
        pos_bat = point_gps(float(gps_val[0]),float(gps_val[1]))
        #pos_bat = point_gps(48.40736,-4.49544)
    #Navigation voilier
#    x_bat,y_bat = point_gps(48.40577,-4.49726)
    except:
	pos_bat = point_gps(0,0)

    liste = glob.glob(path[0] + "/carte_mission_U*")
    nb_objectif = len(liste)
    
    for i in range(nb_objectif):
        
        carte_mission_U = np.zeros((100,100))
        carte_mission_V = np.zeros((100,100))
        
        path_U = path[0] + "/carte_mission_U" + str(i)
        path_V = path[0] + "/carte_mission_V" + str(i)
        path_arrivee = path[0] + "/arrive" + str(i)
        
        tab_U = open(path_U,"r")
        content_U = tab_U.read()
        tab_U.close()
        vecteur_U = content_U.split("|")
        
        tab_V = open(path_V,"r")
        content_V = tab_V.read()
        tab_V.close()
        vecteur_V = content_V.split("|")

        fic_arrivee = open(path_arrivee)
        content_arrivee = fic_arrivee.read()
        fic_arrivee.close()
        arrivee = content_arrivee.split("/")
        
        compte = 0
        for i in range(100):
            for j in range(100):
                carte_mission_U[i,j] = float(vecteur_U[compte])
                carte_mission_V[i,j] = float(vecteur_V[compte])
                compte = compte + 1
                
        while (pow((pos_bat[0] - float(arrivee[0])),2) + pow((pos_bat[1] - float(arrivee[1])),2) > pow(5,2)):
            
            #-----------------
            # angle vent
            #-----------------
            try:
                girouette_data = open("girouette_data","r")
                gir = girouette_data.readline()
                if(int(gir,base=0) <= 360):
                    dir_vent = int(gir)
                    #angle du vent
                    psy = np.radians(dir_vent)
                    #LOG GIROUETTE
                    log_capteur.write('\nVent: %s' % dir_vent +'\n')
                    #print("Erreur lecture girouette")
                else:
                    psy = np.radians(0)
            except:
                print("Erreur girouette")
                log_capteur.write('\nVent: Erreur \n')
                psy = np.radians(0)

            #-----------------
            #cap voilier
            #-----------------
            razor_data = open("razor_data","r") 
            razor = razor_data.readline()
            razor = razor_data.readline()
            razor_data.close()
            razor_split = razor.split(",") #lire donnees boussole
            try:
            	if len(razor_split) > 1:
                 razor_yaw = razor_split[0].split("=")
                 if len(razor_yaw) > 1:
                     #LOG RAZOR
                     log_capteur.write('Razor: %s' % razor_yaw[1] +'\n')
                     #cap voilier
                     theta = np.radians(float(razor_yaw[1])+180)
                 else:
                     theta = 0
            	else:
                     theta = 0
            except:
                theta = 0
            #           print("theta",theta)
               
            #-----------------
            # position bateau
            #-----------------
            gps_data = open("gps_data","r") 
            gps = gps_data.readline()
            gps_data.close()
            gps_val = gps.split("/")
            try: 
            	if gps_val[0] != "'nan'":
                	pos_bat = point_gps(float(gps_val[0]),float(gps_val[1]))
	    except:
		pos_bat = point_gps(0,0)
            #pos_bat = point_gps(48.40736,-4.49544)
            #            compteur = compteur + 2
            #            bat = (pos_bat[compteur],pos_bat[compteur+1])
            
            #LOG GPS
	    try:
              log_capteur.write('GPS: %s' % gps_val[0] + ' - %s ' % gps_val[1] +'\n')
  	      log_gps.write('%s' % gps_val[0] + '/%s' % gps_val[1] +'\n')
            
	    except:
		log_capteur.write("GPS error\n")  
		
            #-----------------
            # Suivi de ligne voilier
            #-----------------
            #            print(carte_mission_U[])
            try:
                angle_safran, angle_max_voile, angle_max_foc, q, cap_souhaite = suivi_ligne(theta,psy,pos_bat,carte_mission_U,carte_mission_V,xmin,ymin)
            except:
                angle_safran = 0
            	angle_max_voile = 60
            	angle_max_foc = 105
            	cap_souhaite = 0 
            	print("Impossible de calculer de trajectoire")
            	log_capteur.write("Impossible de calculer trajectoire \n")
            
            angle_max_voile = np.degrees(angle_max_voile)
            angle_max_foc = np.degrees(angle_max_foc)
            		
            if(angle_max_voile > 135):
                angle_max_voile = 135
    	    elif(angle_max_voile < 60):
            	angle_max_voile = 60
            
            if(angle_max_foc > 120):
                angle_max_foc = 120
            elif(angle_max_foc < 105):
                angle_max_foc = 105
            	
            
            #controle des servomoteurs
            servo1.write(np.degrees(angle_safran)+82)
            servo2.write(angle_max_voile)
            servo3.write(angle_max_foc)
            
            log_capteur.write('Safran: %s' % str(np.degrees(angle_safran)+82) + '\n')
            log_capteur.write('Voile: %s' % str(angle_max_voile) + '\n')
            log_capteur.write('Foc: %s' % str(angle_max_foc) + '\n')
            log_capteur.write('Cap souhaite: %s' % str(np.degrees(cap_souhaite)) + '\n')
            
            log_capteur.write("-----------------")
        
        log_capteur.write("\n waypoint " + str(i) + " atteind") 
    log_capteur.close()
