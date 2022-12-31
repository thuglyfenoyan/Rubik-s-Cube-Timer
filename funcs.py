# funcs.py: Contains various functions that are used throughout
# the menu selection / main program

from cube_timer import time_solve
import scrambles


# variable declaration section
times_2x2 = []
times_3x3 = []
times_4x4 = []
times_5x5 = []
times_6x6 = []
scrambles_2x2 = []
scrambles_3x3 = []
scrambles_4x4 = []
scrambles_5x5 = []
scrambles_6x6 = []
avg5_2x2 = []       # keep track of best averages in a session and its occurrence
avg5_3x3 = []
avg5_4x4 = []
avg5_5x5 = []
avg5_6x6 = []
avg12_2x2 = []
avg12_3x3 = []
avg12_4x4 = []
avg12_5x5 = []
avg12_6x6 = []


def print_list(lst):
    for i in lst:
        print(i, end=', ')
    print()  # newline


def record_solves(mode):
    global times_2x2, times_3x3, times_4x4, times_5x5, times_6x6
    global scrambles_2x2, scrambles_3x3, scrambles_4x4, scrambles_5x5, scrambles_6x6
    global avg5_2x2, avg5_3x3, avg5_4x4, avg5_5x5, avg5_6x6
    global avg12_2x2, avg12_3x3, avg12_4x4, avg12_5x5, avg12_6x6

    if mode == '2x2':
        shuffle = scrambles.scramble_2x2()
        scrambles_2x2.append(shuffle)
        print_list(shuffle)
        time_taken = time_solve()
        times_2x2.append(time_taken)
