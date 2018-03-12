# -*- coding: utf-8 -*-

"""Main module."""
import re

class LightTester:
    
    lights = None
    def __init__(self,N):
        self.lights = [[False]*N for _ in range(0,N)]

    def apply(self, cmd):
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
            coOrds = [x1, x2, y1, y2]
            for i in range(0,len(coOrds)):
                if coOrds[i] < 0:
                    coOrds[i] = 0
            
        
        
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
    
    
    
def parseFile(inputFile):
    
    file = open(inputFile, 'r')
    instructions = file.readlines()
    size = instructions[0]   
    del instructions[0]
    file.close()
    return size, instructions
