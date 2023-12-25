import math


def rcs_to_dB(rcs_m2, reference_value=1.0):
    return 10 * math.log10(rcs_m2 / reference_value)


def load_E_field(path):
    E_field_table = {}
    try:
        with open(path, 'r') as file:
            line = file.readline()

            # Get numbers of example frequencies
            while line != '// #Frequencies\n':
                line = file.readline()
            line = file.readline()
            total_frequencies_sample = int(line)

            # Get frequencies value
            while line != '// Radiated/Accepted/Stimulated Power , Frequency \n':
                line = file.readline()
            # Skip the next three lines
            for _ in range(3):
                next(file)
            line = file.readline()
            frequency = float(line)

            # Get total samples information
            while line != '// >> Total #phi samples, total #theta samples\n':
                line = file.readline()
            line = file.readline()
            total_samples = line.split()
            total_phi_samples = float(total_samples[0])
            total_theta_samples = float(total_samples[1])

            # Get valid E-field information
            while line != '// >> Phi, Theta, Re(E_Theta), Im(E_Theta), Re(E_Phi), Im(E_Phi): \n':
                line = file.readline()
            line = file.readline()
            # Store the E-field data
            while line:
                phi = float(line[:8])
                theta = float(line[9:18])
                E_theta_Re = float(line[19:35])
                E_theta_Im = float(line[36:52])
                E_phi_Re = float(line[53:68])
                E_phi_Im = float(line[69:])

                E_theta = complex(E_theta_Re, E_theta_Im)
                E_phi = complex(E_phi_Re, E_phi_Im)
                angle = (phi, theta)
                E_field = [E_theta, E_phi]
                E_field_table[angle] = E_field
                line = file.readline()

        sample_num = [total_phi_samples, total_theta_samples, total_frequencies_sample]
        return E_field_table, sample_num, frequency
    except FileNotFoundError:
        print('E-field information not found!')


def load_RCS(path):
    RCS_table = {}
    try:
        with open(path, 'r') as file:
            line = file.readline()
            while line != ('Theta [deg.]  Phi   [deg.]  Abs(RCS )[dB(m^2)]   Abs(Theta)[dB(m^2)]  Phase(Theta)[deg.]  '
                           'Abs(Phi  )[dB(m^2)]  Phase(Phi  )[deg.]  Ax.Ratio[dB    ]    \n'):
                line = file.readline()
            line = file.readline()
            line = file.readline()
            # Store the RCS data
            while line:
                theta = float(line[:8])
                phi = float(line[9:25])
                RCS_value = float(line[26:46])

                angle = (phi, theta)
                RCS_table[angle] = RCS_value
                line = file.readline()
        return RCS_table

    except FileNotFoundError:
        print('RCS information not found!')


def single_RCS_output(RCS_table, use_dB=False):
    for angles, RCS_value in RCS_table.items():
        if use_dB:
            print('RCS: σ( θ=', angles[1], ',φ=', angles[0], ')=', rcs_to_dB(RCS_value))
        else:
            print('RCS: σ( θ=', angles[1], ',φ=', angles[0], ')=', RCS_value)
