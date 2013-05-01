# coding: utf-8

from bus.api import ABus, ABusAddress
from bus import BusAddress
from robotics import Aflex2


def real_bus():
    import smbus
    first_bus = smbus.SMBus(0)
    ABus.register(smbus.SMBus)
    return first_bus


def fake_bus():
    from doublex import Stub, ANY_ARG

    with Stub(ABus) as stub_bus:
        stub_bus.read_byte(ANY_ARG).returns(0x01)

    return stub_bus


ADDRESS = 0x4A  # sourced from `i2cdetect -y 0`

aflex2 = Aflex2(BusAddress(fake_bus(), ADDRESS))
