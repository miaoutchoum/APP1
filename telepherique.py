###  Importing packages  ###
import math
import numpy as np
import matplotlib.pyplot as plt



###  Data  ###
L = 16                             # [m]
d = 15                             # [m]
h1 = 5                             # [m]
h2 = 4                             # [m]
f = (d**2 + (h2-h1)**2) ** 0.5     # []

# Ellipse
a = L / 2                          # []
b = (L**2 - f**2)**0.5 / 2         # []

# Other
g = 9.81                           # [m/s²]
m = 0.4                            # [kg]



###  Physics code  ###
def trajectory_equation(interval: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    :param interval : step to draw the trajectory equation
    :return the data of the car cable trajectories as an array:
    """

    u = interval

    # Multiply every u-axis to get the correspondant value on the v-axis
    #        np.sqrt applies √ for every value at the SAME time
    v = -b * np.sqrt(1 - (2*u/L) ** 2)

    return v

def velocity_equation(interval: np.ndarray) -> list:
    """
    :param interval : step to draw the velocity equation
    :return speed vector:
    """
    # return dv
    pass

def acceleration_equation(interval: np.ndarray) -> list:
    """
    :param interval : step to draw the acceleration equation
    :return speed vector:
    """
    # return the acceleration equation
    pass



###  Graphics code  ###
def draw_trajectory(interval: np.ndarray, color='Black') -> None:
    """
    :param interval : step to draw the trajectory equation
    :param color : color of the trajectory equation
    :return None:
    """

    # Data
    u = interval
    v = trajectory_equation(interval=u)


    # Drawing trajectory
    plt.plot(interval, v, color=color, label="Trajectory")
    plt.xlabel("Length [m]")
    plt.ylabel("Heigh [m]")
    plt.title("Cable car")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()
    plt.show()

def draw_velocity(interval: np.ndarray, color='Black') -> None:
    """
    :param interval : step to draw the velocity equation
    :param color : color of the velocity equation
    :return None:
    """

    # Data
    u = interval
    dv = velocity_equation(interval=u)


    # Drawing Velocity
    plt.plot(u, dv, color=color, label="Velocity")
    plt.xlabel("t [s]")
    plt.ylabel("speed [m/s]")
    plt.title("Cable car")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()
    plt.show()



step = 0.01

# Create an array of every values on the u-axis
#                                  + step is use to include the last value
divided_interval = np.arange(-a, a + step, step)

draw_trajectory(interval=divided_interval, color='Blue')