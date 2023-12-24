import os
import argparse

from fileio import load_E_field
from utils import single_direction_RCS


def main():
    """
    TODO: Add rad unit
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--unit', '-u', default='degree', type=str, help='angle unit')
    parser.add_argument('--path', default='data', type=str, help='path to data folder')
    parser.add_argument('--Ei', '-E', default=1, type=float, help='Incidence electric field')
    parser.add_argument('--theta', '-t', default=0, type=float, help='Incidence theta angle')
    parser.add_argument('--phi', '-p', default=0, type=float, help='Incidence phi angle')
    parser.add_argument('--R', '-R', default=1, type=float, help='Incidence phi angle')
    args = parser.parse_args()

    E_field_table = load_E_field(os.path.join(args.path, 'E-field.txt'))

    RCS_table = {}
    for angles, E_field_list in E_field_table.items():
        RCS_table[angles] = single_direction_RCS(args.R, E_field_list[0], E_field_list[1], args.Ei)
    print(RCS_table)


if __name__ == "__main__":
    # 确保脚本在被导入时不会立即执行
    main()
