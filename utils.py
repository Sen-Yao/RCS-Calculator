import math


def single_direction_RCS(R, E_theta, E_phi, E_i):
    return 4 * math.pi * (R**2) * ((abs(E_phi)+abs(E_theta)) / abs(E_i))
