from modules import csv_file


def compareCSV(csv1, csv2):
    csv_a_header = csv_file.get_csv_from_file(csv1, False)[0]
    # csv_a = csv_file.get_csv_from_file(csv1)

    csv_b_header = csv_file.get_csv_from_file(csv2, False)[0]
    # csv_b = csv_file.get_csv_from_file(csv2)

    if not compareHeader(csv_a_header, csv_b_header):
        print('Cannot continue, due to different columns count.')
        print()
        exit()


def compareHeader(csv1, csv2):
    print('Compare HEADERS:')

    if len(csv1) != len(csv2):
        print('   DIFF: CSV1 length != CSV2 length')
        print()
        return False

    for c, col in enumerate(csv1):
        if col != csv2[c]:
            print('   DIFF: Col {}'.format(c))
            print('       : CSV1 = {}, CSV2 = {}'.format(col, csv2[c]))

    print('   No more differences.')
    print()
    return True
