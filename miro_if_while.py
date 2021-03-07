from cs1robots import *
import time

create_world(avenues=7, streets=7)
hubo = Robot(beepers = 10)
sleep_time = 0.5

# 시작점에 비퍼 놓는다
hubo.drop_beeper()

# 벽 만날때 까지 전진
while not hubo.on_beeper():
    if hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()

