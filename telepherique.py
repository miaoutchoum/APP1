###  Importing packages  ###
import math
import numpy as np
import matplotlib.pyplot as plt



###  Data  ###
P1 = (-f/2, 0)
P2 = (f/2, 0)
d = 30
h1 = 2
h2 = 8
h = h2 - h1
L1 = math.sqrt((u + f/2)**2 + v**2)
L2 = (u - f/2)**2 + v**2



###  Physics code  ###
def speed(t: float) -> tuple:
    """
    :param t : time [s]
    :return speed vector:
    """
    # return (x, y)
    pass

def position(t: float) -> tuple:
    """
    :param t : time [s]
    :return position vector:
    """
    # return (x, y)
    pass



###  Graphics code  ###
def draw_position(t_i: float, t_f: float) -> None:
    """
    :param t_i : initial time [s]
    :param t_f : final time [s]
    :return None: 
    """
    pass