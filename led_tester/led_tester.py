# -*- coding: utf-8 -*-

"""
LightTester Object
------------------
Defines the LED board object with functions to turn on/off
ranges of LEDs and count the amount left on. 

Also defines a function to parse the input file to separate
the appropriate instructions for controlling the LED board.
"""

import re
import requests

class LightTester:
    
    lights = None
    def __init__(self,N):
        self.lights = [[False]*N for _ in range(0,N)]

    "Function to control the LEDs on the board"
    def apply(self, cmd, N):
        pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        res = re.findall(pat, cmd)

        if len(res) != 0:
            x1,x2 = int(res[0][1]), int(res[0][3])
            y1,y2 = int(res[0][2]), int(res[0][4])
            op = res[0][0]
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
           
            "Deals with out of range co-ordinates"
            if x1 < 0:
                x1 = 0
            elif x1 > int(N):
                x1 = int(N)
            if x2 < 0:
                x2 = 0
            elif x2 > int(N):
                x2 = int(N)
            if y1 < 0:
                y1 = 0
            elif y1 > int(N):
                y1 = int(N)
            if y2 < 0:
                y2 = 0
            elif y2 > int(N):
                y2 = int(N)
        
        
            if res[0][0] == "turn on":
                for i in range(y1,y2):
                    for j in range(x1, x2):
                        self.lights[i][j] = True
                    
            elif res[0][0] == "turn off":
                for i in range(y1,y2):
                    for j in range(x1, x2):
                        self.lights[i][j] = False

            elif res[0][0] == "switch":
                for i in range(y1,y2):
                    for j in range(x1, x2):
                        if self.lights[i][j] == True:
                            self.lights[i][j] = False
                        else:
                            self.lights[i][j] = True

    def count(self):
        count = 0
        for i in range(len(self.lights)):
            for j in range(len(self.lights)):
                if self.lights[i][j] == True:
                    count +=1
        return count
    
    
    
"Function to separate correct arguments from an input file"
def parseFile(inputFile):
    
    if inputFile.startswith('http'):
        r = requests.get(inputFile).text
        lines = r.splitlines()
        size = lines[0]
        instructions = lines[1:]
    else:
        file = open(inputFile, 'r')
        instructions = file.readlines()
        size = instructions[0]   
        del instructions[0]
        file.close()
    
    return size, instructions
