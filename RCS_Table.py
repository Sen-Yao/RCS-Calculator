import math


class RCS_Table:
    def __init__(self, R, Ei):
        self.E_table = {}
        self.RCS_table = {}
        self.total_RCS = None
        self.frequency = None
        self.sample_num = []

        self.R = R
        self.Ei = Ei

    def calculate_single_direction_RCS(self):
        for angles, E_values_list in self.E_table.items():
            E_phi, E_theta = self.E_table[angles]
            self.RCS_table[angles] = 4 * math.pi * (self.R ** 2) * ((abs(E_phi) ** 2 + abs(E_theta) ** 2) / abs(self.Ei) ** 2)

    def calculate_total_RCS(self):
        total_RCS_value = 0
        delta_phi = 360 / (self.sample_num[0] - 1)
        delta_theta = 180 / (self.sample_num[1] - 1)

        for angles, RCS_value in self.RCS_table.items( ):
            # Avoid calculate theta = 0/180 and phi = 0/360 twice
            if angles[0] == 360 or angles[1] == 180:
                continue
            area = math.radians(delta_theta) * math.radians(delta_phi) * math.sin(
                math.radians(angles[1] + delta_theta / 2))
            total_RCS_value += ((area * RCS_value) / (4 * math.pi))
        self.total_RCS = total_RCS_value
