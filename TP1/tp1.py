#!/usr/bin/python2
import turtle
import math
import random

vcte=10
boid=[] #tableau d'oiseaux
N=10 #nombre de oiseau
zoneRepu = 30
alpha=0.3
beta=0.5
gamma=5#1
rx=0; ry=0;
rx1=0; ry1=0
rx2=0; ry2=0
rx3=0; ry3=0

'''
REGLE 1 :
- OBTENIR POSITION MOYENNE DE TOUT LES BOIDS : positionMoyenne()
- CALCULER LE VECTEUR VITESSE BOID[i] VERS LA POSITION MOYENNE : AB : xB - xA, yB - yA : vecteurVitesse()
'''
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

#Determine le vecteur Boid[i]->Centre des Boids
def vecteurVitesse( x, y, xposM, yposM ):
	return xposM - x, yposM - y

'''
REGLE 2 :
- OBTENIR ANGLE MOYEN DE TOUT LES BOIDS : angleMoyen()
- CONVERTION ANGLE -> SPEED : heading2speed()
'''
def angleMoyen():
    a = 0
    for i in range(N):
        a += boid[i].heading()
    return a/N

'''
REGLE 3 :
- OBTENIR ANGLE MOYEN DE TOUT LES BOIDS : angleMoyen()
- CONVERTION ANGLE -> SPEED : heading2speed()
'''
def distanceVoisin(j):
	k=0
	repx=0; repy=0;
	sommeDistanceVoisin = map(range,[2] * (N-1) )
	for i in range(N):
		if ( i != j ):
			distance = boid[j].distance( boid[i] )
			if (  distance < zoneRepu ):
				sommeDistanceVoisin[k][0] = boid[i].xcor()
				sommeDistanceVoisin[k][1] = boid[i].ycor()
				k+=1
				repx += boid[i].xcor() - boid[j].xcor()
				repy += boid[i].ycor() - boid[j].ycor()
	if ( k > 0):
		#repx, repy = vecteurVitesse( boid[j].xcor(), boid[j].ycor(), repx/k, repy/k )
		return -repx/k, -repy/k
	return 0, 0

#Conversion angle -> vitesse et vitesse -> angle
def heading2speed(angle):
	return vcte*math.cos(angle/57.17), vcte*math.sin(angle/57.17)
    
def speed2heading(x,y):
	return math.atan2(y,x)*57.17
     
#MAIN
for i in range(N):
    boid.append(turtle.Turtle())

#initialisation des parametres
for i in range(N):
    boid[i].penup() #ne pas tracer
    boid[i].setposition(random.randint(-100, 100), random.randint(-100, 100))
    boid[i].setheading(random.randint(0,359)) #angle de l'oiseau en degree
    boid[i].color(random.random(), random.random(), random.random())
    #boid[i].pendown() #tracer deplacement
    boid[i].speed("fastest")

while True:

	#regle 1 : tout les oiseaux vont au centre
	xPosMoy, yPosMoy = positionMoyenne()
	angleMoy = angleMoyen()
	for i in range(N):
		rx1, ry1 = vecteurVitesse( boid[i].xcor(), boid[i].ycor(), xPosMoy, yPosMoy )
		
		rx2, ry2 = heading2speed( angleMoy )
		
		rx3, ry3 = distanceVoisin( i )
		
		rx = alpha*rx1 + beta*rx2 + gamma*rx3
		ry = alpha*ry1 + beta*ry2 + gamma*ry3
		
		boid[i].setheading( speed2heading( rx, ry) )
		boid[i].tracer()
		boid[i].forward(vcte)


raw_input()#attend que l'utilisateur frappe une touche pour quitter


