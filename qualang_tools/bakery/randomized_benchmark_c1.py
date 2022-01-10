import numpy as np

c1_ops = [  # Clifford operations
    ("I",),
    ("X",),
    ("Y",),
    ("Y", "X"),
    ("X/2", "Y/2"),
    ("X/2", "-Y/2"),
    ("-X/2", "Y/2"),
    ("-X/2", "-Y/2"),
    ("Y/2", "X/2"),
    ("Y/2", "-X/2"),
    ("-Y/2", "X/2"),
    ("-Y/2", "-X/2"),
    ("X/2",),
    ("-X/2",),
    ("Y/2",),
    ("-Y/2",),
    ("-X/2", "Y/2", "X/2"),
    ("-X/2", "-Y/2", "X/2"),
    ("X", "Y/2"),
    ("X", "-Y/2"),
    ("Y", "X/2"),
    ("Y", "-X/2"),
    ("X/2", "Y/2", "X/2"),
    ("-X/2", "Y/2", "-X/2"),
]

# Cayley table corresponding to above Clifford group structure

c1_table = np.array(
    [
        0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
        1, 1, 0, 3, 2, 6, 7, 4, 5, 11, 10, 9, 8, 13, 12, 18, 19, 22, 23, 14, 15, 21, 20, 16, 17,
        2, 2, 3, 0, 1, 7, 6, 5, 4, 10, 11, 8, 9, 20, 21, 15, 14, 23, 22, 19, 18, 12, 13, 17, 16,
        3, 3, 2, 1, 0, 5, 4, 7, 6, 9, 8, 11, 10, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 23, 22,
        4, 4, 7, 5, 6, 11, 8, 9, 10, 2, 3, 1, 0, 22, 17, 21, 12, 14, 18, 13, 20, 23, 16, 15, 19,
        5, 5, 6, 4, 7, 10, 9, 8, 11, 1, 0, 2, 3, 23, 16, 12, 21, 19, 15, 20, 13, 22, 17, 18, 14,
        6, 6, 5, 7, 4, 8, 11, 10, 9, 3, 2, 0, 1, 16, 23, 20, 13, 18, 14, 12, 21, 17, 22, 19, 15,
        7, 7, 4, 6, 5, 9, 10, 11, 8, 0, 1, 3, 2, 17, 22, 13, 20, 15, 19, 21, 12, 16, 23, 14, 18,
        8, 8, 9, 11, 10, 1, 3, 2, 0, 7, 4, 5, 6, 19, 14, 22, 16, 20, 12, 23, 17, 15, 18, 13, 21,
        9, 9, 8, 10, 11, 2, 0, 1, 3, 6, 5, 4, 7, 14, 19, 23, 17, 13, 21, 22, 16, 18, 15, 20, 12,
        10, 10, 11, 9, 8, 3, 1, 0, 2, 4, 7, 6, 5, 18, 15, 17, 23, 12, 20, 16, 22, 14, 19, 21, 13,
        11, 11, 10, 8, 9, 0, 2, 3, 1, 5, 6, 7, 4, 15, 18, 16, 22, 21, 13, 17, 23, 19, 14, 12, 20,
        12, 12, 13, 21, 20, 18, 19, 14, 15, 22, 17, 23, 16, 1, 0, 4, 5, 8, 10, 6, 7, 2, 3, 11, 9,
        13, 13, 12, 20, 21, 14, 15, 18, 19, 16, 23, 17, 22, 0, 1, 6, 7, 11, 9, 4, 5, 3, 2, 8, 10,
        14, 14, 19, 15, 18, 22, 16, 23, 17, 20, 21, 12, 13, 8, 9, 2, 0, 6, 4, 1, 3, 10, 11, 7, 5,
        15, 15, 18, 14, 19, 17, 23, 16, 22, 12, 13, 20, 21, 10, 11, 0, 2, 5, 7, 3, 1, 8, 9, 4, 6,
        16, 16, 23, 22, 17, 12, 21, 20, 13, 19, 14, 15, 18, 5, 6, 8, 11, 3, 0, 10, 9, 7, 4, 1, 2,
        17, 17, 22, 23, 16, 21, 12, 13, 20, 14, 19, 18, 15, 4, 7, 9, 10, 0, 3, 11, 8, 6, 5, 2, 1,
        18, 18, 15, 19, 14, 16, 22, 17, 23, 21, 20, 13, 12, 11, 10, 3, 1, 4, 6, 0, 2, 9, 8, 5, 7,
        19, 19, 14, 18, 15, 23, 17, 22, 16, 13, 12, 21, 20, 9, 8, 1, 3, 7, 5, 2, 0, 11, 10, 6, 4,
        20, 20, 21, 13, 12, 19, 18, 15, 14, 17, 22, 16, 23, 3, 2, 7, 6, 10, 8, 5, 4, 0, 1, 9, 11,
        21, 21, 20, 12, 13, 15, 14, 19, 18, 23, 16, 22, 17, 2, 3, 5, 4, 9, 11, 7, 6, 1, 0, 10, 8,
        22, 22, 17, 16, 23, 13, 20, 21, 12, 15, 18, 19, 14, 7, 4, 11, 8, 2, 1, 9, 10, 5, 6, 0, 3,
        23, 23, 16, 17, 22, 20, 13, 12, 21, 18, 15, 14, 19, 6, 5, 10, 9, 1, 2, 8, 11, 4, 7, 3, 0
    ]
).reshape(24, 25)[:, 1:]