#!/usr/bin/python3
import argparse
import os
import datetime
import re

def to_csv_format(*values):
    """
    Generates a CSV string based on the values.
    """
    return ','.join(map(str, values))

def is_proper_csv(csv_string, cols=None):
    """
    Determines if a string is proper CSV.

    Proper csv in this case just means that there is the same number of entries (separated by commas) per line.
    """
    rows = csv_string.strip().split('\n')
    parsed = list(set([ row.count(',') for row in rows ]))

    if not csv_string:
        return True

    if cols is None:
        return len(parsed) == 1
    else:
        return len(parsed) == 1 and parsed[0] == (cols - 1)

def log_vitals(log_filename, systolic, diastolic, pulse, date):
    # Open file for appending
    log_file = open(log_filename, 'a+')

    # Read the contents of the file
    log_file.seek(0, os.SEEK_SET)
    log_string = log_file.read()

    # Display an error if the CSV is not proper
    if not is_proper_csv(log_string, 5):
        print("The log file is malformed.")
        log_file.close()
        return -1

    # Add csv header if necessary
    if not log_string:
        log_file.write(to_csv_format('date', 'time', 'systolic', 'diastolic', 'pulse') + '\n')

    # Get the date and time
    formated_date = date.strftime("%Y-%m-%d")
    formated_time = date.strftime("%H:%M:%S")

    # Append csv to file
    log_file.write(to_csv_format(formated_date, formated_time, systolic, diastolic, pulse) + '\n')

    # Close file
    log_file.close()

    return 0

if __name__ == '__main__':
    # Read and validate arguments
    parser = argparse.ArgumentParser(description='Log your vitals.')
    parser.add_argument('systolic', type=int, help='Your systolic blood pressure in mm Hg')
    parser.add_argument('diastolic', type=int, help='Your diastolic blood pressure in mm Hg')
    parser.add_argument('pulse', type=int, help='Your pulse in BPM')
    parser.add_argument('log_file', type=str, help='The path to the log file.')
    args = parser.parse_args()

    log_vitals(args.log_file, args.systolic, args.diastolic, args.pulse, datetime.datetime.now())
