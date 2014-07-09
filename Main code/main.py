import MOV as mov
import RPIO
import picamera

RPIO.setmode(RPIO.BCM)

i = [9,10,11,23,24,25]

for j in i:
    
    RPIO.setup(j, RPIO.OUT, initial = False)

camera = picamera.PiCamera()
camera.resolution = (640,480)
l = 0    
lv = 0
rec = True

c = True

print("Bienvenido a RaspByCar! Puedes haccer lo siguiente, ingresando la tecla indicada:");print ""
print( "Adelante: W")
print( "Atras: S")
print( "Derecha: D")
print( "Izquierda: A")
print( "Parar: Q")
print( "Tomar foto: F")
print( "Iniciar grabacion: R")
print( "Salir: X"); print "";print ""

while c:
	tecla = raw_input("Ingresa tu opcion: ")
	if tecla == "w":
		mov.on()
		mov.ade()
       		print "Adelante"

	elif tecla == "s":
		mov.on()
		mov.atras()
       		print "Atras"

	elif tecla == "a":
		mov.on()
		mov.izq()
       		print "Izquierda"

	elif tecla == "d":
       		mov.on()
		mov.der()
      		print "Derecha"

	elif tecla == "q":
		mov.parar()
		print "Para"
	elif tecla == "x":
       		print "SALIENDO, ADIOS!"
		c = False
	elif tecla == "f":
       		name = "foto"+str(l)+".jpg"
		camera.capture(name)
       		print "FOTO GUARDADA COMO: "+name
		l+=1
	elif tecla == "r":

		namevid = "video"+str(lv)+".h264"

		if rec:
			camera.start_recording(namevid)
			print "Iniciando grabacion!"
			rec = False
		else:
			camera.stop_recording()
			print "Grabacion detenida. Video guardado como: "+namevid
			lv +=1
			rec = True

RPIO.cleanup()





