# -*- coding: utf-8 -*-
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

def tourner(t, angle):
    t.setheading(t.heading()+angle)

def prendreMesure(T, V):
    liste = range(37)
    
    for i in range(37):
        distance = telemetry(T,boxelist)
        V.fd(distance)
        tourner(V, 180)
        V.fd(distance)
        tourner(V, 180)
        print str( i*10 ) + " " + str( distance )
        if ( distance >= 197 ):
             distance = 500
        liste[i] = distance
        # i += 1
        tourner(T, 10)
        tourner(V, 10)
    return liste

def compte500(liste):
    indiceMax500 = 0
    indice500 = 0
    cptMax500 = 0
    cpt500 = 0
    flag = False

    for i in range(37):
        if ( liste[i] == 500 ):
            if ( flag == False ):
                flag = not flag
                indice500 = i
            cpt500 += 1
        else:
            if ( cpt500 > cptMax500 ):
                indiceMax500 = indice500
                cptMax500 = cpt500
    # return (indiceMax500 + cptMax500)/2
    return indiceMax500


######### main ########
turtle.clearscreen()
T = turtle.Turtle()
T.penup()
T.tracer(2, 1)

boxelist = [ new_box(0,0,400) ]
boxelist = boxelist +[ new_box(150*cos(1+i*2*pi/15),150*sin(1+i*2*pi/15),random.randint(10,40)) for i in range(12)]

V = turtle.Turtle()
T.setheading( random.randint( 0, 359 ) )
V.setheading( T.heading() )

# print telemetry(T,boxelist)

liste = prendreMesure(T, V)

T.pendown()
T.color(random.random(), random.random(), random.random())
heading = compte500(liste)*10
print heading
# tourner(T, heading )
T.setheading(compte500(liste)*10)
T.forward(0)
T.forward(150)

# plt.plot( liste )
# plt.show()




raw_input()
