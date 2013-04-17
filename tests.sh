#!/bin/bash

. bin/activate 2>/dev/null || . Scripts/activate 2>/dev/null || (
    . bin/activate
    . Scripts/activate
)

find bus robotics -name '*.py' -exec grep TODO {} \;

./bus/tests.py
./robotics/tests.py
