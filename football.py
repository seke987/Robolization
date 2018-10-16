#! /usr/bin/env python3

import ev3dev.ev3 as ev3
import time
import utilities as util

# ev3.Sound.speak('I am a robot').wait()
# ev3.Sound.speak('I will rule the fucking world').wait()
infra = ev3.Sensor('in1:i2c8')
motorRight = ev3.LargeMotor('outA')
motorLeft = ev3.LargeMotor('outD')
# touch = ev3.TouchSensor('in4')
ultra = ev3.UltrasonicSensor('in3')
motorRight.connected
motorLeft.connected
infra.connected
# touch.connected
ultra.connected


def runTimedR(speed, time):
    motorRight.run_timed(speed_sp=speed, time_sp=time)
    motorLeft.run_timed(speed_sp=(speed) * -1, time_sp=time)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.YELLOW)


def runTimedL(speed, time):
    motorLeft.run_timed(speed_sp=speed, time_sp=time)
    motorRight.run_timed(speed_sp=(speed) * -1, time_sp=time)
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.YELLOW)


def runTimed(speed, time):
    motorLeft.run_timed(speed_sp=speed, time_sp=time)
    motorRight.run_timed(speed_sp=speed, time_sp=time)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.YELLOW)
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.YELLOW)


def waitForMotor(motorRight, motorLeft):
    time.sleep(0.1)
    while motorRight.state == ["running"]:
        time.sleep(0.1)

    while motorLeft.state == ["running"]:
        time.sleep(0.1)


def zero():
    waitForMotor(motorRight, motorLeft)


def one():
    waitForMotor(motorRight, motorLeft)
    runTimedR(600, 400)


def two():
    waitForMotor(motorRight, motorLeft)
    runTimedR(550, 300)


def three():
    waitForMotor(motorRight, motorLeft)
    runTimedR(500, 200)


def four():
    waitForMotor(motorRight, motorLeft)
    runTimedR(400, 100)


def five():
    waitForMotor(motorRight, motorLeft)
    with open('/sys/class/lego-sensor/sensor3/value0') as ultraFile:
        ultraValue = ultraFile.read()
        if int(ultraValue) > 800:
            time = int(ultraValue) / 900 * 1000
            waitForMotor(motorRight, motorLeft)
            runTimed(900, time)
        elif int(ultraValue) > 400 and int(ultraValue) < 801:
            time = int(ultraValue) / 600 * 1000
            waitForMotor(motorRight, motorLeft)
            runTimed(600, time)
        elif int(ultraValue) < 401:
            time = int(ultraValue) / 300 * 1000
            waitForMotor(motorRight, motorLeft)
            runTimed(300, time)
        if int(ultraValue) < 250:
            waitForMotor(motorRight, motorLeft)
            runTimed(-300, 1000)
            time = (int(ultraValue) / 1050 * 1000) + 1000
            waitForMotor(motorRight, motorLeft)
            runTimed(1050, 1000)


        print (ultraValue)


def six():
    waitForMotor(motorRight, motorLeft)
    runTimedL(400, 100)


def seven():
    waitForMotor(motorRight, motorLeft)
    runTimedL(500, 200)


def eight():
    waitForMotor(motorRight, motorLeft)
    runTimedL(550, 300)


def nine():
    waitForMotor(motorRight, motorLeft)
    runTimedL(600, 400)


def infraValueDef(i):
    switcher = {
        0: zero,
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
    }

    func = switcher.get(i, lambda: "Invalid")
    return func()


"""def touch():
    with open('/sys/class/lego-sensor/sensor2/value0') as touchFile:
        touchValue = touchFile.readline()
        if  int(touchValue) == 1:
            waitForMotor(motorRight, motorLeft)   
            runTimed(-500,1000)
            waitForMotor(motorRight, motorLeft)
            runTimed(1050,1000)
"""


def main():
    i = 0
    with open('/sys/class/lego-sensor/sensor0/mode', 'w') as infraFile:
        infraFile.write('AC')
    print(infra.mode)
    while 1:
        with open('/sys/class/lego-sensor/sensor0/value0') as infraFile:
            waitForMotor(motorRight, motorLeft)
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
            infraValue = int(infraFile.readline())
            infraValueDef(infraValue)
        # touch()


main()
