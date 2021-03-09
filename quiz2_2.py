from cs1robots import *
import time

create_world()
hubo = Robot(beepers = 2)
sleep_time = 0.5

def turn_around():
    for i in range(2):
        hubo.turn_left()

for i in range(2):
    time.sleep(sleep_time)
    hubo.move()
time.sleep(sleep_time)
hubo.drop_beeper()

time.sleep(sleep_time)
hubo.move()

for i in range(2):
    time.sleep(sleep_time)
    hubo.move()
time.sleep(sleep_time)
hubo.drop_beeper()

for i in range(2):
    time.sleep(sleep_time)
    hubo.turn_left()

for i in range(5):
    time.sleep(sleep_time)
    hubo.move()
turn_around()

while hubo.front_is_clear():
    if not hubo.on_beeper():
        print("No beeper!")
    time.sleep(sleep_time)
    hubo.move()

    if hubo.on_beeper():
        for i in range(2):
            time.sleep(sleep_time)
            hubo.turn_left()