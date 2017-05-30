import numpy as np
import codeAlJawad as vfl
import matplotlib.pyplot as plt
import utm

    
def carte_globale(latig,lonig,latsd,lonsd):
    xmin,ymin,zone,lettre = utm.from_latlon(latig, lonig)
    xmax,ymax,zone,lettre = utm.from_latlon(latsd, lonsd)
    return xmax,ymax,xmin,ymin
    
def point_gps(lat, lon):
    x,y,zone,lettre = utm.from_latlon(lat, lon)
    return x,y
    
#entree: coordonnees du waypoint
def objectif(X,Y,x,y):
    U, V = vfl.patrouille_circulaire(X, Y, x, y, K=1, R=10, turning_R=10)
    return U, V
    
#entree: coordonnees des deux extremites du segment
def trajectoire(X,Y,xa,ya,xb,yb):
    U, V = vfl.ligne(X,Y,xa,ya,xb-1,yb-1,R=10,K=1)
    return U, V

def bordure_carte(X,Y,debut_x,debut_y,fin_x,fin_y):
    xa,ya = point_gps(debut_x,debut_y)
    xb,yb = point_gps(fin_x,fin_y)  

    U0, V0 = vfl.limite(X, Y, xa, ya, xb, yb,R=10,K=1)
    
    carte_bord_U = U0
    carte_bord_V = V0
    
    return  carte_bord_U, carte_bord_V


    
def add_objectives(X,Y,depart,arrivee,bordure_U,bordure_V):
    
    Ut,Vt = trajectoire(X,Y,depart[0],depart[1],arrivee[0],arrivee[1])
    Uo, Vo = objectif(X,Y,arrivee[0],arrivee[1])
    
    carte_mission_U = bordure_U + Ut + Uo
    carte_mission_V = bordure_V + Vt + Vo
    
    return carte_mission_U,carte_mission_V
    
def dessine_carte(X,Y,carte_mission_U,carte_mission_V):#,x_bat,y_bat):    
    
    
#    plt.scatter(x_bat,y_bat,marker='o',color="r")
    
    plt.quiver(X, Y,carte_mission_U,carte_mission_V)
    
    
def dessine_points(x_bat,y_bat):    
    plt.scatter(x_bat,y_bat,s=2,marker='o',color="r") 
    
def show_graphs():
    plt.show()
    

