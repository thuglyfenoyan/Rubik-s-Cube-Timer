# funcs.py: Contains various functions that are used throughout
# the menu selection / main program

from cube_timer import time_solve
import scrambles
import datetime


def print_list(lst):
    for i in lst:
        print(i, end=', ')
    print()  # newline


def to_mins(time, round_to=3):  # convert seconds to either minutes or hours if required
    if time < 60:
        return time
    elif 60 <= time < 3600:
        mins = int(time // 60)
        seconds = round(time % 60, round_to)
        return f'%d:%ds.{round_to}f' % (mins, seconds)
    else:
        return str(datetime.timedelta(seconds=time))


def input_num(prompt):  # Validating input from user. Used in main menu
    num = 0
    while True:
        try:
            num = int(input(prompt))
            return num
        except:
            print('Invalid Input.')


def calc_avg5(lst):     # the best and worst solves are excluded when calculating average
    avg = 'n/a'
    if len(lst) >= 5:
        prev5 = lst[len(lst) - 5:]
        avg = (sum(prev5) - max(prev5) - min(prev5)) / 3
    return round(avg, 3)


def calc_avg12(lst):    # the best and worst solves are excluded when calculating average
    avg = 'n/a'
    if len(lst) >= 12:
        prev12 = lst[len(lst)-12:]
        avg = (sum(prev12) - max(prev12) - min(prev12)) / 10
    return round(avg, 3)


def statistics(times, scramble_list, avg5, avg12):
    if len(times) >= 1:
        print('%-20s %-10s ' % ('Best Solve:', to_mins(min(times))), end='')
        print_list(scramble_list[times.index(min(times))])
        if len(times) >= 5:
            print('%-20s %-10s' % ('Best a05:', to_mins(min(avg5))), end='')
            print_list(times[avg5.index(min(avg5)):avg5.index(min(avg5))+5])
            if len(times) >= 12:
                print('%-20s %-10s' % ('Best a012:', to_mins(min(avg12))), end='')
                print_list(times[avg12.index(min(avg12)):avg12.index(min(avg12)) + 12])


def get_shuffle(puzzle_type):
    shuffle = puzzle_type
    print_list(shuffle)



# def statistics():
#     if len(times_2x2) >= 1:
#         print('******************** 2x2 ********************')
#         print(f'Best Solve:      {min(times_2x2)}       ', end='')
#         print_list(scrambles_2x2[times_2x2.index(min(times_2x2))])
#         if len(times_2x2) >= 5:
#             print(f'Best ao5:        {min(avg5_2x2)}        ', end='')
#             print_list(times_2x2[avg5_2x2.index(min(avg5_2x2)):avg5_2x2.index(min(avg5_2x2))+5])
#             if len(times_2x2) >= 12:
#                 print(f'Best ao12:        {min(avg12_2x2)}        ', end='')
#                 print_list(times_2x2[avg12_2x2.index(min(avg12_2x2)):avg12_2x2.index(min(avg12_2x2)) + 12])
#
#     if len(times_3x3) >= 1:
#         print('******************** 3x3 ********************')
#         print(f'Best Solve:      {min(times_3x3)}       ', end='')
#         print_list(scrambles_3x3[times_3x3.index(min(times_3x3))])
#         if len(times_3x3) >= 5:
#             print(f'Best ao5:        {min(avg5_3x3)}        ', end='')
#             print_list(times_3x3[avg5_3x3.index(min(avg5_3x3)):avg5_3x3.index(min(avg5_3x3))+5])
#             if len(times_3x3) >= 12:
#                 print(f'Best ao12:        {min(avg12_3x3)}        ', end='')
#                 print_list(times_3x3[avg12_3x3.index(min(avg12_3x3)):avg12_3x3.index(min(avg12_3x3)) + 12])
#
#     if len(times_4x4) >= 1:
#         print('******************** 4x4 ********************')
#         print(f'Best Solve:      {min(times_4x4)}       ', end='')
#         print_list(scrambles_4x4[times_4x4.index(min(times_4x4))])
#         if len(times_4x4) >= 5:
#             print(f'Best ao5:        {min(avg5_4x4)}        ', end='')
#             print_list(times_4x4[avg5_4x4.index(min(avg5_4x4)):avg5_4x4.index(min(avg5_4x4))+5])
#             if len(times_4x4) >= 12:
#                 print(f'Best ao12:        {min(avg12_4x4)}        ', end='')
#                 print_list(times_4x4[avg12_4x4.index(min(avg12_4x4)):avg12_4x4.index(min(avg12_4x4)) + 12])
#
#     if len(times_5x5) >= 1:
#         print('******************** 5x5 ********************')
#         print(f'Best Solve:      {min(times_5x5)}       ', end='')
#         print_list(scrambles_5x5[times_5x5.index(min(times_5x5))])
#         if len(times_5x5) >= 5:
#             print(f'Best ao5:        {min(avg5_5x5)}        ', end='')
#             print_list(times_5x5[avg5_5x5.index(min(avg5_5x5)):avg5_5x5.index(min(avg5_5x5))+5])
#             if len(times_5x5) >= 12:
#                 print(f'Best ao12:        {min(avg12_5x5)}        ', end='')
#                 print_list(times_5x5[avg12_5x5.index(min(avg12_5x5)):avg12_5x5.index(min(avg12_5x5)) + 12])
#
#     if len(times_6x6) >= 1:
#         print('******************** 6x6 ********************')
#         print(f'Best Solve:      {min(times_6x6)}       ', end='')
#         print_list(scrambles_6x6[times_6x6.index(min(times_6x6))])
#         if len(times_6x6) >= 5:
#             print(f'Best ao5:        {min(avg5_6x6)}        ', end='')
#             print_list(times_6x6[avg5_6x6.index(min(avg5_6x6)):avg5_6x6.index(min(avg5_6x6))+5])
#             if len(times_6x6) >= 12:
#                 print(f'Best ao12:        {min(avg12_6x6)}        ', end='')
#                 print_list(times_6x6[avg12_6x6.index(min(avg12_6x6)):avg12_6x6.index(min(avg12_6x6)) + 12])


def history(times, scramble_list):  # history of ALL solves of a specific puzzle
    print('%-10s %-10s%s' % ('Solve No.', 'Time', 'Scramble'))
    for i in range(len(times)):
        print('%-10d %-10.3f' % (i + 1, times[i]), end='')
        print_list(scramble_list[i])


# def history(puzzle):
#     print('%-10s %-10s%s' % ('Solve No.', 'Time', 'Scramble'))
#     if puzzle == '2x2':
#         for i in range(len(times_2x2)):
#             print('%-10d %-10.3f' % (i+1, times_2x2[i]), end='')
#             print_list(scrambles_2x2[i])
#     elif puzzle == '3x3':
#         for i in range(len(times_3x3)):
#             print('%-10d %-10.3f' % (i+1, times_3x3[i]), end='')
#             print_list(scrambles_3x3[i])
#     elif puzzle == '4x4':
#         for i in range(len(times_4x4)):
#             print('%-10d %-10.3f' % (i+1, times_4x4[i]), end='')
#             print_list(scrambles_4x4[i])
#     elif puzzle == '5x5':
#         for i in range(len(times_5x5)):
#             print('%-10d %-10.3f' % (i+1, times_5x5[i]), end='')
#             print_list(scrambles_5x5[i])
#     elif puzzle == '6x6':
#         for i in range(len(times_6x6)):
#             print('%-10d %-10.3f' % (i+1, times_5x5[i]), end='')
#             print_list(scrambles_6x6[i])


def record_solve(times, scramble_list, scramble_func, avg5, avg12):
    shuffle = scramble_func
    print_list(shuffle)
    time_taken = time_solve()
    # record data
    scramble_list.append(shuffle)
    times.append(time_taken)
    current_avg5 = 'n/a'
    current_avg12 = 'n/a'
    if len(times) >= 5:
        current_avg5 = calc_avg5(times)
        avg5.append(current_avg5)
        if len(times) >= 12:
            current_avg12 = calc_avg12(times)
            avg12.append(current_avg12)
    # display data
    print('%s %-10s%s %-10s%s %-10s' % ('Time Taken:', to_mins(time_taken), 'Average of 5:', current_avg5, 'Average of 12:', current_avg12))
    print('*******************************************')  # separators for each solve


def del_solve(times, scramble_list, avg5, avg12, index):
    # TODO: Pop solve from times and scrambles and update average lists
    times.pop(index-1)
    scramble_list.pop(index-1)

    # update average lists after deletion
    if len(times) >= 5:
        avg5.pop(0)
        for i in range(len(avg5)):
            avg5[i] = calc_avg5(times[i:i+5])   
            if len(times) >= 12:
                avg12.pop(0)
                for j in range(len(avg12)):
                    avg12[j] = calc_avg12(times[i:i+12])


'''
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
'''


