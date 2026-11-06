###  Importing packages  ###
import math
import numpy as np
import matplotlib.pyplot as plt

###  Data  ###
L = 16
d = 15
h1 = 5
h2 = 4
f = (d**2 + (h2-h1)**2) ** 0.5



###  Physics code  ###
def position_equation(step: float=0.001) -> list:
    """
    :param step : step to draw the position equation
    :return the data of the car cable positions as a matrix:
    """
    a = L / 2
    b = (L**2 - f**2)**0.5 / 2

    u = np.linspace(-L/2, L/2, int(10/step))
    v = -b * np.sqrt(1 - (2*u/L) ** 2)

    return u, v

def velocity_equation(step: float=0.001) -> list:
    """
    :param step : step to draw the velocity equation
    :return speed vector:
    """
    # return the velocity equation
    pass

def acceleration_equation(step: float=0.001) -> list:
    """
    :param step : step to draw the acceleration equation
    :return speed vector:
    """
    # return the acceleration equation
    pass



###  Graphics code  ###
def draw_position(step: float=0.001, color='Black') -> None:
    """
    :param step : step to draw the position equation
    :param color : color of the position equation
    :return None:
    """
    # Time data
    u, v = position_equation(step=step)


    # Drawing position
    plt.plot(u, v, color=color)
    plt.xlabel("Length [m]")
    plt.ylabel("Heigh [m]")
    plt.title("Cable car")
    plt.grid(True)
    plt.axis("equal")
    plt.show()



# step = 0.01
# draw_position(step=step)