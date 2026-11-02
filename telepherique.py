import math
import numpy as np
import matplotlib.pyplot as plt

P1 = (-f/2, 0)
P2 = (f/2, 0)
d = 30
h1 = 2
h2 = 8
h = h2 - h1
L1 = "racine de : ", (u + f/2)**2 + v**2
L2 = (u - f/2)**2 + v**2


class Telepherique:
    def __init__(self, name):
        self.name = name
        self.P1 = P1
        self.P2 = P2
        self.d = d
        self.h1 = h1
        self.h2 = h2
        self.h = h
        self.L1 = L1
        self.L2 = L2

    def SetCoordinates_xy(self, x, y):
        self.u, self.v = u, v

    def GetCoordinates_xy(self, u, v, alpha):
        """x = (d/2) + ( u * math.cos(alpha) - v * math.sin(alpha) )
        y = (h1 + h/2) + ( u * math.sin(alpha) + v * math.cos(alpha) )
        return x, y"""
        x = (d / 2) + (self.u * d/f - self.v * h/f)
        y = (h1 + h / 2) + (self.u * h/f + self.v * d/f)
        return x, y

    def GetCoordinates_uv(self, x, y, alpha):
        u = None
        v = None

    def Ellipse_Coordinates(self, u):
        a = None
        b = None
