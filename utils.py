import math


def single_direction_RCS(R, E_theta, E_phi, E_i):
    return 4 * math.pi * (R ** 2) * ((abs(E_phi) ** 2 + abs(E_theta) ** 2) / abs(E_i) ** 2)


def total_RCS(RCS_table, total_phi_samples, total_theta_samples):
    total_RCS_value = 0
    delta_phi = 360 / (total_phi_samples-1)
    delta_theta = 180 / (total_theta_samples - 1)

    for angles, RCS_value in RCS_table.items():
        # Avoid calculate theta = 0/180 and phi = 0/360 twice
        if angles[0] == 360 or angles[1] == 180:
            continue
        area = math.radians(delta_theta) * math.radians(delta_phi) * math.sin(math.radians(angles[1] + delta_theta / 2))
        total_RCS_value += ((area * RCS_value) / (4 * math.pi))

    return total_RCS_value
