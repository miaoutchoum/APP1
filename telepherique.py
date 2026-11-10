"""
GitHub repository link : https://github.com/miaoutchoum/APP1
"""

###  Importing packages  ###
import math
import numpy as np
import matplotlib.pyplot as plt



###  Data  ###
# Installation
L = 16                             # cable length [m]
d = 15                             # [m]
h1 = 5                             # [m]
h2 = 4                             # [m]
h = h2 - h1                        # [m]
f = (d**2 + h**2) ** 0.5           # [-]
alpha = math.atan2(h, d)           # tan(𝜶) = h/d [rad]

# Ellipse
a = L / 2                          # semi-major axis [-]
b = (L**2 - f**2)**0.5 / 2         # semi-minor axis [-]

# Other
g = 9.81                           # gravity [m/s²]
m = 0.4                            # mass of the cable car [kg]
f_d = 0.1                          # friction coefficient [kg/s]

# Simulation
step = 0.001                       # time step dt [s]
end = 60.0                         # duration [s]
x_0 = 0.0                          # initial horizontal position [m]
du_0 = 0.0                         # initial speed [m/s]


###  Physics code  ###
def trajectory_equation(interval: np.ndarray) -> np.ndarray:
    """
    :param interval : values on the u-axis [m]
    :return v : corresponding values on the v-axis, lower branch of the ellipse [m]
    """

    u = interval

    # Applied to every value of u at the SAME time (NumPy vectorisation)
    v = -b * np.sqrt(1 - (u / a) ** 2)

    return v

def slope_equation(interval: np.ndarray) -> np.ndarray:
    """
    :param interval : values on the u-axis [m]
    :return v' = dv/du : slope of the trajectory in the (u, v) frame [-]
    """

    u = interval

    return b / a**2 * u / np.sqrt(1 - (u / a) ** 2)

def curvature_equation(interval: np.ndarray) -> np.ndarray:
    """
    :param interval : values on the u-axis [m]
    :return v'' = d²v/du² : second derivative of the trajectory [1/m]
    """

    u = interval

    return b / a**2 * (1 - (u / a) ** 2) ** (-3 / 2)

def acceleration_equation(u: float, du: float) -> float:
    """
    :param u  : position on the u-axis [m]
    :param du : speed along u, du/dt [m/s]
    :return ddu : acceleration along u, d²u/dt² [m/s²] (final equation of Annex H2)
    """

    dv = slope_equation(u)          # v'
    ddv = curvature_equation(u)     # v''
    
    # ů = du
    
    courbure =  ((dv * ddv) / (1 + dv**2)) * (du**2)
    frotement_force = (f * du) / m
    gravity_force = ((dv * math.cos(alpha) + math.sin(alpha)) / (1 + (dv**2))) * g
    
    return (-1) * (courbure + frotement_force + gravity_force)

def velocity_equation(u: np.ndarray, du: np.ndarray) -> np.ndarray:
    """
    :param u  : positions on the u-axis [m]
    :param du : speeds along u [m/s]
    :return ds : speed of the cable car along the cable, ||dR/dt|| = sqrt(1 + v'²) |du/dt| [m/s]
    """
    dv = slope_equation(u)
    
    return np.sqrt((1 + dv**2))*abs(du)

def change_of_reference(u: np.ndarray, v: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    :param u, v : coordinates in the ellipse frame [m]
    :return x, y : coordinates in the real frame (origin at the foot of P1) [m]
    """

    x = d / 2 + u * math.cos(alpha) - v * math.sin(alpha)
    y = h1 + h / 2 + u * math.sin(alpha) + v * math.cos(alpha)

    return x, y

def u_from_x(x_target: float) -> float:
    """
    :param x_target : horizontal position in the real frame [m]
    :return u : position on the u-axis of the point of the path with this x [m]
    """

    u_grid = np.linspace(-a, a, 200001)
    x_grid, _ = change_of_reference(u_grid, trajectory_equation(u_grid))

    return float(np.interp(x_target, x_grid, u_grid))


u_min = u_from_x(0)
u_max = u_from_x(d)
u_0 = u_from_x(x_0)


def simulation() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Solve the equation of motion with Euler's method.

    :return t, u, du, ddu : time [s], position [m], speed [m/s] and acceleration [m/s²] along u
    """

    t = np.arange(0, end, step)

    u = np.empty_like(t)
    du = np.empty_like(t)
    ddu = np.empty_like(t)

    u[0], du[0] = u_0, du_0

    n = len(t)
    for i in range(0, len(t) - 1):
        dt = step
        ddu[i] = acceleration_equation(u[i], du[i])
        du[i+1] = du[i] + ddu[i] * dt
        u[i+1] = u[i] + du[i] * dt
        ddu[i+1] = ddu[i]

        # Stop the simulation
        if not (u_min <= u[i] <= u_max):
            n = i + 1
            break

    return t[:n], u[:n], du[:n], ddu[:n]



###  Graphics code  ###
def draw_trajectory(x: np.ndarray, y: np.ndarray, color='Black') -> None:
    """
    :param x, y : simulated positions [m]
    :param color : color of the simulated positions
    :return None:
    """

    # Full path of the cable car, between the poles
    u_path = np.linspace(u_min, u_max, 2001)
    x_path, y_path = change_of_reference(u_path, trajectory_equation(u_path))

    plt.figure(1)
    plt.plot(x_path, y_path, '--', color='Grey', label="Possible path (ellipse)")
    plt.plot(x, y, color=color, label="Simulated positions")
    plt.plot([0, d], [h1, h2], 'ko', label="Anchors P1, P2")
    plt.plot(x[-1], y[-1], 'o', color='Red', label=f"Final position ({x[-1]:.3f}, {y[-1]:.3f})")
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.title("Cable car - trajectory")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()
    plt.show()

def draw_position_velocity(t: np.ndarray, x: np.ndarray, y: np.ndarray, speed: np.ndarray, color='Black') -> None:
    """
    :param t : time [s]
    :param x, y : positions [m]
    :param speed : speed along the cable [m/s]
    :param color : color of the simulated curves
    :return None:
    """

    pass

def draw_energy(t: np.ndarray, y: np.ndarray, speed: np.ndarray) -> None:
    """
    Check of the simulation: the total energy must decrease (friction)
    and stay constant if f_d = 0.
    :return None:
    """

    pass




###  Main program  ###
if __name__ == "__main__":

    # 1. Solve the equation of motion along u
    t, u, du, ddu = simulation()

    # 2. Back to the real frame and speed along the cable
    v = trajectory_equation(u)
    x, y = change_of_reference(u, v)
    speed = velocity_equation(u, du)

    # 3. Graphics
    draw_trajectory(x, y, color='Blue')
    draw_position_velocity(t, x, y, speed, color='Black')
