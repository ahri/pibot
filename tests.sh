#!/bin/bash

. bin/activate || . Scripts/activate
./bus/tests.py
./robotics/tests.py
