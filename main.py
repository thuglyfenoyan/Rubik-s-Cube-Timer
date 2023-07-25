# Author:           Fawaaz Kamali Siddiqui
# Last Update:      25-July-2023

from Puzzles import Puzzle
import scrambles
import funcs
import os


# puzzle variables declaration section
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

# Puzzle object declaration
cube_2x2 = Puzzle('2x2', times_2x2, scrambles_2x2, avg5_2x2, avg12_2x2)
cube_3x3 = Puzzle('3x3', times_3x3, scrambles_3x3, avg5_3x3, avg12_3x3)
cube_4x4 = Puzzle('4x4', times_4x4, scrambles_4x4, avg5_4x4, avg12_4x4)
cube_5x5 = Puzzle('5x5', times_5x5, scrambles_5x5, avg5_5x5, avg12_5x5)
cube_6x6 = Puzzle('6x6', times_6x6, scrambles_6x6, avg5_6x6, avg12_6x6)

# Possible puzzle options
PUZZLE_OPTIONS = {
    "1": cube_2x2,
    "2": cube_3x3,
    "3": cube_4x4,
    "4": cube_5x5,
    "5": cube_6x6
}

if __name__ == '__main__':

    for i in range(3):
        n = input('What puzzle mode do you want: ')
        if n in PUZZLE_OPTIONS:
            puzzle = PUZZLE_OPTIONS[n]
            for j in range(2):
                puzzle.record_solve()
            puzzle.history()
            puzzle.statistics()
        else:
            print('Not available')


    # for i in range(3):
    #     cube_3x3.record_solve()
    # cube_3x3.history()
    # cube_3x3.statistics()
    # for i in range(8):
    #     funcs.record_solve(times_2x2, scrambles_2x2, scrambles.scramble_2x2(), avg5_2x2, avg12_2x2)
    #
    # funcs.history(times_2x2, scrambles_2x2)
    # funcs.print_list(avg5_2x2)
    # deletion = int(input('Enter the solve number you want to remove: '))
    # funcs.del_solve(times_2x2, scrambles_2x2, avg5_2x2, avg12_2x2, deletion)
    #
    # funcs.history(times_2x2, scrambles_2x2)
    # funcs.print_list(avg5_2x2)

