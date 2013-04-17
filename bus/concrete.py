# coding: utf-8

from api import *


class BusAddress(object):

    def __init__(self, bus, address):
        self.bus = bus
        self.address = address

    def read_byte(self):
        return self.bus.read_byte(self.address)

    def write_byte(self, byte):
        self.bus.write_byte(self.address, byte)


ABusAddress.register(BusAddress)
