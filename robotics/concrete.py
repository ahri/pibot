# coding: utf-8


class BusAddressExecutor(object):

    def __init__(self, bus_address, execution_leader):
        self.bus_address = bus_address
        self.execution_leader = execution_leader

    def execute(self, command, *params):
        self.bus_address.write_byte(self.execution_leader)
        self.bus_address.write_byte(command)
        for param in params:
            self.bus_address.write_byte(param)
