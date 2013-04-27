#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase, main as test_main
from doublex import Mock, verify
from hamcrest import assert_that, equal_to
from bus.api import ABus, ABusAddress
from bus import BusAddress


class TestBusAddress(TestCase):

    def setUp(self):
        self.address = 0x00

    def test_read_byte(self):
        # Arrange
        BYTE_TO_READ = 0x00
        with Mock(ABus) as mock_bus:
            mock_bus.read_byte(self.address).returns(BYTE_TO_READ)

        # Act
        bus_address = BusAddress(mock_bus, self.address)

        # Assert
        assert_that(bus_address.read_byte(),
                    equal_to(BYTE_TO_READ))

        assert_that(mock_bus, verify())

    def test_write_byte(self):
        # Arrange
        BYTE_TO_WRITE = 0x00
        with Mock(ABus) as mock_bus:
            mock_bus.write_byte(self.address, BYTE_TO_WRITE)

        bus_address = BusAddress(mock_bus, self.address)

        # Act
        bus_address.write_byte(BYTE_TO_WRITE)

        # Assert
        assert_that(mock_bus, verify())


if __name__ == '__main__':
    test_main()
