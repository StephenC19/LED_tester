# -*- coding: utf-8 -*-

"""Console script for led_tester."""

import sys
sys.path.append('.')
import led_tester



def main(fileName):
    size, commands = led_tester.parseFile(fileName)
    
    leds = led_tester.LightTester(int(size))
    for i in commands:
        leds.apply(i)
    print(leds.count())


testData = '../test_files/input_assign3_d.txt'
main(testData)


#if __name__ == "__main__":
 #   import sys
#    sys.exit(main())
