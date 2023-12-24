import math


def single_direction_RCS(R, E_theta, E_phi, E_i):
    return 4 * math.pi * (R**2) * ((abs(E_phi)**2+abs(E_theta)**2) / abs(E_i)**2)
