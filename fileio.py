def load_E_field(path):
    E_field_table = {}
    try:
        with open(path, 'r') as file:
            line = file.readline()

            # Find the start of valid information
            while line != '// >> Phi, Theta, Re(E_Theta), Im(E_Theta), Re(E_Phi), Im(E_Phi): \n':
                line = file.readline()

            # Store the E-field data
            while line:
                line = file.readline()
                phi = float(line[:8])
                theta = float(line[9:18])
                E_theta_Re = float(line[19:35])
                E_theta_Im = float(line[36:52])
                E_phi_Re = float(line[53:68])
                E_phi_Im = float(line[69:])

                angle = (phi, theta)
                E_field = [E_theta_Re, E_theta_Im, E_phi_Re, E_phi_Im]
                E_field_table[angle] = E_field
        return E_field_table
    except FileNotFoundError:
        print('E-field information not found!')