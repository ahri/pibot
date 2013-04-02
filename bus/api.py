# coding: utf-8
from abc import ABCMeta, abstractmethod


class ABus(object):

    """
    Perform operations on a defined bus.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def read_byte(self, address):
        "Read a byte from the given address."

    @abstractmethod
    def write_byte(self, address, byte):
        "Write a byte to the given address."


class ABusAddress(object):

    """
    Perform operations on a defined bus address.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def read_byte(self):
        "Read a single byte."

    @abstractmethod
    def write_byte(self, byte):
        "Write a single byte."


class ABusAddressExecutor(object):

    """
    Execute single-byte commands, supplying multiple parameters.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self, command, *params):
        "Execute a command with zero or more parameters."
