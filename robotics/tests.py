#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase, main as test_main
from doublex import Mock, verify
from hamcrest import assert_that, equal_to
from bus.api import ABus, ABusAddress
from concrete import BusAddressExecutor

# TODO: commands

class TestBusExecute(TestCase):

    def setUp(self):
        self.execution_leader = "exec"

    def test_execute(self):
        # Arrange
        COMMAND = "cmd"
        PARAMS = ("p1", "p2")
        with Mock(ABusAddress) as mock_bus_address:
            mock_bus_address.write_byte(self.execution_leader)
            mock_bus_address.write_byte(COMMAND)
            for param in PARAMS:
                mock_bus_address.write_byte(param)

        bus_address_executor = BusAddressExecutor(mock_bus_address, self.execution_leader)

        # Act
        bus_address_executor.execute(COMMAND, *PARAMS)

        # Assert
        assert_that(mock_bus_address, verify())

if __name__ == '__main__':
    test_main()
