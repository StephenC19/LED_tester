#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_tester` package."""

import sys
sys.path.append(".")
#from click.testing import CliRunner

from led_tester import led_tester
from led_tester import cli




def test_inputs():
    led = led_tester.LightTester(10)
    assert led.count() == 0