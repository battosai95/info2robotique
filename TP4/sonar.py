#!usr/bin/python2.7

import nxt, thread, time

b = nxt.find_one_brick()
roueDroite = nxt.Motor(b, nxt.PORT_B)
roueGauche = nxt.Motor(b, nxt.PORT_C)
sonar = nxt.sensor.Ultrasonic(b,nxt.PORT_1)

def terminer():
	roueGauche.run(0)
	roueDroite.run(0)
	exit(0)

#on fait environ 10 degree avec
#		roueDroite.run(80)
#		roueGauche.run(-80)
#		time.sleep ( 0.111 )
#nbr mesure 360deg = 38

def avance(droite, gauche):
	roueDroite.run(droite)
	roueGauche.run(gauche)
#end avance


def mesureSonnar( tab ):
	for i in range(37):
		avance(80, -80)
		tab.append(sonar.get_sample())
		time.sleep ( 0.111 )

try:
	tabInitial = []
	tabArrive = []
	
	mesureSonnar( tabInitial )
	print tabInitial

	avance(0, 0)
	time.sleep(1)

	mesureSonnar(tabArrive)
	print tabArrive

	terminer()
except KeyboardInterrupt:
	terminer()