# scrambles.py: Contains functions for generating scrambles for
# 2x2, 3x3, 4x4, 5x5 and 6x6 Rubik's Cubes

import random


def scramble(puzzle_type):

    if puzzle_type == '2x2':    # 9 moves long
        shuffle = list()
        moves = [
            'R', 'R\'', 'R2',
            'U', 'U\'', 'U2',
            'F', 'F\'', 'F2',
        ]

        shuffle.append(random.choice(moves))
        while len(shuffle) < 9:
            random_move = random.choice(moves)
            if random_move[0] != shuffle[-1][0]:  # moves must not be repeated consecutively
                shuffle.append(random_move)
        return shuffle

    elif puzzle_type == '3x3':  # 20 moves long
        shuffle = list()
        moves = [
                    'R', 'R\'', 'R2',
                    'L', 'L\'', 'L2',
                    'U', 'U\'', 'U2',
                    'D', 'D\'', 'D2',
                    'F', 'F\'', 'F2',
                    'B', 'B\'', 'B2'
                ]

        shuffle.append(random.choice(moves))
        while len(shuffle) < 20:
            random_move = random.choice(moves)
            if random_move[0] != shuffle[-1][0]:
                shuffle.append(random_move)
        return shuffle

    elif puzzle_type == '4x4':                           # 40 moves long
        shuffle = list()
        moves = [
                    'R', 'R\'', 'R2', 'Rw', 'Rw\'', 'Rw2',
                    'L', 'L\'', 'L2',
                    'U', 'U\'', 'U2', 'Uw', 'Uw\'', 'Uw2',
                    'D', 'D\'', 'D2',
                    'F', 'F\'', 'F2', 'Fw', 'Fw\'', 'Fw2',
                    'B', 'B\'', 'B2'
                ]

        shuffle.append(random.choice(moves))
        while len(shuffle) < 40:
            random_move = random.choice(moves)
            if random_move[0] != shuffle[-1][0]:
                shuffle.append(random_move)
        return shuffle

    elif puzzle_type == '5x5':                           # 60 moves long
        shuffle = list()
        moves = [
                    'R', 'R\'', 'R2', 'Rw', 'Rw\'', 'Rw2',
                    'L', 'L\'', 'L2', 'Lw', 'Lw\'', 'Lw2',
                    'U', 'U\'', 'U2', 'Uw', 'Uw\'', 'Uw2',
                    'D', 'D\'', 'D2', 'Dw', 'Dw\'', 'Dw2',
                    'F', 'F\'', 'F2', 'Fw', 'Fw\'', 'Fw2',
                    'B', 'B\'', 'B2', 'Bw', 'Bw\'', 'Bw2'
                ]

        shuffle.append(random.choice(moves))
        while len(shuffle) < 60:
            random_move = random.choice(moves)
            if random_move[0] != shuffle[-1][0]:
                shuffle.append(random_move)
        return shuffle

    elif puzzle_type == '6x6':                           # 80 moves long
        shuffle = list()
        moves = [
                    'R', 'R\'', 'R2', 'Rw', 'Rw\'', 'Rw2', '3Rw', '3Rw\'', '3Rw2',
                    'L', 'L\'', 'L2', 'Lw', 'Lw\'', 'Lw2',
                    'U', 'U\'', 'U2', 'Uw', 'Uw\'', 'Uw2', '3Uw', '3Uw\'', '3Uw2',
                    'D', 'D\'', 'D2', 'Dw', 'Dw\'', 'Dw2',
                    'F', 'F\'', 'F2', 'Fw', 'Fw\'', 'Fw2', '3Fw', '3Fw\'', '3Fw2',
                    'B', 'B\'', 'B2', 'Bw', 'Bw\'', 'Bw2'
                ]

        shuffle.append(random.choice(moves))
        while len(shuffle) < 80:
            random_move = random.choice(moves)
            if random_move[0] != shuffle[-1][0] and random_move[0] != '3':
                shuffle.append(random_move)
            elif random_move[0] == '3' and shuffle[-1][0] == '3' and random_move[1] != shuffle[-1][1]:
                shuffle.append(random_move)
            elif random_move[0] == '3' and shuffle[-1][0] != '3' and random_move[1] != shuffle[-1][0]:
                shuffle.append(random_move)
        return shuffle

    else:
        print('Puzzle not supported.')

