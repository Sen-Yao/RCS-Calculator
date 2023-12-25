import os
import argparse

from info_io import load_E_field, single_RCS_output, load_RCS, rcs_to_dB
from RCS_Table import RCS_Table


def main():
    """
    TODO: Add rad unit
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--unit', '-u', default='degree', type=str, help='angle unit')
    parser.add_argument('--path', default='data', type=str, help='path to data folder')
    parser.add_argument('--Ei', '-E', default=1, type=float, help='Mode of incident electric field vector')
    parser.add_argument('--R', '-R', default=1, type=float, help='Far field range')
    args = parser.parse_args()

    print('Parameter:',
          '\nAngle unit =', args.unit,
          '\nPath to data folder =', args.path,
          '\nMode of incident electric field vector =', args.Ei,
          '\nFar field range =', args.R,
          '\n\nResult:')

    RCS_Table_list = []
    for root, directories, files in os.walk(args.path):
        # Detect E_field txt
        for filename in files:
            if filename[0:2] == 'E_' and filename[-4:] == '.txt':
                Table = RCS_Table(args.R, args.Ei)
                Table.E_table, Table.sample_num, Table.frequency = load_E_field(os.path.join(args.path, filename))
                Table.frequency_str = filename[2:-4]
                Table.renew_frequency_str()

                Table.remove_redundancy_table()
                Table.calculate_single_direction_RCS()
                Table.calculate_total_RCS()

                RCS_Table_list.append(Table)

            elif filename[0:4] == 'RCS_' and filename[-4:] == '.txt':
                for Table in RCS_Table_list:
                    if Table.frequency_str == filename[4:-4]:
                        Table.CST_table = load_RCS(os.path.join(args.path, filename))
                        Table.check_single_RCS()

    RCS_Table_list.sort(key=lambda x: x.frequency)
    for Table in RCS_Table_list:
        print('When Frequency =', Table.frequency_str + 'Hz, the total RCS =', Table.total_RCS,
              'or', rcs_to_dB(Table.total_RCS), 'dB')





if __name__ == "__main__":
    main()
