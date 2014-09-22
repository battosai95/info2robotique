#!usr/bin/python2.7

import nxt, thread, time

##################
#	Variable	 #
##################

#Necessaire pour le robot
b = nxt.find_one_brick()				#detection du robot
roueDroite = nxt.Motor(b, nxt.PORT_B)	#roue droite
roueGauche = nxt.Motor(b, nxt.PORT_C)	#roue gauche

#Flag
flag = True
flagRechercheNoir = True 	#Active la recherche de la ligne noir
flagNoir = False 			#Permet de savoir si on est toujours sur la ligne noir

#Lumière
lux = nxt.sensor.Color20(b,nxt.PORT_3)	#Active les détecteurs de lumière du capteur
lux2 = nxt.sensor.Light(b,nxt.PORT_3)

##################
#	Fonction	 #
##################

#permet de tourner le robot vers la droite de 45°
def diagonalDroite( puissance, angle ) :
	roueGauche.weak_turn( puissance, angle )

#De même mais vers la gauche
def diagonalGauche( puissance, angle ):
	roueDroite.weak_turn( puissance, angle )

#Arrete le robot
def stop():
	roueDroite.brake()
	roueGauche.brake()

#Fais avancer le robot
def avancer( puissance ):
	roueDroite.run( puissance )
	roueGauche.run( puissance )

#Permet de connaître la valeur precedente et actuelle du capteur
def ledVerte():
	previousValue = valeurLedVerte
	valeurLedVerte = lux.get_reflected_light(nxt.sensor.Type.COLORGREEN)
	return valeurLedVerte

#Permet de choisir la diagonale gauche ou droite
#Le robot zigzague quand il est sur la ligne
def choisirDiagonale( puissance, angle ):
	if ( flag ):
		diagonalDroite( puissance, angle )
	else:
		diagonalGauche( puissance, angle )
	flag = not flag

#On pense avoir trouver la ligne
def ligneNoirTrouve():
	stop()					#on arrete le robot
	flagNoir = True 		#on prépare une boucle
	debut = time.time()		#on enregistre le temps actuel
	avancer( 70 )			#Le robot avance doucement

	while flagNoir == True:
		#tant qu'il ne sort pas de la ligne et qu'il y reste pendant 2secondes
		#alors on est sur que c'est la ligne
		if ( ledVerte() > 40 && ( ( time.time() - debut ) > 2 ) :	
			choisirDiagonale( 100, 90 )	#permet de choisir la diagonale
			flagNoir = False

##################
#		MAIN	 #
##################

valeurLedVerte = lux.get_reflected_light(nxt.sensor.Type.COLORGREEN)
choisirDiagonale( 100, 45 )

while True:
	avancer( 70 )
	ledVerte()

	print valeurLedVerte
	
	if ( valeurLedVerte > 40 ):
		if ( previousValue < 40 ):
			choisirDiagonale( 100, 45 )

		else:
			while ( flagRechercheNoir ):

				if ( ledVerte() < 40 ):
					ligneNoirTrouve()
					flagRechercheNoir = False

			flagRechercheNoir = True
#################################################################
#CAPTEUR LUMIERE
#lux = nxt.sensor.Color20(b,nxt.PORT_3)

#lux.get_reflected_light(nxt.sensor.Type.COLORGREEN)


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