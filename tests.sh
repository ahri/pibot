#!/bin/bash

. bin/activate 2>/dev/null || . Scripts/activate 2>/dev/null || (
    . bin/activate
    . Scripts/activate
)

./bus/tests.py
./robotics/tests.py
