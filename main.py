# Author:           Fawaaz Kamali Siddiqui
# Last Update:      08-January-2023

import scrambles
import cube_timer
import funcs
import os


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

if __name__ == '__main__':

    for i in range(5):
        funcs.record_solve(times_2x2, scrambles_2x2, scrambles.scramble_2x2(), avg5_2x2, avg12_2x2)
    funcs.print_list(times_2x2)
    funcs.print_list(scrambles_2x2)
    funcs.print_list(avg5_2x2)
    funcs.print_list(avg12_2x2)

