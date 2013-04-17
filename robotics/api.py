# coding: utf-8
from abc import ABCMeta, abstractmethod


class ABoardFirmwareVersion(object):

    """
    For boards that provide their firmware version.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def firmware_version(self):
        "Get the firmware version for the board."


class ABoardMicroswitchRead(object):

    """
    For boards that provide microswitches.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def microswitch_read(self, num):
        "Read from the specified microswitch."


class ABoardMicroswitch4bitRead(object):

    """
    Convenience around microswitches.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def microswitch_4bit_read(self, num):
        "Read 4 bits from the specified microswitch."


class ABoardMotorCurrent(object):

    """
    Set the (global) current for a board.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def motor_current(self, mA):
        "Set the motor driver to a specific mA value."


class ABoardMotor(object):

    """
    Generic motor controls.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def motor_stop(self, num):
        "Stop the given motor."

    @abstractmethod
    def motor_forward(self, num, pc):
        "Set the forward speed as a percentage of the maximum."

    @abstractmethod
    def motor_reverse(self, num, pc):
        "Set the reverse speed as a percentage of the maximum."


class ABoardMotorPwm(object):

    """
    Motor controls as a function of PWM.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def motor_forward_pwm(self, num, val):
        "Set the motor function as pwm."

    @abstractmethod
    def motor_reverse_pwm(self, num, val):
        "Set the motor function as pwm, in reverse."


class ABoardDigitalMode(object):

    """
    Set digital read/write modes.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def digital_mode_read(self, pin):
        "Set a pin to digital mode read."

    @abstractmethod
    def digital_mode_write(self, pin):
        "Set a pin to digital mode write."


class ABoardDigitalRead(object):

    """
    Read bytes.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def digital_read(self, pin):
        "Read a byte from the given pin."


class ABoardDigitalWrite(object):

    """
    Write bytes.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def digital_write(self, pin, val):
        "Write a byte to a given pin."
