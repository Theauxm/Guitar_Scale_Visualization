from colorama import Fore
from colorama import Style

FRETBOARD_LENGTH = 15

NOTES_ASC = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
NOTES_ASC_A_0 = dict()
NOTES_ASC_0_A = dict()
for idx, note in enumerate(NOTES_ASC):
    NOTES_ASC_A_0[note] = idx
    NOTES_ASC_0_A[idx] = note

NOTES_DES = ["G", "Gb", "F", "E", "Eb", "D", "Db", "C", "B", "Bb", "A", "Ab"]
NOTES_DES_A_0 = dict()
NOTES_DES_0_A = dict()
for idx, note in enumerate(NOTES_DES):
    NOTES_DES_A_0[note] = idx
    NOTES_DES_0_A[idx] = note

STRING_TUNING = ["E", "A", "D", "G", "B", "E"]

MAJOR_SCALE = [2, 2, 1, 2, 2, 2, 1]

MINOR_SCALE = [2, 1, 2, 2, 1, 2, 2]

# [['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#'],
# ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
# ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#'],
# ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
# ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#'],
# ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#']]
FRETBOARD_ASC = [
    [
        NOTES_ASC_0_A[i % len(NOTES_ASC)]
        for i in range(
            NOTES_ASC_A_0[STRING_TUNING[x]],
            NOTES_ASC_A_0[STRING_TUNING[x]] + FRETBOARD_LENGTH,
        )
    ]
    for x in range(len(STRING_TUNING))
]

# [['E', 'Eb', 'D', 'Db', 'C', 'B', 'Bb', 'A', 'Ab', 'G', 'Gb', 'F'],
# ['A', 'Ab', 'G', 'Gb', 'F', 'E', 'Eb', 'D', 'Db', 'C', 'B', 'Bb'],
# ['D', 'Db', 'C', 'B', 'Bb', 'A', 'Ab', 'G', 'Gb', 'F', 'E', 'Eb'],
# ['G', 'Gb', 'F', 'E', 'Eb', 'D', 'Db', 'C', 'B', 'Bb', 'A', 'Ab'],
# ['B', 'Bb', 'A', 'Ab', 'G', 'Gb', 'F', 'E', 'Eb', 'D', 'Db', 'C'],
# ['E', 'Eb', 'D', 'Db', 'C', 'B', 'Bb', 'A', 'Ab', 'G', 'Gb', 'F']]
FRETBOARD_DES = [
    [
        NOTES_DES_0_A[i % len(NOTES_DES)]
        for i in range(
            NOTES_DES_A_0[STRING_TUNING[x]],
            NOTES_DES_A_0[STRING_TUNING[x]] + FRETBOARD_LENGTH,
        )
    ]
    for x in range(len(STRING_TUNING))
]


C_SCALE_SHAPE = [
    [True, False, False, True, False],
    [True, False, False, True, False],
    [True, False, True, False, False],
    [True, False, True, False, False],
    [False, True, False, True, False],
    [True, False, False, True, False],
]

A_SCALE_SHAPE = [
    [False, True, False, True, False],
    [False, True, False, True, False],
    [True, False, False, True, False],
    [True, False, False, True, False],
    [False, True, False, True, False],
    [False, True, False, True, False],
]

G_SCALE_SHAPE = [
    [True, False, False, True, False],
    [True, False, True, False, False],
    [True, False, True, False, False],
    [True, False, True, False, False],
    [True, False, False, True, False],
    [True, False, False, True, False],
]

E_SCALE_SHAPE = [
    [False, True, False, True, False],
    [True, False, False, True, False],
    [True, False, False, True, False],
    [True, False, True, False, False],
    [False, True, False, True, False],
    [False, True, False, True, False],
]

D_SCALE_SHAPE = [
    [False, True, False, True, False],
    [False, True, False, True, False],
    [False, True, False, True, False],
    [True, False, False, True, False],
    [False, True, False, False, True],
    [False, True, False, True, False],
]


def scale_map(shape, root):
    root_idx = (
        (NOTES_ASC_A_0[STRING_TUNING[0]] + NOTES_ASC_A_0[root] - 2) % len(NOTES_ASC)
        if root
        else -1
    )

    offset_shape = shape[0].index(True)

    root_idx -= offset_shape

    return [
        [False for i in range(root_idx)]
        + [shape[x][(j + offset_shape) if (j + offset_shape) < len(shape[x]) and root == STRING_TUNING[0] else j] for j in range(len(shape[x]))]
        # + shape[x]
        + [False for i in range(FRETBOARD_LENGTH - root_idx - len(shape[x]))]
        for x in range(len(shape))
    ]


DELIMETER = "-------"


def fretboard_asc_to_str(shape_map=None, color=Fore.WHITE):

    for string_idx, string in enumerate(FRETBOARD_ASC):
        for note_idx, note in enumerate(string):
            l = 0 - len(note)

            if shape_map and shape_map[string_idx][note_idx]:
                print(
                    f"{DELIMETER[:l]}{color}[{note}]{Style.RESET_ALL}{DELIMETER[:l]}",
                    end="",
                )
            else:
                print(f"{DELIMETER[:l]}{note}{DELIMETER[:l]}", end="")
        print()


def fretboard_des_to_str():
    for string in FRETBOARD_DES:
        for note in string:
            if len(note) == 2:
                print(f"{note}{DELIMETER[:-1]}", end="")
            else:
                print(f"{note}{DELIMETER}", end="")
        print()
