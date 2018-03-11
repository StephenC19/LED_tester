# -*- coding: utf-8 -*-

"""Main module."""

class LightTester:
    
    lights = None
    def __init__(self,N):
        self.lights = [[False]*N for _ in range(0,N)]
        
    def apply(self, x1, x2, y1,y2):
        for i in range(y1,y2):
            for j in range(x1, x2):
                self.lights[i][j] = True
                
    def count(self):
        count = 0
        for i in range(len(self.lights)):
            for j in range(len(self.lights)):
                if self.lights[i][j] == True:
                    count +=1
        return count