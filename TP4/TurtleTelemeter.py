# -*- coding: utf-8 -*-
#INFO2 FAIT PAR 
# UNG Brondon - Dahiorus
# CHEAM Tony - TonyCheam
# BOUJU Tristan - battosai95
"""
Telemetry
"""
from sympy.geometry import Polygon,Line,Point,intersection
from sympy import N
import turtle
import random
from math import *
import numpy as np
import matplotlib.pyplot as plt
import time

def new_box(x,y,c):
    V = turtle.Turtle()
    V.hideturtle(); V.penup()
    V.setpos(x-c/2,y-c/2); V.setheading(0) ; V.pendown()
    for i in range(4):
        V.fd(c)
        V.left(90)
    return Polygon(Point(x-c/2,y-c/2),Point(x-c/2,y+c/2),Point(x+c/2,y+c/2),Point(x+c/2,y-c/2))

def telemetry(T,boxelist):
    a = radians(T.heading())
    P1,P2 = Point(T.xcor(),T.ycor()) , Point(T.xcor()+cos(a),T.ycor()+sin(a))
    P12 = P2 - P1
    intr = [N(P12.dot(p-P1)) for r in boxelist for p in intersection(Line(P1,P2),r) ]
    intr = [d for d in intr if d >= 0]
    #print intr
    return None if intr==[] else (min(intr)+np.random.normal(0,10))

'''
permet de tourner de 10deg par rapport à l'angle actuel
'''
def tourner(t, angle):
    t.setheading(t.heading()+angle)

'''
prend les valeurs tout les 10 deg et dessine les angles
'''
def prendreMesure(T, V):

    liste = range(72)
    
    for i in range(72):
        distance = telemetry(T,boxelist)
        V.fd(distance)
        tourner(V, 180)
        V.fd(distance)
        tourner(V, 180)
        print str( i ) + " " + str( T.heading() ) + " " + str( distance )

        #Toutes valeurs plus grande que 196 sont considere comme etant l infini
        if ( distance >= 197 and distance <= 296 ):
            distance = 500
        elif ( distance > 300 ):
            distance = 1000
        liste[i] = distance
        tourner(T, 5)
        tourner(V, 5)
    return liste

'''
la plus longue suite de l occur correspond au plus grand vide detecte
'''
# compte le nombre de mesures contigues menant a une sortie (i.e. >= mesure_max)
# renvoie le debut et la fin de l'intervalle de sortie
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

'''
permet de choisir la direction de la solution 
en connaissant son angle et celui de la solution
'''
def angleSolution( angleTurtle, angleSolution, T ):
    print angleTurtle
    print angleSolution

    print "left"
    #angleTurtle = angleTurtle + angleSolution
    T.left(angleSolution)

######### main ########
turtle.clearscreen()
T = turtle.Turtle()
T.penup()
T.tracer(2, 1)

#construction obstacle
boxelist = [ new_box(0,0,600) ]
boxelist = boxelist +[ new_box(150*cos(1+i*2*pi/15),150*sin(1+i*2*pi/15),random.randint(10,40)) for i in range(12)]

boxelist = boxelist +[ new_box(250*cos(1+i*2*pi/25),250*sin(1+i*2*pi/25),random.randint(10,40)) for i in range(24)]

#La tortue à un angle d'origine aléatoire
#La tortue V permet de dessiner les angles
V = turtle.Turtle()
T.setheading( random.randint( 0, 359 ) )
V.setheading( T.heading() )

V.pencolor("red")
V.fd(300)
tourner(V, 180)
V.fd(300)
tourner(V, 180)

V.pencolor("black")


#prise des valeurs et dessiner les angles
liste = prendreMesure(T, V)

#On colorie la sortie
T.pendown()
T.pencolor("blue")

#Choix de l'angle de sortie
#heading = compteOccurMax(liste, 1000)
debut, sortie = calcul_sortie(liste, 1000, 3)

if ( debut == -1 and sortie == -1 ):
    print "pas de sortie"
else:
    heading = (sortie+debut)/2

    #le tableau est de taille 74 et 
    angleSolution( T.heading(), heading*5, T)

    #sortie
    T.forward(0)
    T.forward( 300 )
raw_input()
