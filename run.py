from modules import arguments
from modules import compare_csv

ARGS = arguments.getArguments()

if __name__ == '__main__':
    compare_csv.compareCSV(
        ARGS.csvfiles[0],
        ARGS.csvfiles[1]
    )
