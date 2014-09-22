import nxt, thread, time

b = nxt.find_one_brick()
mA = nxt.Motor(b, nxt.PORT_A)
mB = nxt.Motor(b, nxt.PORT_B)

#######################################################################
#########################   nxt.motor   ###############################
#######################################################################


## weak_turn(puissance,degres)
#
# Fonction non bloquante (rend immediatement la main)
# Avance d'environ moins 90 degres, et laisse la roue s'arreter d'elle meme
# Cette fonction a un bug:
# lors d'un changement de direction
# (si on alterne mA.weak_turn(-100,90) puis mA.weak_turn(100,90),
# il tourne bien plus de 90 degre.
# Ex d'utilisation:
# mA.


weak_turn(100,90)


## turn(puissance,degres)
#
# Fonction bloquante (ne rend la main qu'après la rotation de la roue)
# Ex:
# mA.turn(-100,90,brake=False)
# Recule d'au moins 90 degres, et laisse la roue s'arreter d'elle meme
#
# mA.turn(100,90,brake=True)
# Avance d'exactement 90 degres

## run(puissance)
#
# Fonction non bloquante. Doit etre suivie de run(0) ou brake()
# Ex:
# mA.run(100) ; time.sleep(1); mA.brake()

## brake()
#
# Arrete le moteur a l'angle actuel.
# Avec asservissement. Peut donc provoquer des oscillations avant/arriere
# contrairement a run(0) qui laisse le moteur s'arreter sans asservissement

#
# Autres fonctions potentiellement utiles: idle, reset_position

#
# Exemple de synchronisation des moteurs
# mA.run(100);mB.run(100);time.sleep(3);mA.brake();mB.brake()


#######################################################################
#########################   nxt.sensor  ###############################
#######################################################################

#
# SONAR
# Ex:
# sonar = nxt.sensor.Ultrasonic(b,nxt.PORT_1)
# print sonar.get_sample()
#
# A moins de 1 cm, peut renvoyer 255. A moins de 5cm, aucune precision.
# 0cm -> 255, 1cm -> 5, 2cm -> 6, 5cm -> 6, 10cm -> 12, 20cm -> 22, 30cm -> 30

#
# CAPTEUR DE CONTACT
# Ex: (ce code affiche True ou False)
# touche = nxt.sensor.Touch(b,nxt.PORT_2)
# print touche.get_sample()
# 
# 

# CAPTEUR DE COULEUR
#
# Pour capter l'intensite lumineuse ambiante (valeur entre 0 et 1000) 
# lux = nxt.sensor.Color20(b,nxt.PORT_3)
# lux.get_reflected_light(nxt.sensor.Type.COLORNONE)
#
# Allume la LED (verte, rouge ou bleue) et capte l'intensite (entre 0 et 1000)
# lux.get_reflected_light(nxt.sensor.Type.COLORGREEN)
# lux.get_reflected_light(nxt.sensor.Type.COLORRED)
# lux.get_reflected_light(nxt.sensor.Type.COLORBLUE)
#
# note: lux.get_light_color() bug: elle renvoie toujours la valeur 13 (=COLORFULL) quoi qu'il arrive
# lux.get_color() renvoie un entier entre 1 et 6

# lux2 = nxt.sensor.Light(b,PORT_3) allume la led en combinant R/V/B
# lux2.get_lightness() renvoie 1 ou 5 (ca fait quoi ?)
# lux.get_reflected_light(nxt.sensor.Type.COLORFULL) renvoie aussi 1 ou 5

