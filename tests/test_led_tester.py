#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_tester` package."""

import sys
sys.path.append(".")

from led_tester import led_tester
from led_tester import cli
    
    
def test_file():
    fileName = './test_files/input_assign3_d.txt'
    size, commands = led_tester.parseFile(fileName)
    assert size is not None and commands is not None
    
def test_count():
    grid = 10
    led = led_tester.LightTester(grid)
    led.apply('turn on 0,0 through 10,10', grid)
    assert led.count() == 100
    
def test_main():
    fileName = './test_files/input_assign3_d.txt'
    result = cli.main(fileName)
    assert result == 349519

def test_outside_grid():
    grid = 10
    led = led_tester.LightTester(grid)
    led.apply('turn on 0,0 through 100,12', grid)
    assert led.count() == 100
    