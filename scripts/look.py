#!/home/b426/miniconda3/envs/mpc/bin/python

import dask.dataframe as dd
import argparse

def summary(file_name, is_csv):
    df = dd.read_hdf(file_name, key='data') if not is_csv else dd.read_csv(file_name)
    print(f"===== Info of {file_name} =====")
    df.info(verbose=True)
    print(f"\n\n===== Describe of {file_name} =====")
    print(df.describe().compute())


def peek(file_name, lines, is_csv):
    df = dd.read_hdf(file_name, key='data') if not is_csv else dd.read_csv(file_name)
    print(f"===== Top {lines} lines of {file_name} =====")
    print(df.head(lines))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Look at a data file')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the file')
    parser.add_argument('-l', '--line', type=int, default=0, help='Lines to peek')
    parser.add_argument('--csv', action='store_true', default=False, help="Pure CSV mode.")
    args = parser.parse_args()
    
    if args.line <= 0:
        summary(args.file, args.csv)
    else:
        peek(args.file, args.line, args.csv)
