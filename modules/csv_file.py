import csv
import os


def get_csv_from_file(csv_file='', as_dict=True):
    """Gib CSV array zurück von Datei."""
    if not os.path.isfile(csv_file):
        print('{} ist keine Datei!'.format(csv_file))
        exit()

    out_dict = []
    with open(csv_file, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        out_list = []
        for row in spamreader:
            out_list.append(row)

        for row in out_list:
            tmp = {}
            for c, col in enumerate(row):
                if len(out_list[0]) > c:
                    tmp[out_list[0][c]] = col
            out_dict.append(tmp)

    if as_dict:
        return out_dict[1:]
    else:
        return out_list
