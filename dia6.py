# Créditos: código del equipo "Rocky", ganador del torneo de robot-sumo (RoDI)

import rodi
import time

robot = rodi.RoDI()

# Música: "Gonna Fly Now" por Bill Conti (Theme from Rocky)
def rocky_song():
    robot.sing(659.26,125)
    time.sleep(0.125)
    robot.sing(783.99,375)
    time.sleep(0.375)
    robot.sing(880,1000)
    time.sleep(1.75)
    robot.sing(880,125)
    time.sleep(0.125)
    robot.sing(987.77,375)
    time.sleep(0.375)
    robot.sing(659.26,1000)
    time.sleep(1.75)
    robot.sing(659.26,125)
    time.sleep(0.125)
    robot.sing(783.99,375)
    time.sleep(0.375)
    robot.sing(880,1000)
    time.sleep(1.75)
    robot.sing(880,125)
    time.sleep(0.125)
    robot.sing(987.77,375)
    time.sleep(0.375)
    robot.sing(659.26,1000)
    time.sleep(2)
    robot.sing(587.33,125)
    time.sleep(0.125)
    robot.sing(523.25,125)
    time.sleep(0.125)
    robot.sing(587.33,375)
    time.sleep(0.375)
    robot.sing(523.25,125)
    time.sleep(0.125)
    robot.sing(587.33,125)
    time.sleep(0.125)
    robot.sing(659.26,875)
    time.sleep(1)
    robot.sing(1046.5,125)
    time.sleep(0.125)
    robot.sing(1046.5,125)
    time.sleep(0.125)
    robot.sing(987.77,250)
    time.sleep(0.250)
    robot.sing(987.77,125)
    time.sleep(0.125)
    robot.sing(880,125)
    time.sleep(0.125)
    robot.sing(880,125)
    time.sleep(0.125)
    robot.sing(880,125)
    time.sleep(0.125)
    robot.sing(783.99,500)
    time.sleep(0.5)
    robot.sing(698.46,250)
    time.sleep(0.250)
    robot.sing(659.26,2000)
    time.sleep(2)

# Música: "Estrellita, ¿dónde estás?" (Canción popular)
def estrellita_song():
    robot.sing(523.25,500)
    time.sleep(0.5)
    robot.sing(523.25,500)
    time.sleep(0.5)
    robot.sing(783.99,500)
    time.sleep(0.5)
    robot.sing(783.99,500)
    time.sleep(0.5)
    robot.sing(880,500)
    time.sleep(0.5)
    robot.sing(880,500)
    time.sleep(0.5)
    robot.sing(783.99,1000)
    time.sleep(1)
    robot.sing(698.46,500)
    time.sleep(0.5)
    robot.sing(698.46,500)
    time.sleep(0.5)
    robot.sing(659.26,500)
    time.sleep(0.5)
    robot.sing(659.26,500)
    time.sleep(0.5)
    robot.sing(587.33,500)
    time.sleep(0.5)
    robot.sing(587.33,500)
    time.sleep(0.5)
    robot.sing(523.25,1000)
    time.sleep(1)

# Bucle: dar instrucciones al robot por comandos individuales en tiempo real
while True:

    comando = input("Ingrese un comando: ")

    if comando == "w":
        robot.move_forward()
        time.sleep(0.01)

    if comando == "x":
        robot.move_backward()
        time.sleep(0.01)

    if comando == "a":
        robot.move_left()
        time.sleep(0.05)

    if comando == "d":
        robot.move_right()
        time.sleep(0.01)

    if comando == "s":
        robot.move_stop()
        time.sleep(0.01)

    if comando == "m":
        rocky_song()
        time.sleep(0.01)

    if comando == "n":
        estrellita_song()
        time.sleep(0.01)