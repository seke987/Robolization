#! /usr/bin/env python3

import ev3dev.ev3 as ev3
import time
import utilities as util

#ev3.Sound.speak('I am a robot').wait()
#ev3.Sound.speak('I will rule the fucking world').wait()


def operateWheelsBasic():
    motorRight=ev3.LargeMotor('outA')
    motorLeft=ev3.LargeMotor('outD')
    motorRight.connected
    motorLeft.connected

    #ev3.Sound.speak('I am going sa la la la')

    motorRight.run_timed(speed_sp=500, time_sp=3000)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.YELLOW)
    motorLeft.run_timed(speed_sp=500, time_sp=3000)
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.YELLOW)
    time.sleep(0.5)

    waitForMotor(motorRight, motorLeft) 
    motorRight.run_timed(speed_sp=500, time_sp=4500)

    waitForMotor(motorRight, motorLeft)                        
    time.sleep(0.5)
    motorLeft.run_timed(speed_sp=500, time_sp=3000)
    motorRight.run_timed(speed_sp=500, time_sp=3000)

    waitForMotor(motorRight, motorLeft)
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
    ev3.Sound.speak('I stopped')
    time.sleep(1)

def waitForMotor(motorRight, motorLeft):
    time.sleep(0.1)         # Make sure that motor has time to start
    while motorRight.state==["running"]:             
        time.sleep(0.1)

    while motorLeft.state==["running"]:             
        time.sleep(0.1)

def infraSensor():
    infra = ev3.Sensor('in1:i2c8')
    motorRight=ev3.LargeMotor('outA')
    motorLeft=ev3.LargeMotor('outD')
    touch = ev3.TouchSensor('in2')
    motorRight.connected
    motorLeft.connected
    infra.connected
    touch.connected
    i = 0
    print (infra.mode)
    while 1:
            with open('/sys/class/lego-sensor/sensor1/value0') as infraFile: 
                waitForMotor(motorRight, motorLeft) 
                ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
                ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
                infraValue = infraFile.readline()
                
                if int(infraValue) < 5 and int(infraValue) > 0: 
                    waitForMotor(motorRight, motorLeft) 
                    motorRight.run_timed(speed_sp=400, time_sp=500)
                    motorLeft.run_timed(speed_sp=-400, time_sp=500)
                    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.YELLOW)

                elif int(infraValue) > 5 and int(infraValue) > 0:
                    waitForMotor(motorRight, motorLeft) 
                    motorLeft.run_timed(speed_sp=400, time_sp=500)
                    motorRight.run_timed(speed_sp=-400, time_sp=500)
                    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.YELLOW)

                elif int(infraValue) == 5:
                    waitForMotor(motorRight, motorLeft)                        
                    motorLeft.run_timed(speed_sp=400, time_sp=500)
                    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.YELLOW)
                    motorRight.run_timed(speed_sp=400, time_sp=500)
                    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.YELLOW)

                with open('/sys/class/lego-sensor/sensor2/value0') as touchFile:
                    touchValue = touchFile.readline()
                    if  int(touchValue) == 1:
                        waitForMotor(motorRight, motorLeft)                    
                        motorLeft.run_timed(speed_sp=-500, time_sp=1000)
                        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.YELLOW)
                        motorRight.run_timed(speed_sp=-500, time_sp=1000)
                        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.YELLOW)
                        waitForMotor(motorRight, motorLeft)
                        motorLeft.run_timed(speed_sp=1050, time_sp=1000)
                        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
                        motorRight.run_timed(speed_sp=1050, time_sp=1000)
                        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)

    
infraSensor()
#operateWheelsBasic()