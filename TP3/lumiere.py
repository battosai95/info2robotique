import nxt, thread, time

b = nxt.find_one_brick()

lux = nxt.sensor.Color20(b,nxt.PORT_3)
lux2 = nxt.sensor.Light(b,nxt.PORT_3)
roueDroite = nxt.Motor(b, nxt.PORT_B)
roueGauche = nxt.Motor(b, nxt.PORT_C)

def terminer():
	roueGauche.run(0)
	roueDroite.run(0)
	lux.get_reflected_light(nxt.sensor.Type.COLORNONE)
	exit(0)

try:
	while True:
		roueDroite.run(60)
		roueGauche.run(60)
		roueDroite.turn(100,90,brake=True)
		print lux.get_reflected_light(nxt.sensor.Type.COLORGREEN)
		print
except KeyboardInterrupt:
	terminer()