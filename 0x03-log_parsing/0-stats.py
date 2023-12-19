#!/usr/bin/python3
'''A script for parsing HTTP request logs and computing metrics.
'''
import sys


def extract_input(line):
    '''Extracts information from a line of an HTTP request log.

    Args:
        line (str): The input line to extract information from.

    Returns:
        tuple: A tuple containing IP address, date, status code, and file size.
    '''
    try:
        _, _, _, _, _, _, _, _, _, ip, _, date, request, status_code, file_size = line.strip().split(' ', 13)
        return ip, date, request, status_code, int(file_size)
    except ValueError:
        return None


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.

    Args:
        total_file_size (int): The total file size.
        status_codes_stats (dict): A dictionary containing status codes and their counts.
    '''
    print(f'File size: {total_file_size}')
    for code in sorted(status_codes_stats):
        count = status_codes_stats[code]
        if count > 0:
            print(f'{code}: {count}')


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.
        total_file_size (int): The current total file size.
        status_codes_stats (dict): A dictionary containing status codes and their counts.

    Returns:
        int: The new total file size.
    '''
    log_info = extract_input(line)
    if log_info:
        _, _, _, status_code, file_size = log_info
        status_codes_stats[status_code] += 1
        return total_file_size + file_size
    return total_file_size


def run():
    '''Starts the log parser.
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        for line in sys.stdin:
            total_file_size = update_metrics(line, total_file_size, status_codes_stats)
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)

if __name__ == '__main__':
    run()
