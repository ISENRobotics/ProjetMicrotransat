# Voilier Autonome

## A propos

Auteurs : Esmé James / Théo Debay  
Projet M1 Isen Brest 2017  
Voilier autonome  

## Installation

* Linux kernel 3.8 avec une distribution Debian 7.9
* Installer les packages suivants
	* sudo apt-get install python2.7
	* sudo apt-get install python-pip
	* sudo apt-get update && apt-get install python-serial python-setuptools python-dev python-smbus python-pip
* Installer les bibliothèques python suivantes
	* pip install numpy==1.7.1
	* pip install utm==0.4.1
	* pip install matplotlib==1.3.0
	* pip install --upgrade PyBBIO  
		*Lien vers le github PyBBio https://github.com/graycatlabs/PyBBIO/wiki/Installing-PyBBIO*

## Pins capteurs et servomoteurs

* Servomoteur Safran : 9-14
* Servomoteur Grand-voile : 9-16
* Servomoteur Foc : 8-13
* Girouette : 9-40
* Centrale Inertielle Razor IMU - SEN-10736 : TX 9-24 / RX 9-26
* GPS : Port USB

## Lancer le programme de navigation

Lancer un screen afin que le programme tourne sans le lien avec l'ordinateur

	screen -S nom_screen  

Lancer le programme

	python main.py nom_mission.txt

Quitter le screen

	CTRL-a 
	d
	
