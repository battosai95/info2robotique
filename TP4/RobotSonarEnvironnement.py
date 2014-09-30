#!usr/bin/python2.7

import nxt, thread, time
from sympy.geometry import Polygon,Line,Point,intersection
from sympy import N
import turtle
import random
from math import *
import numpy as np
import matplotlib.pyplot as plt
import time

b = nxt.find_one_brick()
roueDroite = nxt.Motor(b, nxt.PORT_B)
roueGauche = nxt.Motor(b, nxt.PORT_C)
sonar = nxt.sensor.Ultrasonic(b,nxt.PORT_1)

def stop():
	roueGauche.run(0)
	roueDroite.run(0)

def terminer():
	stop()
	exit(0)

'''
permet de tourner de 10deg par rapport a l'angle actuel
'''
def tourner(t, angle):
    t.setheading(t.heading()+angle)

def avance(droite, gauche):
	roueDroite.run(droite)
	roueGauche.run(gauche)

def mesureSonnarRealTime( T, tab ):
	for i in range(37):
		avance(80, -80)
		time.sleep ( 0.075 )
		stop()
		tab[i] = sonar.get_sample() 
		turtleDessin1Obstacle( T, tab[i] )
		time.sleep ( 1 )

def turtleDessin1Obstacle( T, valeur ):
	T.forward( valeur )
	tourner(T, 180)
	T.forward( valeur )
	tourner(T, 180)
	tourner(T, 10)

def calcul_sortie(liste, mesure_max, long_inter):
    nb_mesures = 0
    i = 0

    while ( i < 2 * len(liste) ):
        if liste[ i%len(liste) ] >= mesure_max:
            nb_mesures += 1
        else:
            if nb_mesures >= long_inter:
                return i%len(liste) - nb_mesures, i%len(liste) 
            nb_mesures = 0
        i += 1
    return -1, -1

def angleSolution( angleSolution ):
    T.left(angleSolution)

def angleSolutionRobot( angleSolution ):
	for i in range(angleSolution):
		avance(80, -80)
		time.sleep ( 0.075 )
		stop()
		time.sleep ( 1 )

try:
	tabInitial = range(37)
	tabArrive = range(37)

	T = turtle.Turtle()
	T.tracer(2, 1)

	mesureSonnarRealTime( T, tabInitial )
	print tabInitial
	stop()

	debut, sortie = calcul_sortie(tabInitial, 255, 3)

	if ( debut == -1 and sortie == -1 ):
	    print "pas de sortie"
	else:
	    heading = (sortie+debut)/2
	    print heading
	    #le tableau est de taille 74 et 
	    angleSolutionRobot( heading )

	    #sortie
	    avance(80,80)
	    time.sleep(2)
	    avance(0,0)
	raw_input()
	terminer()
except KeyboardInterrupt:
	terminer()