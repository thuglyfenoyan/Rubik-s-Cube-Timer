# cube_timer.py: contains the main function for measuring the time
# taken for the user to solve a puzzle.

import time


def time_solve():
    i = input('Enter the enter button to start timer: ')
    start = time.time()
    print('Recording...')
    i = input('Enter the enter button to stop timer: ')
    stop = time.time()
    time = stop - start
    return time

