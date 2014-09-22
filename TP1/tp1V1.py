#!/usr/bin/python2
import turtle
import math
import random
   
'''
REGLE 1 :
- OBTENIR POSITION MOYENNE DE TOUT LES BOIDS : positionMoyenne()
- CALCULER LE VECTEUR VITESSE BOID[i] VERS LA POSITION MOYENNE : AB : xB - xA, yB - yA : vecteurVitesse()
- TRANSFORMER VITESSE EN ANGLE : speed2heading()
'''

boid=[] #tableau d'oiseaux
N=4 #nombre de oiseau
#zoneRepu = 3

#REGLE 1
def positionMoyenne():
    sx=0
    sy=0
    x=0
    y=0
    for i in range(N):
        x, y = boid[i].position()
        sx += x
        sy += y
    return sx / N, sy / N

def vecteurVitesse( x, y, xposM, yposM ):
    return xposM - x, yposM - y

def speed2heading(x,y):
    return math.atan2(y,x)*57.17

#REGLE 2
def angleMoyen():
    a = 0
    for i in range(N):
        a += boid[i].position()
    return a/N

#regle 2
def regle2():
    theta = angleMoyen() / 57.17 #57,17 360 -> 2pi
    return math.cos(theta), math.sin(theta)


posx=0;
posy=0;

for i in range(N):
    boid.append(turtle.Turtle())

#initialisation des parametres
for i in range(N):
    boid[i].penup() #ne pas tracer
    boid[i].setposition(random.randint(-100, 100), random.randint(-100, 100))
    boid[i].setheading(random.randint(0,359)) #angle de l'oiseau en degree
    boid[i].color(random.random(), random.random(), random.random())
    boid[i].pendown() #tracer deplacement

while True:

    #regle 1 : tout les oiseaux vont au centre
    
    for i in range(N):
        posx, posy = positionMoyenne()
        posx, posy = vecteurVitesse( boid[i].xcor(), boid[i].ycor(), posx, posy)
        boid[i].setheading( speed2heading( posx, posy ) )
        boid[i].forward(1)

raw_input()#attend que l'utilisateur frappe une touche pour quitter


