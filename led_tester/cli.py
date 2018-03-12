# -*- coding: utf-8 -*-

"""Console script for led_tester."""

import sys
sys.path.append('.')
from led_tester import led_tester
import click


@click.command()
@click.option("--input", default=None, help="input the url of instuction file (local or online)")

def main(input):
    size, commands = led_tester.parseFile(input)
    leds = led_tester.LightTester(int(size))
    for i in commands:
        leds.apply(i, size)
    print("Leds turned on: ",leds.count())



if __name__ == "__main__":
    sys.exit(main())
