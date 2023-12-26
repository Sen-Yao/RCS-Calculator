import math
import warnings

from info_io import rcs_to_dB


class RCS_Table:
    def __init__(self, R, Ei):
        self.E_table = {}
        self.RCS_table = {}
        self.CST_table = {}
        self.total_RCS = None
        self.frequency = None
        self.frequency_str = ''
        self.sample_num = []

        self.R = R
        self.Ei = Ei

    def calculate_single_direction_RCS(self):
        for angles, E_values_list in self.E_table.items( ):
            E_phi, E_theta = self.E_table[angles]
            self.RCS_table[angles] = (4 * math.pi * (self.R ** 2) *
                                      ((abs(E_phi) ** 2 + abs(E_theta) ** 2) / abs(self.Ei) ** 2))

    def calculate_total_RCS(self):
        total_RCS_value = 0
        delta_phi = 360 / (self.sample_num[0] - 1)
        delta_theta = 180 / (self.sample_num[1] - 1)

        for angles, RCS_value in self.RCS_table.items( ):
            # When theta = 0 or 180, area approx 0
            if angles[1] == 0 or angles[1] == 180:
                area = self.R ** 2 * math.radians(delta_theta / 2) * math.radians(delta_phi) * math.sin(
                    math.radians(delta_theta / 2)) / 2
            else:
                area = self.R ** 2 * ((math.radians(delta_theta) / 2) *
                                       (math.radians(delta_phi) * math.sin(math.radians(angles[1] - delta_theta / 2))
                                        + math.radians(delta_phi) * math.sin(
                                                   math.radians(angles[1] + delta_theta / 2))))
            total_RCS_value += ((area * RCS_value) / (4 * math.pi))
        self.total_RCS = total_RCS_value

    def check_single_RCS(self):
        for angles, result_RCS in self.RCS_table.items( ):
            if abs(self.CST_table[angles] - rcs_to_dB(result_RCS)) > 0.01:
                warnings.warn('Error! When θ=' + str(angles[1]) + ',φ=' + str(angles[0]) + ')=, result RCS=' +
                              str(rcs_to_dB(result_RCS)) + 'dB, but RCS from CST=' + str(self.CST_table[angles]))

    def remove_redundancy_table(self):
        angles_to_remove = []
        for angles, E in self.E_table.items( ):
            if angles[0] == 360:
                angles_to_remove.append(angles)
        for angles in angles_to_remove:
            self.E_table.pop(angles)

    def renew_frequency_str(self):
        if 1000 < self.frequency < 1000000:
            self.frequency_str = str(int(self.frequency / 1000)) + 'k'
        elif 1000000 < self.frequency < 1000000000:
            self.frequency_str = str(int(self.frequency / 1000000)) + 'M'
        else:
            self.frequency_str = str(int(self.frequency))
