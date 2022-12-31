# funcs.py: Contains various functions that are used throughout
# the menu selection / main program
import main


# variable declaration section
times_2x2 = []
times_3x3 = []
times_4x4 = []
times_5x5 = []
times_6x6 = []


def print_list(lst):
    for i in lst:
        print(i, end=', ')
    print()  # newline


def record_solve():
    global times_2x2, times_3x3, times_4x4, times_5x5, times_6x6
