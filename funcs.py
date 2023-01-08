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


def calc_avg5(lst):     # the best and worst solves are excluded from calculating average
    avg = 'n/a'
    if len(lst) >= 5:
        prev5 = lst[len(lst) - 5:]
        avg = (sum(prev5) - max(prev5) - min(prev5)) / 3
    return round(avg, 3)


def calc_avg12(lst):    # the best and worst solves are excluded from calculating average
    avg = 'n/a'
    if len(lst) >= 12:
        prev12 = lst[len(lst)-12:]
        avg = (sum(prev12) - max(prev12) - min(prev12)) / 10
    return round(avg, 3)


def statistics():
    # TODO: Display PB, Best avg5 and best avg12 of each puzzle
    if len(times_2x2) >= 1:
        print('******************** 2x2 ********************')
        print(f'Best Solve:      {min(times_2x2)}       ', end='')
        print_list(scrambles_2x2[times_2x2.index(min(times_2x2))])
        if len(times_2x2) >= 5:
            print(f'Best ao5:        {min(avg5_2x2)}        ', end='')
            print_list(times_2x2[avg5_2x2.index(min(avg5_2x2)):avg5_2x2.index(min(avg5_2x2))+5])
            if len(times_2x2) >= 12:
                print(f'Best ao12:        {min(avg12_2x2)}        ', end='')
                print_list(times_2x2[avg12_2x2.index(min(avg12_2x2)):avg12_2x2.index(min(avg12_2x2)) + 12])


def record_2x2():
    global times_2x2, scrambles_2x2, avg5_2x2, avg12_2x2
    shuffle = scrambles.scramble_2x2()
    print_list(shuffle)
    time_taken = time_solve()
    # record data
    scrambles_2x2.append(shuffle)
    times_2x2.append(time_taken)
    avg5 = 'n/a'
    avg12 = 'n/a'
    if len(times_2x2) >= 5:
        avg5 = calc_avg5(times_2x2)
        avg5_2x2.append(avg5)
        if len(times_2x2) >= 12:
            avg12 = calc_avg12(times_2x2)
            avg12_2x2.append(avg12)
    # display data
    print('%s %-10s%s %-10s%s %-10s' % ('Time Taken:', time_taken, 'Average of 5:', avg5, 'Average of 12:', avg12))
    print('*******************************************')    # separators for each solve


def record_3x3():
    global times_3x3, scrambles_3x3, avg5_3x3, avg12_3x3
    shuffle = scrambles.scramble_3x3()
    print_list(shuffle)
    time_taken = time_solve()
    # record data
    scrambles_3x3.append(shuffle)
    times_3x3.append(time_taken)
    avg5 = 'n/a'
    avg12 = 'n/a'
    if len(times_3x3) >= 5:
        avg5 = calc_avg5(times_3x3)
        avg5_3x3.append(avg5)
        if len(times_3x3) >= 12:
            avg12 = calc_avg12(times_3x3)
            avg12_3x3.append(avg12)
    # display data
    print('%s %-10s%s %-10s%s %-10s' % ('Time Taken:', time_taken, 'Average of 5:', avg5, 'Average of 12:', avg12))
    print('*******************************************')    # separators for each solve


def record_4x4():
    global times_4x4, scrambles_4x4, avg5_4x4, avg12_4x4
    shuffle = scrambles.scramble_4x4()
    print_list(shuffle)
    time_taken = time_solve()
    # record data
    scrambles_4x4.append(shuffle)
    times_4x4.append(time_taken)
    avg5 = 'n/a'
    avg12 = 'n/a'
    if len(times_4x4) >= 5:
        avg5 = calc_avg5(times_4x4)
        avg5_4x4.append(avg5)
        if len(times_4x4) >= 12:
            avg12 = calc_avg12(times_4x4)
            avg12_4x4.append(avg12)
    # display data
    print('%s %-10s%s %-10s%s %-10s' % ('Time Taken:', time_taken, 'Average of 5:', avg5, 'Average of 12:', avg12))
    print('*******************************************')    # separators for each solve


def record_5x5():
    global times_5x5, scrambles_5x5, avg5_5x5, avg12_5x5
    shuffle = scrambles.scramble_5x5()
    print_list(shuffle)
    time_taken = time_solve()
    # record data
    scrambles_5x5.append(shuffle)
    times_5x5.append(time_taken)
    avg5 = 'n/a'
    avg12 = 'n/a'
    if len(times_5x5) >= 5:
        avg5 = calc_avg5(times_5x5)
        avg5_5x5.append(avg5)
        if len(times_5x5) >= 12:
            avg12 = calc_avg12(times_5x5)
            avg12_5x5.append(avg12)
    # display data
    print('%s %-10s%s %-10s%s %-10s' % ('Time Taken:', time_taken, 'Average of 5:', avg5, 'Average of 12:', avg12))
    print('*******************************************')    # separators for each solve


def record_6x6():
    global times_6x6, scrambles_6x6, avg5_6x6, avg12_6x6
    shuffle = scrambles.scramble_6x6()
    print_list(shuffle)
    time_taken = time_solve()
    # record data
    scrambles_6x6.append(shuffle)
    times_6x6.append(time_taken)
    avg5 = 'n/a'
    avg12 = 'n/a'
    if len(times_6x6) >= 5:
        avg5 = calc_avg5(times_6x6)
        avg5_6x6.append(avg5)
        if len(times_6x6) >= 12:
            avg12 = calc_avg12(times_6x6)
            avg12_6x6.append(avg12)
    # display data
    print('%s %-10s%s %-10s%s %-10s' % ('Time Taken:', time_taken, 'Average of 5:', avg5, 'Average of 12:', avg12))
    print('*******************************************')    # separators for each solve


