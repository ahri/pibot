# coding: utf-8

from bus.api import ABus, ABusAddress, ABusAddressExecutor
from bus import BusAddress
from robotics import Aflex2


# Registrations
ABusAddress.register(BusAddress)


class VerboseProxy(object):

    """
    For debugging; print out and proxy calls.
    """

    def __init__(self, obj):
        self.obj = obj

    def __getattribute__(self, name):
        obj = object.__getattribute__('obj')
        attr = obj.__getattribute__(name)
        if not callable(attr):
            return attr

        def verbose_call(*params):
            print "Calling %s%s" % (name, params)
            return attr(*params)

        # monkey-patch
        attr = verbose_call
        return attr


def real_bus():
    import smbus
    first_bus = smbus.SMBus(0)
    ABus.register(smbus.SMBus)
    return first_bus

def fake_bus():
    from doublex import Stub, ANY_ARG
    with Stub(ABus) as stub_bus:
        stub_bus.read_byte(ANY_ARG).returns(0x01)

    return VerboseProxy(stub_bus)

ADDRESS = 0x4A  # sourced from `i2cdetect -y 0`

aflex2 = Aflex2(BusAddress(fake_bus(), ADDRESS))
