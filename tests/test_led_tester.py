#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_tester` package."""

#import pytest
import sys
sys.path.append(".")
#from click.testing import CliRunner

from led_tester import led_tester
from led_tester import cli




def test_inputs():
    led = cli.LightTester(10)
    assert led.count() == 0
    
"""    
def test_command_line_interface():
    Test the CLI.
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'led_tester.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
"""