"""
Author: Jeremy Cornett
Date: 11/4/2019
Purpose: Show a basic logging example that uses a file directly from a function.
"""

import datetime
import os
import time


def log_file(message, path_file=None):
    """Save the message to a file.
    :param message: The message to save to the file.
    :type message: str
    :param path_file: The path to the log file.
    :type path_file: str
    :return: None
    """
    if not path_file:
        # The default path for a log file.
        path_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "log_file.log")

    # With is used to open and close the file automatically instead of doing the open and close manually.
    # This also performs better if an exception is thrown during the call to the write function.
    # PROBLEM #1: One things this doesn't address is multiprocessing. If this function is called simultaneously,
    # you could have a lock issue with the file.
    # PROBLEM #2: The other concern is there's no rotating of log files. What happens when this file gets really big?
    # Hypothetically, if a program continually calls this log function, it could fill up the disk drive.
    # PROBLEM #3: Isn't there something better that does this all automatically for me?
    with open(path_file, 'a') as file_log:
        # The print function nicely handles the line endings \n on mac/linux or \r\n on Windows.
        print("{} >>> {}".format(datetime.datetime.now(), message), file=file_log)


def main():
    print("Let's use the log_file function to write to the log file directly.")
    log_file("George Lucas ruined Star Wars.")
    time.sleep(2)
    log_file("No really, he did.")
    time.sleep(1)

    # If you plan to only write to this log file on occasion and only from a single class,
    # the problems elicited in the function comments are a non issue.


if __name__ == '__main__':
    main()
