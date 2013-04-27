#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase, main as test_main
from doublex import Mock, verify
from hamcrest import assert_that, equal_to
from bus.api import ABus, ABusAddress
from robotics import Aflex2


CMD_LEADER = 0xfe
CMD_VERSION = 0x24
CMD_MODE = 0x40
CMD_DIGITAL_WRITE = 0x41
CMD_DIGITAL_READ = 0x42
CMD_MOTOR_FORWARD = 0x50
CMD_MOTOR_REVERSE = 0x51
CMD_MOTOR_STOP = 0x52
CMD_MOTOR_CURRENT = 0x53
CMD_SWITCH_READ = 0x54


# ABoardFirmwareVersion
class TestAflex2FirmwareVersion(TestCase):

    def test_run(self):
        # Arrange
        READ_BYTE = 0x00

        with Mock(ABusAddress) as mock_bus_address:
            for byte in CMD_LEADER, CMD_VERSION:
                mock_bus_address.write_byte(byte)

            mock_bus_address.read_byte().returns(READ_BYTE)

        board = Aflex2(mock_bus_address)

        # Act
        ret = board.firmware_version()

        # Assert
        assert_that(ret,
                    equal_to(READ_BYTE))
        assert_that(mock_bus_address, verify())


# ABoardMicroswitchRead
class TestAflex2MicroswitchRead(TestCase):

    def test_run(self):
        # Arrange
        READ_BYTE = 0x00

        with Mock(ABusAddress) as mock_bus_address:
            for byte in CMD_LEADER, CMD_SWITCH_READ:
                mock_bus_address.write_byte(byte)

            mock_bus_address.read_byte().returns(READ_BYTE)

        board = Aflex2(mock_bus_address)

        # Act
        ret = board.microswitch_read()

        # Assert
        assert_that(ret,
                    equal_to(READ_BYTE))
        assert_that(mock_bus_address, verify())


# ABoardMicroswitch4bitRead
class TestAflex2Microswitch4BitRead(TestCase):

    def test_run(self):
        # Arrange
        READ_BYTE = 0x0a

        with Mock(ABusAddress) as mock_bus_address:
            for byte in CMD_LEADER, CMD_SWITCH_READ:
                mock_bus_address.write_byte(byte)

            mock_bus_address.read_byte().returns(READ_BYTE)

        board = Aflex2(mock_bus_address)

        # Act
        ret = board.microswitch_4bit_read()

        # Assert
        assert_that(ret,
                    equal_to((False, True, False, True)))
        assert_that(mock_bus_address, verify())


# ABoardMotorCurrent
class TestAflex2MotorCurrent(TestCase):

    def test_run(self):
        # Arrange
        PERCENT_MAX = 100

        # aflex2 works with a 10-250 current scale
        SCALED_MAX = 250

        with Mock(ABusAddress) as mock_bus_address:
            for byte in CMD_LEADER, CMD_MOTOR_CURRENT, SCALED_MAX:
                mock_bus_address.write_byte(byte)

        board = Aflex2(mock_bus_address)

        # Act
        pc = PERCENT_MAX
        board.motor_current(pc)

        # Assert
        assert_that(mock_bus_address, verify())


# ABoardMotorPwm
class TestAflex2MotorPwm(TestCase):

    def test_forward(self):
        # Arrange
        MOTOR = 0x01
        PWM = 0xaa

        with Mock(ABusAddress) as mock_bus_address:
            for byte in CMD_LEADER, CMD_MOTOR_FORWARD, MOTOR, PWM:
                mock_bus_address.write_byte(byte)

        board = Aflex2(mock_bus_address)

        # Act
        num = MOTOR
        val = PWM
        board.motor_forward_pwm(num, val)

        # Assert
        assert_that(mock_bus_address, verify())

    def test_reverse(self):
        # Arrange
        MOTOR = 0x01
        PWM = 0xaa

        with Mock(ABusAddress) as mock_bus_address:
            for byte in CMD_LEADER, CMD_MOTOR_REVERSE, MOTOR, PWM:
                mock_bus_address.write_byte(byte)

        board = Aflex2(mock_bus_address)

        # Act
        num = MOTOR
        val = PWM
        board.motor_reverse_pwm(num, val)

        # Assert
        assert_that(mock_bus_address, verify())


# ABoardMotor
class TestAflex2Motor(TestCase):

    def test_forward(self):
        # Arrange
        MOTOR = 0x01
        PWM = 0x32

        with Mock(ABusAddress) as mock_bus_address:
            for byte in CMD_LEADER, CMD_MOTOR_STOP, MOTOR:
                mock_bus_address.write_byte(byte)

        board = Aflex2(mock_bus_address)

        # Act
        num = MOTOR
        board.motor_stop(num)

        # Assert
        assert_that(mock_bus_address, verify())

    def test_forward(self):
        # Arrange
        MOTOR = 0x01
        PWM = 0x32

        with Mock(ABusAddress) as mock_bus_address:
            for byte in CMD_LEADER, CMD_MOTOR_FORWARD, MOTOR, PWM:
                mock_bus_address.write_byte(byte)

        board = Aflex2(mock_bus_address)

        # Act
        num = MOTOR
        pc = 20
        board.motor_forward(num, pc)

        # Assert
        assert_that(mock_bus_address, verify())

    def test_reverse(self):
        # Arrange
        MOTOR = 0x01
        PWM = 0x32

        with Mock(ABusAddress) as mock_bus_address:
            for byte in CMD_LEADER, CMD_MOTOR_REVERSE, MOTOR, PWM:
                mock_bus_address.write_byte(byte)

        board = Aflex2(mock_bus_address)

        # Act
        num = MOTOR
        pc = 20
        board.motor_reverse(num, pc)

        # Assert
        assert_that(mock_bus_address, verify())


# ABoardDigitalMode
class TestAflex2DigitalMode(TestCase):

    def test_mode_read(self):
        # Arrange
        PIN = 0x01
        MODE_DIGITAL_INPUT = 0x00

        with Mock(ABusAddress) as mock_bus_address:
            for byte in CMD_LEADER, CMD_MODE, PIN, MODE_DIGITAL_INPUT:
                mock_bus_address.write_byte(byte)

        board = Aflex2(mock_bus_address)

        # Act
        pin = PIN
        board.digital_mode_read(pin)

        # Assert
        assert_that(mock_bus_address, verify())

    def test_mode_write(self):
        # Arrange
        PIN = 0x01
        MODE_DIGITAL_OUTPUT = 0x01

        with Mock(ABusAddress) as mock_bus_address:
            for byte in CMD_LEADER, CMD_MODE, PIN, MODE_DIGITAL_OUTPUT:
                mock_bus_address.write_byte(byte)

        board = Aflex2(mock_bus_address)

        # Act
        pin = PIN
        board.digital_mode_write(pin)

        # Assert
        assert_that(mock_bus_address, verify())


# ABoardDigitalRead
class TestAflex2DigitalRead(TestCase):

    def test_run(self):
        # Arrange
        PIN = 0x01
        BYTE = 0x00

        with Mock(ABusAddress) as mock_bus_address:
            for byte in CMD_LEADER, CMD_DIGITAL_READ, PIN:
                mock_bus_address.write_byte(byte)

            mock_bus_address.read_byte().returns(BYTE)

        board = Aflex2(mock_bus_address)

        # Act
        pin = PIN
        ret = board.digital_read(pin)

        # Assert
        assert_that(ret,
                    equal_to(BYTE))
        assert_that(mock_bus_address, verify())


# ABoardDigitalWrite
class TestAflex2DigitalWrite(TestCase):

    def test_run(self):
        # Arrange
        PIN = 0x01
        BYTE = 0x00

        with Mock(ABusAddress) as mock_bus_address:
            for byte in CMD_LEADER, CMD_DIGITAL_WRITE, PIN, BYTE:
                mock_bus_address.write_byte(byte)

        board = Aflex2(mock_bus_address)

        # Act
        pin = PIN
        val = BYTE
        board.digital_write(pin, val)

        # Assert
        assert_that(mock_bus_address, verify())


# TODO: build abstractions for api
# TODO: pwm < 0 or > 250
# TODO: pc < 0 or > 100
# TODO: motor < 1 or > 2
# TODO: current < 10 or > 250
# TODO: pin < 1 or > 4
# TODO: current (see manual)

#   Motor Current
#   Syntax hexadecimal 0xFE 0x53 [current]
#   Parameter Length Description
#    [current] 2 bytes Set the current limit for the motors
#   Description: This command sets the current limit for the motors. The parameter [current]
#   defines the current limit. The parameter [current] is in range from 10 to 250.
#   The motor current limit = Imax * [current] / 250, where Imax is max motor driver current (for
#   the board “AFlex-2” – 2A; for the board “AFlex-3.5” – 3.5A.)
#   Example: To set a motor current limit to 1A for the board “Flex-2”:
#   1. Defind the [current] value: (1A / 2A) *250 = 125
#   2. Send a command: 0xFE 0x53 0x7D


if __name__ == '__main__':
    test_main()
