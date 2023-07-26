from cube_timer import time_solve
import scrambles
import os
import datetime
from funcs import print_list, to_mins, calc_avg5, calc_avg12, get_shuffle


class Puzzle:

    def __init__(self, puzzle_type, times, scramble_list, avg5, avg12):
        self.puzzle_type = puzzle_type          # determining which cube scramble will be displayed
        self.times = times                      # keeping track of all times for a puzzle
        self.scramble_list = scramble_list      # keeping track of all scrambles for a puzzle
        self.avg5 = avg5                        # keeping track of all averages for a puzzle
        self.avg12 = avg12

    def record_solve(self):
        shuffle = scrambles.scramble(self.puzzle_type)
        print_list(shuffle)
        time_taken = time_solve()
        if time_taken == -1:    # user wants to quit
            return -1
        # record data
        self.scramble_list.append(shuffle)
        self.times.append(time_taken)
        current_avg5 = 'n/a'
        current_avg12 = 'n/a'
        if len(self.times) >= 5:
            current_avg5 = calc_avg5(self.times)
            self.avg5.append(current_avg5)
            if len(self.times) >= 12:
                current_avg12 = calc_avg12(self.times)
                self.avg12.append(current_avg12)
        # display data
        print('%s %-10s%s %-10s%s %-10s' % (
        'Time Taken:', to_mins(time_taken), 'Average of 5:', current_avg5, 'Average of 12:', current_avg12))
        print('*******************************************')  # separators for each solve

    def del_solve(self, index):
        # pop solve from times and scrambles and update average lists
        if 0 < int(index) <= len(self.times):
            self.times.pop(index - 1)
            self.scramble_list.pop(index - 1)
        else:
            print('Solve number not found.')
            return

        # update average lists after deletion
        if len(self.times) >= 5:
            self.avg5.pop(0)
            for i in range(len(self.avg5)):
                self.avg5[i] = calc_avg5(self.times[i:i + 5])
                if len(self.times) >= 12:
                    self.avg12.pop(0)
                    for j in range(len(self.avg12)):
                        self.avg12[j] = calc_avg12(self.times[i:i + 12])

    def history(self):  # displays ALL solves and scrambles for the puzzle
        os.system('cls')
        print('%-10s %-10s%s' % ('Solve No.', 'Time', 'Scramble'))
        for i in range(len(self.times)):
            print('%-10d %-10.3f' % (i + 1, self.times[i]), end='')
            print_list(self.scramble_list[i])

    def statistics(self):
        if len(self.times) >= 1:
            print('%-20s %-10s ' % ('Best Solve:', to_mins(min(self.times))), end='')
            print_list(self.scramble_list[self.times.index(min(self.times))])
            if len(self.times) >= 5:
                print('%-20s %-10s' % ('Best a05:', to_mins(min(self.avg5))), end='')
                print_list(self.times[self.avg5.index(min(self.avg5)):self.avg5.index(min(self.avg5)) + 5])
                if len(self.times) >= 12:
                    print('%-20s %-10s' % ('Best a012:', to_mins(min(self.avg12))), end='')
                    print_list(self.times[self.avg12.index(min(self.avg12)):self.avg12.index(min(self.avg12)) + 12])

    def get_puzzle_type(self):
        return self.puzzle_type


