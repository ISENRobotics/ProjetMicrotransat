import numpy as np
from codeAlJawad import *
#import wrc_jawad as carte
from wrc_jawad import *
import matplotlib.pyplot as plt
import utm
from math import *

def cap_suivre(x_bat,y_bat,carte_U,carte_V,xmin,ymin):
   # print("Y bat",y_bat)
    #print("Y min",ymin)
    #print("X bat",x_bat)
    #print("X min",xmin)
    #print("Index X",x_bat-xmin)
    #print("Index Y",y_bat - ymin)
    theta = atan(carte_V[(x_bat-xmin)][(y_bat - ymin)]/carte_U[(x_bat-xmin)][(y_bat - ymin)])
#    theta = atan(carte_V[x_bat][y_bat]/carte_U[x_bat][y_bat])
    
    return theta
    
def suivi_ligne(theta,psy,m,carte_U,carte_V,xmin,ymin):
    
    #CLEAR LOGS
    #log_cap_souhaite = open("log_cap_souhaite", "w")    
    #log_angle_safran = open("log_angle_safran", "w")    
    #log_angle_voile = open("log_angle_voile", "w")    
  
    #angle de la voile pour un vent de travers (a determiner experimentalement)
    beta = 0.3
    angle_max_safran = np.pi/4   
    #angle de vent le plus serre (close-hauled) = angle louvoiement
    sigma = np.pi/3
    #angle incidence
    #gamma_inf = np.pi/4    
    
    #cap souhaite pour le voilier (pas de prise en compte du vent)
    theta_barre = cap_suivre(m[0],m[1],carte_U,carte_V,xmin,ymin)
    if theta_barre <= 0:
        q = -1
    elif theta_barre > 0:
        q = 1


    #Si cos(psy - theta_barre) + cos(sigma) < 0
    #   cap a suivre trop pres du vent -> impossible a suivre
    #   ---> mode de navigation face au vent    
    if (np.cos(psy - theta_barre) + np.cos(sigma) < 0): 
        #cap souhaite = direction vent +- angle louvoiement        
        theta_barre = np.pi + psy - q*sigma
    
    #LOG CAP SOUHAITE
    #log_cap_souhaite.write('%s' % np.degrees(theta_barre) +'\n')
    
    #definition de l'angle du safran pour que le voilier suive le cap voulu
    if np.cos(theta-theta_barre) >= 0:
        angle_safran = angle_max_safran*np.sin(theta-theta_barre)
    else:
        angle_safran = angle_max_safran*np.sign(theta-theta_barre)

    #LOG ANGLE SAFRAN
    #log_angle_safran.write('%s' % np.degrees(angle_safran) +'\n')
        
    
    #angle maximal d'ouverture de la voile
    angle_max_voile = pow((np.pi/2)*((np.cos(psy-theta_barre)+1)/2),log10(np.pi/2*beta)/log10(2))
#    print("angle_max_voile",angle_max_voile)
    angle_max_foc = pow((np.pi/2)*((np.cos(psy-theta_barre)+1)/2),log10(np.pi/2*beta)/log10(2))
    
       
    #LOG ANGLE SAFRAN
    #log_angle_voile.write('%s' % np.degrees(angle_max_voile)+82 +'\n')
    
    print("safran",np.degrees(angle_safran)+82)
    print("voile",np.degrees(angle_max_voile))
    print("cap souhaite",np.degrees(theta_barre))
    print("pos_bat", m)
    print("------")
    #log_angle_voile.close()
    #log_angle_safran.close()
    #log_cap_souhaite.close()
    return angle_safran, angle_max_voile, angle_max_foc, q, theta_barre

