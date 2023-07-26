# Author:           Fawaaz Kamali Siddiqui
# Last Update:      26-July-2023

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


# Function for getting user input from main menu
def get_menu():

    # TODO: Add menu for all puzzles and statistics menu
    valid_entries = ['1', '2', '3', '4', '5', '6', '7']  # possible valid entries
    while True:
        os.system('cls')  # clear terminal window
        mode = input('''Enter a number to choose function:
1. 2x2
2. 3x3
3. 4x4
4. 5x5
5. 6x6
6. Statistics
7. Logout
> ''')
        if mode in valid_entries:
            return mode


def puzzle_options(puzzle_object):

    # TODO: Add features for recording solves and checking history
    valid_entries = ['1', '2', 'g', '\'g\'']
    while True:
        os.system('cls')  # clear terminal window
        print(f'Current Puzzle: {puzzle_object.get_puzzle_type()}')
        mode = input('''Enter one of the following options:
1. Resume Current Session
2. History
Enter \'g\' to go back
> ''')
        if mode.lower() in valid_entries:
            return mode


class BreakMatch:
    pass


if __name__ == '__main__':

    mode = 0
    while mode != '7':  # while logout is not entered
        mode = get_menu()
        match mode:
            case '1' | '2' | '3' | '4' | '5':
                # TODO: Implement feature to remain in current state after recording solves
                puzzle = PUZZLE_OPTIONS[mode]
                function = puzzle_options(puzzle)  # displays puzzle menu
                match function:
                    case '1':  # record normal solves
                        # TODO: Implement feature to exit current state
                        for i in range(3):
                            puzzle.record_solve()
                    case '2':  # display puzzle history
                        # TODO: Implement del_solve() feature
                        puzzle.history()
                        foo = ''
                        while foo.lower() != 'g':
                            foo = input('Enter \'g\' to go back: ')
                    case _:     # going back to main menu
                        pass
            case '6':
                # TODO: Implement feature to exit current state
                for i in PUZZLE_OPTIONS:
                    print(f'********** {PUZZLE_OPTIONS[i].get_puzzle_type()} **********')
                    PUZZLE_OPTIONS[i].statistics()
            case '7':
                pass



