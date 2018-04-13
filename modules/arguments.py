import argparse


def getArguments():
    """Return argparse object."""

    ARGS = argparse.ArgumentParser(
        description=(
            'Vergleicht zwei CSV Dateien miteinander und gibt Unterschiede zurück.'
        )
    )

    ARGS.add_argument(
        'csvfiles',
        nargs=2,
        default=None,
        help=(
            'CSV1 CSV2: vergleicht diese CSV und gibt Unterschiede mit '
            'Spalte+Zeile zurück.'
        )
    )

    return ARGS.parse_args()
