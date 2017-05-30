import numpy as np
from suivi_trajectoire import *
from wrc_jawad import *
import matplotlib.pyplot as plt
import utm
import sys
import os
import glob

if __name__ == '__main__':
    
    nom_fichier = "mission_tycolo_1.txt"    
    path = nom_fichier.split(".")
    
    f_mission = open(nom_fichier,"r")
    f_mission.readline()
    f_mission.readline()
    bordure = f_mission.readline()
    coordonnee_bordure = bordure.split("/")
    f_mission.close()

    xmax,ymax,xmin,ymin = carte_globale(float(coordonnee_bordure[0]),float(coordonnee_bordure[1]),float(coordonnee_bordure[2]),float(coordonnee_bordure[3]))
    pas = 100j # (= taille des matrices)
    X, Y = np.mgrid[xmin:xmax:pas, ymin:ymax:pas]    

    
    #Recup carte
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
        
        dessine_carte(X,Y,carte_mission_U,carte_mission_V)
    
    #Recup trajet gps
    f_gps = open("donnees_gps.txt", "r")
    lignes = f_gps.readlines()
    nb_gps = len(lignes)
    f_gps.close()
    f_gps = open("donnees_gps.txt", "r")
    
    
    
    #dessine carte    
    
    for i in range(nb_gps):
            coordonnees = f_gps.readline()
            p_gps = coordonnees.split("/")
            x = point_gps(float(p_gps[0]),float(p_gps[1]))
            dessine_points(x[0],x[1])
#    dessine_carte(X,Y,carte_mission_U3,carte_mission_V3)
    show_graphs()
   
   