#! /usr/bin/env python3

import ev3dev.ev3 as ev3
import time
import utilities as util
from random import randint


# ev3.Sound.speak('I am a robot').wait()
# ev3.Sound.speak('I will rule the fucking world').wait()
infra = ev3.Sensor('in1:i2c8')
motorRight = ev3.LargeMotor('outA')
motorLeft = ev3.LargeMotor('outD')
motorLittle = ev3.MediumMotor('outB')
# touch = ev3.TouchSensor('in4')
ultra = ev3.UltrasonicSensor('in3')
motorRight.connected
motorLeft.connected
motorLittle.connected
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
    #leftOrRight = randint(0, 50)
    #if leftOrRight < 25:
    #    runTimedR(200, 800)
    #else:
    #    runTimedL(200, 800)

def one():
    waitForMotor(motorRight, motorLeft)
    runTimedR(600, 400)


def two():
    waitForMotor(motorRight, motorLeft)
    runTimedR(550, 300)


def three():
    waitForMotor(motorRight, motorLeft)
    runTimedR(400, 200)


def four():
    waitForMotor(motorRight, motorLeft)
    runTimedR(200, 200)


def five():
    waitForMotor(motorRight, motorLeft)
    with open('/sys/class/lego-sensor/sensor2/value0') as ultraFile:
        ultraValue = ultraFile.read()
        if int(ultraValue) > 800:
            timeForRun = int(ultraValue) / 900 * 1000
            waitForMotor(motorRight, motorLeft)
            runTimed(900, timeForRun)
        elif int(ultraValue) > 400 and int(ultraValue) < 801:
            timeForRun = int(ultraValue) / 600 * 1000
            waitForMotor(motorRight, motorLeft)
            runTimed(600, timeForRun)
        elif int(ultraValue) < 401:
            timeForRun = int(ultraValue) / 300 * 1000 - 100
            waitForMotor(motorRight, motorLeft)
            runTimed(300, timeForRun)
        if int(ultraValue) < 250:
            with open('/sys/class/lego-sensor/sensor1/value0') as infraGoalFile:
                infraGoalValue = int(infraGoalFile.readline())
                motorRight.stop()
                motorLeft.stop()

                time.sleep(0.1)
                motorLittle.run_to_abs_pos(position_sp=20)
                time.sleep(1)
                if infraGoalValue == 0:
                    while infraGoalValue == 0:
                        runTimedR(200, 350)
                        waitForMotor(motorRight, motorLeft)
                        with open('/sys/class/lego-sensor/sensor1/value0') as infraGoalFile:
                            infraGoalValue = int(infraGoalFile.readline())
                            time.sleep(1)

                infraGoalValueDef(infraGoalValue)
                waitForMotor(motorRight, motorLeft)
                #with open('/sys/class/lego-sensor/sensor1/value0') as infraGoalFile:
                #    infraGoalValue = int(infraGoalFile.readline())

                #if infraGoalValue != 5:
                #    infraGoalValueDef(infraGoalValue)

                print(infraGoalValue)
                time.sleep(2.5)

                waitForMotor(motorRight, motorLeft)
                runTimed(-300, 1000)
                timeForRun = (int(ultraValue) / 1050 * 1000) + 1500

                waitForMotor(motorRight, motorLeft)
                motorLittle.run_to_abs_pos(position_sp=110)
                runTimed(1050, 1000)
                time.sleep(5)






def six():
    waitForMotor(motorRight, motorLeft)
    runTimedL(200, 200)


def seven():
    waitForMotor(motorRight, motorLeft)
    runTimedL(400, 200)


def eight():
    waitForMotor(motorRight, motorLeft)
    runTimedL(550, 300)


def nine():
    waitForMotor(motorRight, motorLeft)
    runTimedL(600, 400)

def zeroG():
    waitForMotor(motorRight, motorLeft)




def oneG():
    waitForMotor(motorRight, motorLeft)
    runTimedR(200, 1500)


def twoG():
    waitForMotor(motorRight, motorLeft)
    runTimedR(200, 1150)


def threeG():
    waitForMotor(motorRight, motorLeft)
    runTimedR(200, 750)


def fourG():
    waitForMotor(motorRight, motorLeft)
    runTimedR(200, 350)

def sixG():
    waitForMotor(motorRight, motorLeft)
    runTimedL(200, 350)


def sevenG():
    waitForMotor(motorRight, motorLeft)
    runTimedL(200, 750)


def eightG():
    waitForMotor(motorRight, motorLeft)
    runTimedL(200, 1150)


def nineG():
    waitForMotor(motorRight, motorLeft)
    runTimedL(200, 1500)

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

def infraGoalValueDef(i):
    switcher = {
        0: zeroG,
        1: oneG,
        2: twoG,
        3: threeG,
        4: fourG,
        5: zeroG,
        6: sixG,
        7: sevenG,
        8: eightG,
        9: nineG,
    }

    func = switcher.get(i, lambda: "Invalid")
    return func()


def main():
    i = 0
    with open('/sys/class/lego-sensor/sensor0/mode', 'w') as infraBallFile:
        infraBallFile.write('AC')
    with open('/sys/class/lego-sensor/sensor1/mode', 'w') as infraGoalFile:
        infraGoalFile.write('AC')
    motorLittle.reset()
    motorLeft.reset()
    motorRight.reset()
    while 1:
        with open('/sys/class/lego-sensor/sensor0/value0') as infraBallFile:
            waitForMotor(motorRight, motorLeft)
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
            motorLittle.speed_sp=150
            motorLittle.run_to_abs_pos(position_sp=110)

            #while motorLeft.state == ["running"]:
            #motorLittle.stop()
            infraValue = int(infraBallFile.readline())
            infraValueDef(infraValue)


main()
