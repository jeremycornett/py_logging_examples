"""
Author: Jeremy Cornett
Date: 11/4/2019
Purpose: Show how to use the python logging library.
"""

import logging
import os


def main():
    print("The logging library is a complex implimentation that has many considerations.")
    print("Without more information about the program that needs to do logging, how often you want log,")
    print("what targets you want to log to (file, stdout/stderr, etc), it's hard to say more.")
    print("The library has decent documentation.")
    print()
    print("https://docs.python.org/3/howto/logging.html#when-to-use-logging")
    print()
    print("Each of the commented sections below must be uncommented separately and run in their own command prompt.")

    # --------------------------------------------------------------------------------------

    # logging.warning('Watch out!')  # will print a message to the console
    # logging.info('I told you so')  # will not print anything

    # --------------------------------------------------------------------------------------

    logging.basicConfig(filename=os.path.join(os.path.dirname(os.path.realpath(__file__)), "example.log"),
                        level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')

    # --------------------------------------------------------------------------------------

    # # create logger
    # logger = logging.getLogger('simple_example')
    # logger.setLevel(logging.DEBUG)
    #
    # # create console handler and set level to debug
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)
    #
    # # create formatter
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #
    # # add formatter to ch
    # ch.setFormatter(formatter)
    #
    # # add ch to logger
    # logger.addHandler(ch)
    #
    # # 'application' code
    # logger.debug('debug message')
    # logger.info('info message')
    # logger.warning('warn message')
    # logger.error('error message')
    # logger.critical('critical message')

    # --------------------------------------------------------------------------------------

    print()
    print("My guess is that you'll want to use the second example to just output to a file with the formatter from")
    print("the third example?")
    print()
    print("Look at the logging cookbook for examples on how to handle logging with threads and processes.")
    print("Doing it with threads/processes looks rather complicated, so unless you do intend to log from")
    print("threads or processes, I'd rather not code up examples. Let me know if you do intend to and I can")
    print("whip something up.")
    print()
    print("https://docs.python.org/3/howto/logging-cookbook.html")


if __name__ == '__main__':
    main()
