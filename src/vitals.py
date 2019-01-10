#!/usr/bin/python3
import argparse
import os
import datetime
import re

if __name__ == '__main__':
    # Read and validate arguments
    parser = argparse.ArgumentParser(description='Log your vitals.')
    parser.add_argument('systolic', type=int, help='Your systolic blood pressure in mm Hg')
    parser.add_argument('diastolic', type=int, help='Your diastolic blood pressure in mm Hg')
    parser.add_argument('pulse', type=int, help='Your pulse in BPM')
    parser.add_argument('log_file', type=str, help='The path to the log file.')
    args = parser.parse_args()

    # Open file for appending
    log_file = open(args.log_file, 'a+')

    # Read the contents of the file
    log_file.seek(0, os.SEEK_SET)
    log_string = log_file.read()

    # Add csv header if necessary
    if not log_string:
        log_file.write('date,time,systolic,diastolic,pulse\n')

    # Get the date and time
    date = datetime.datetime.now()
    formated_date = date.strftime("%Y-%m-%d")
    formated_time = date.strftime("%H:%M:%S")

    # Append csv to file
    log_file.write(f'{formated_date},{formated_time},{args.systolic},{args.diastolic},{args.pulse}\n')

    # Close file
    log_file.close()
