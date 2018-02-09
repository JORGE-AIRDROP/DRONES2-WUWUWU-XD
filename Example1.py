from  dronekit import connect, VehicleMode, LocationGlobalRelative
import time

#Primero que nada este comando define la altura  para que comience a volar.
def arm_and_takeoff(TargetAltitude):
#Vehicle Connection
#Cuando esta listo dira que va a empezar a volar.
	print ("Executing Takeoff")

#En caso de que no pueda volar nos dira qeu aun no puede despegar y esperara un segundo para voolver a intentarlo.
	while not drone.is_armable:
		print ("Vehicle is not armable, waiting...")
		times.sleep(1)
#Una vez que este armado nos dira y el "Guided" es para que podamos volarlo y controlar el dron desde el codigo.
	print ("Ready to arm")
	drone.mode = VehicleMode("GUIDED")
	drone.armed = True
#Hasta que este listo nos dira que esta esperando a ser armado cada segundo.
	while not drone.armed:
		print("Waiting for arming...")
		time.sleep(1)

#Cuando este todo preparado dira que esta listo y empezara a despegar y lo podremos ver en el mission planer.
	print("Ready for takeoff, taking off...")
#El target altitude es para que el dron vaya a la altura que queramos.	
	drone.simple_takeoff(TargetAltitude)
#El drone tomara su altura relativa a la altura en la que esta y no al nivel del mar, y no ira diciendo la altura en
#la que esta en todo momento hasta llegar a la altura deseado y nos dira que llego. 

	while True:
		Altitude = drone.location.global_relative_frame.alt
		print("Altitude", Altitude)
		time.sleep(1)
		
		if Altitude >= TargetAltitude * 0.95:
			print("Altitude reached")
			break



#Vehicle Connection
#Esto es basicamente la direccion que tiene el dron para que lo podamos conectar en las terminales de Ubuntu.
#Y la velocidad a la que esta yendo al igual que la altura que queremos.

drone = connect('127.0.0.1:14551' , wait_ready=True)
arm_and_takeoff(20)
drone.airspeed = 10

#Estas cuatro lineas de codigo son para darles las cordenadas a nuestro dron de a donde tiene que ir en la mision.
a_location = LocationGlobalRelative(20.7377260, -103.4570155, 20)
b_location = LocationGlobalRelative(20.7376890, -103.4565404, 20)
c_location = LocationGlobalRelative(20.7371951, -103.4565840, 20)
d_location = LocationGlobalRelative(20.7372334, -103.4570624, 20)
print("Despegue Exitoso")
print("Going to point a")
#Esto que queda sirve para que el dron vaya a las cordenadas y regrese a casa.
drone.simple_goto(a_location)
time.sleep(40)
print("a location reached going to point b")

drone.simple_goto(b_location)
time.sleep(40)
print("b location reached going to point c")

drone.simple_goto(c_location)
time.sleep(40)
print("c location reached going to point d")

drone.simple_goto(d_location)
time.sleep(40)
print("d location reached going home")

drone.mode = VehicleMode("RTL")
print("The drone is home")
#Por ultimo este codigo sirve para que nos diga la bateria de nuestro dron al terminar la mision.
print(drone.battery.level)

