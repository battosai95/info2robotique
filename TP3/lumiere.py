import nxt, thread, time

b = nxt.find_one_brick()

lux = nxt.sensor.Color20(b,nxt.PORT_3)
lux2 = nxt.sensor.Light(b,nxt.PORT_3)
roueDroite = nxt.Motor(b, nxt.PORT_B)
roueGauche = nxt.Motor(b, nxt.PORT_C)


for i in range(30):
	print lux.get_reflected_light(nxt.sensor.Type.COLORGREEN)
	print
	time.sleep(1)