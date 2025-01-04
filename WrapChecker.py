#!/usr/bin/env python3

"""
Wrap Checker will check the length of each line in a document to ensure it does
not exceed a specified length
"""

import argparse


PROG_NAME = 'WrapChecker'
PROG_DESC = 'Checks the length of each line in a document to ensure it is wrapped'
PROG_VERSION='1.0'

DEFAULT_CONFIG = {
    'length': 90,
    'encoding': 'utf-8',
    'tab-size': 4
}


def parse_args():
    '''
    Parses the command line arguments
    '''
    parser = argparse.ArgumentParser(
               prog=PROG_NAME,
               description=PROG_DESC)
    parser.add_argument('filename')
    parser.add_argument('-l', '--length', type=int, default=DEFAULT_CONFIG['length'], help='Length limit of line (default: {0})'.format(DEFAULT_CONFIG['length']))
    parser.add_argument('-e', '--encoding', type=str, default=DEFAULT_CONFIG['encoding'], help='File encoding to use (default: {0})'.format(DEFAULT_CONFIG['encoding']))
    parser.add_argument('-t', '--tab-size', type=int, default=DEFAULT_CONFIG['tab-size'], help='Size of tab characters (default: {0})'.format(DEFAULT_CONFIG['tab-size']))
    parser.add_argument('-v', '--version', action='version', version='{0} v{1}'.format(PROG_NAME, PROG_VERSION))
    return parser.parse_args()


def check_document(filename: str, limit: int, encoding: str, tab_size: int):
    '''
    Checks a file document's line lengths and reports any that are too long
    '''
    tab_replacement = ' ' * tab_size
    with open(filename, 'r', encoding=encoding) as file:
        num_of_fails = 0
        row = 0
        for line in file:
            row += 1
            line = line.replace('\n', '')   # Strip the newline from the count
            line = line.replace('\t', tab_replacement)
            length = len(line)    # Strip the newline from the count
            if length > limit:
                num_of_fails += 1
                report_failed_line(row, length, limit, line)

        if num_of_fails > 0:
            print('Total fails: {0}'.format(num_of_fails))
        print('Total lines: {0}'.format(row))


def report_failed_line(row: int, length: int, limit: int, line: str):
    '''
    Formats an error message for a line that is too long
    '''
    print('[ line:{0}, length:{1} ] {2}'.format(row, length, line[0:limit]))


def main():
    '''
    Main routine
    '''
    args = parse_args()
    print('Line length limit: {0}'.format(args.length))
    check_document(args.filename, args.length, args.encoding, args.tab_size)


if __name__ == '__main__':
    main()
