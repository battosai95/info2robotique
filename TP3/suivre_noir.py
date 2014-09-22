#!usr/bin/python2.7

import nxt, thread, time

b = nxt.find_one_brick()
roueDroite = nxt.Motor(b, nxt.PORT_B)
roueGauche = nxt.Motor(b, nxt.PORT_C)
flag = True

#################################################################
#CAPTEUR LUMIERE
#lux = nxt.sensor.Color20(b,nxt.PORT_3)

#lux.get_reflected_light(nxt.sensor.Type.COLORGREEN)

lux = nxt.sensor.Color20(b,nxt.PORT_3)
lux2 = nxt.sensor.Light(b,nxt.PORT_3)
#print lux2.get_lightness()
#print lux.get_reflected_light(nxt.sensor.Type.COLORFULL)

#################################################################
#CAPTEUR MOTEUR

#roueDroite.run(100)
#roueGauche.run(100)
#roueDroite.turn(100,180,brake=False)
#roueGauche.turn(100,-180,brake=False)

#roueDroite.weak_turn(-100,90)
#roueGauche.weak_turn(100, 90)

#time.sleep(1)
#roueDroite.brake()
#roueGauche.brake()

while True:
	valeurLedVerte = lux.get_reflected_light(nxt.sensor.Type.COLORGREEN)
	print valeurLedVerte
	if ( valeurLedVerte < 40 ):
		roueDroite.run(70)
		roueGauche.run(70)
		time.sleep(1)
		roueDroite.brake()
		roueGauche.brake()

	else:
		fin = time.time() + 1
		while time.time() < fin :
			valeurLedVerte = lux.get_reflected_light(nxt.sensor.Type.COLORGREEN)
			if ( valeurLedVerte > 40 ):
				roueDroite.run(70)
			roueDroite.brake()