# -*- coding: utf-8 -*-

"""Main module"""

import sys
sys.path.append('.')
from led_tester import led_tester
import click


@click.command()
@click.option("--input", default=None, help="Input the url of instuction file (local or online)")

def main(input):
    size, commands = led_tester.parseFile(input)
    leds = led_tester.LightTester(int(size))
    for i in commands:
        leds.apply(i, size)
    on_count = leds.count()
    print("# occupied: ",on_count)
    return on_count



if __name__ == "__main__":
    sys.exit(main())