import os
import argparse

from info_io import load_E_field
from utils import single_direction_RCS, total_RCS


def main():
    """
    TODO: Add rad unit
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--unit', '-u', default='degree', type=str, help='angle unit')
    parser.add_argument('--path', default='data', type=str, help='path to data folder')
    parser.add_argument('--Ei', '-E', default=1, type=float, help='Mode of incident electric field')
    parser.add_argument('--theta', '-t', default=0, type=float, help='Incidence theta angle')
    parser.add_argument('--phi', '-p', default=0, type=float, help='Incidence phi angle')
    parser.add_argument('--R', '-R', default=1, type=float, help='Incidence phi angle')
    args = parser.parse_args()

    for root, directories, files in os.walk(args.path):
        # Detect E_field txt
        for filename in files:
            if filename[0:2] == 'E_' and filename[-4:] == '.txt':
                E_field_table, sample_num, frequency = load_E_field(os.path.join(args.path, filename))


    RCS_table = {}
    for angles, E_field_list in E_field_table.items():
        RCS_table[angles] = single_direction_RCS(args.R, E_field_list[0], E_field_list[1], args.Ei)
    total_RCS_value = total_RCS(RCS_table, sample_num[0], sample_num[1])
    print('When Incidence theta angle Θ=', args.theta)


if __name__ == "__main__":
    main()
