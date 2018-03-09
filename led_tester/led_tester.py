# -*- coding: utf-8 -*-

"""Main module."""

class LightTester:
    
    lights = None
    def __init__(self,N):
        self.lights = [[False]*N for _ in range(0,N)]
        
    
    def count(self):
        count = 0
        return count