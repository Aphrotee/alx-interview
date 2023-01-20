#!/usr/bin/python3

"""
Log Parsing

"""
import re
import sys
import random


fileSize = 0
i = 0


def print_log(fileSize, statusCodes, responses):
    """
    This function prints the log.
    """
    print('File size: {}'.format(fileSize))
    for code in statusCodes:
        if responses[code] > 0:
            print('{}: {}'.format(code, responses[code]))


def run():
    """
    Log parser
    """
    try:
        i = 0
        fileSize = 0
        responses = {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0
        }
        statusCodes = ['200', '301', '400', '401', '403', '404', '405', '500']
        for line in sys.stdin:
            neededString = re.search(r'[2-5]0[0-5] \d+', line)
            # ip = re.search(r'\d+.\d+.\d+.\d+', line)
            if neededString is None:
                continue
            neededString = neededString.group()
            values = neededString.split(' ')
            status = values[0]
            size = values[1]
            try:
                # status = int(status)
                size = int(size)
                # status = str(status)
                size = str(size)
            except Exception:
                continue
            if status in statusCodes:
                responses[status] += 1
            try:
                fileSize += int(size)
            except Exception:
                pass
            if i == 9:
                i = 0
                print_log(fileSize, statusCodes, responses)
                continue
            i += 1
        print_log(fileSize, statusCodes, responses)
    except KeyboardInterrupt as e:
        print_log(fileSize, statusCodes, responses)
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    run()
