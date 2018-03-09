# -*- coding: utf-8 -*-

"""Console script for led_tester."""

import sys
sys.path.append('.')
from led_tester import LightTester
from led_tester import cli



def main(args=None):
    """Console script for led_tester."""
    thing = LightTester(10)
    print(thing.count())

if __name__ == "__main__":
    import sys
    sys.exit(main())
