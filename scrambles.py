# scrambles.py: Contains functions for generating scrambles for
# 2x2, 3x3, 4x4, 5x5 and 6x6 Rubik's Cubes

import random


def scramble_2x2():                           # 9 moves long
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


def scramble_3x3():                           # 20 moves long
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


def scramble_4x4():                           # 40 moves long
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

