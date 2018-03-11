#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_tester` package."""

import sys
sys.path.append(".")

from led_tester import led_tester
from led_tester import cli
    
    
def test_file():
    fileName = './test_files/input_assign3_d.txt'
    file = open(fileName, 'r')
    assert file is not None
    
def test_count():
    led = led_tester.LightTester(10)
    led.apply(0,10,0,10)
    assert led.count() == 100