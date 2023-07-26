# cube_timer.py: contains the main function for measuring the time
# taken for the user to solve a puzzle.

import time
import keyboard
from msvcrt import getch


def time_solve():
    # i = input('Enter the enter button to start timer: ')
    # start = time.time()
    # print('Recording...')
    # i = input('Enter the enter button to stop timer: ')
    # stop = time.time()


    # print('Enter the space bar to start timer: ')
    # while True:
    #     if keyboard.is_pressed(' '):
    #         start = time.time()
    #         break
    #
    # time.sleep(0.2)     # 2 spacebars can be recorded in a very short amount of time
    # print('Enter the space bar to stop timer: ')
    #
    # while True:
    #     if keyboard.is_pressed(' '):
    #         end = time.time()
    #         break

    to_press = [13, 32]  # order number for enter and space bar
    print('Enter \'g\' to go back: ')
    print('Press either the space bar or enter button to start: ')
    key = ord(getch())
    if key in to_press:
        start = time.time()
    elif key in [47, 103, '\'g\'']:    # user wants to quit
        return -1

    time.sleep(0.1)
    print('Press either the space bar or enter button to stop: ')
    key = ord(getch())
    if key in to_press:
        end = time.time()
    elif key in [47, 103, '\'g\'']:    # user wants to quit
        return -1

    solve_time = end - start
    return round(solve_time, 3)

