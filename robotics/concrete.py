# coding: utf-8

class Aflex2(object):

    LEADER = 0xfe

    CMD_FIRMWARE_VERSION = 0x24
    CMD_MODE = 0x40
    CMD_DIGITAL_WRITE = 0x41
    CMD_DIGITAL_READ = 0x42
    CMD_MOTOR_FORWARD = 0x50
    CMD_MOTOR_REVERSE = 0x51
    CMD_MOTOR_STOP = 0x52
    CMD_MOTOR_CURRENT = 0x53
    CMD_SWITCH_READ = 0x54

    MODE_DIGITAL_INPUT = 0x00
    MODE_DIGITAL_OUTPUT = 0x01
    #MODE_ANALOG_INPUT = 0x05 # TODO: currently unused

    MAX_PWM = 250
    MAX_CURRENT_SCALE = 250

    def __init__(self, bus_address):
        self.bus_address = bus_address

    def _exec(self, *cmd_and_params):
        self.bus_address.write_byte(Aflex2.LEADER)
        for byte in cmd_and_params:
            self.bus_address.write_byte(byte)

    def digital_mode_read(self, pin):
        self._exec(Aflex2.CMD_MODE, pin, Aflex2.MODE_DIGITAL_INPUT)

    def digital_mode_write(self, pin):
        self._exec(Aflex2.CMD_MODE, pin, Aflex2.MODE_DIGITAL_OUTPUT)

    def digital_read(self, pin):
        self._exec(Aflex2.CMD_DIGITAL_READ, pin)
        return self.bus_address.read_byte()

    def digital_write(self, pin, val):
        self._exec(Aflex2.CMD_DIGITAL_WRITE, pin, val)

    def firmware_version(self):
        self._exec(Aflex2.CMD_FIRMWARE_VERSION)
        return self.bus_address.read_byte()

    def microswitch_read(self):
        self._exec(Aflex2.CMD_SWITCH_READ)
        return self.bus_address.read_byte()

    def microswitch_4bit_read(self):
        byte = self.microswitch_read()
        return tuple([bool(byte & pow(2, bit)) for bit in xrange(0, 4)])

    def motor_forward_pwm(self, num, pwm):
        self._exec(Aflex2.CMD_MOTOR_FORWARD, num, pwm)

    def motor_reverse_pwm(self, num, pwm):
        self._exec(Aflex2.CMD_MOTOR_REVERSE, num, pwm)

    def _pc_to_pwm(self, pc):
        return int((pc/100.0)*Aflex2.MAX_PWM)

    def motor_forward(self, num, pc):
        self.motor_forward_pwm(num, self._pc_to_pwm(pc))

    def motor_reverse(self, num, pc):
        self.motor_reverse_pwm(num, self._pc_to_pwm(pc))

    def motor_current(self, mA):
        val = int((mA/2000.0)*Aflex2.MAX_CURRENT_SCALE)
        self._exec(Aflex2.CMD_MOTOR_CURRENT, val)
