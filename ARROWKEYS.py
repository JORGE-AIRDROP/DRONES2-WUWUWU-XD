
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk



def set_velocity_body(vehicle, vx, vy, vz):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0, 0,
            mavutil.mavlink.MAV_FRAME_BODY_NED,
            0b0000111111000111, #-- BITMASK -> Consider only the velocities
            0, 0, 0,        #-- POSITION
            vx, vy, vz,     #-- VELOCITY
            0, 0, 0,        #-- ACCELERATIONS
            0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()


#### your code here #####
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



def key(event):
    if event.char == event.keysym: #-- standard keys
        if event.keysym == 'r':
            drone.mode = VehicleMode("RTL")
    else: #-- non standard keys
        if event.keysym == 'Up':
            set_velocity_body(drone,5,0,0)
        elif event.keysym == 'Down':
            set_velocity_body(drone,-5,0,0)
        elif event.keysym == 'Left':
            set_velocity_body(drone,0,-5,0)
        elif event.keysym == 'Right':
            set_velocity_body(drone,0,5,0)
#****************************************************************************
#   MAIN CODE
#
#****************************************************************************

drone = connect('127.0.0.1:14551' , wait_ready=True)

# Take off to 10 m altitude
arm_and_takeoff(10)
 
# Read the keyboard with tkinter
root = tk.Tk()
print(">> Control the drone with the arrow keys. Press r for RTL mode")
root.bind_all('<Key>', key)
root.mainloop()