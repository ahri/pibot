#!/usr/bin/env python

from composition import aflex2


def proto_lights():
    aflex2.digital_mode_write(1)
    aflex2.digital_mode_write(2)
    raw_input()

    p1_val = False
    p2_val = True
    while True:
        aflex2.pin_digital_write(1, p1_val)
        aflex2.pin_digital_write(2, p2_val)
        raw_input()
        p1_val = not p1_val
        p2_val = not p2_val


def proto_read():
    aflex.pin_digital_read(4)
    while True:
        print "Digital read of pin 4: %d" % aflex2.pin_digital_read(4)
        raw_input()


def proto_motors():
    aflex2.motor_current(100)

    while True:
        aflex2.motor_forward(1, 100)
        aflex2.motor_forward(2, 100)
        raw_input()
        aflex2.motor_stop(1)
        aflex2.motor_stop(2)
        raw_input()
        aflex2.motor_reverse_pc(1, 100)
        aflex2.motor_reverse_pc(2, 100)
        raw_input()
        aflex2.motor_stop(1)
        aflex2.motor_stop(2)
        raw_input()


def proto_motor_stepping():
    aflex2.motor_current(100)

    while True:
        for pc in xrange(0, 100, 10):
            aflex2.motor_forward(1, pc)
            aflex2.motor_forward(2, pc)
            raw_input()

        aflex2.motor_stop(1)
        aflex2.motor_stop(2)
        raw_input()

        for pc in xrange(100, 0, -10):
            aflex2.motor_forward(1, pc)
            aflex2.motor_forward(2, pc)
            raw_input()

        aflex2.motor_stop(1)
        aflex2.motor_stop(2)
        raw_input()


def proto_switch_read():
    while True:
        print "Switch value: %s" % aflex2.microswitch_read()
        print "Bits: %s" % (aflex2.microswitch_4bit_read(),)

        raw_input()


if __name__ == '__main__':
    print "Firmware Version: %d" % aflex2.firmware_version()
    print "Ready to go........."
    raw_input()

    proto_switch_read()
