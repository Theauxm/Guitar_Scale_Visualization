from colorama import Fore
from config import NOTES_ASC, C_SCALE_SHAPE, A_SCALE_SHAPE, G_SCALE_SHAPE, E_SCALE_SHAPE, D_SCALE_SHAPE, fretboard_asc_to_str, scale_map

def main():
    shape_map = {
        "C": C_SCALE_SHAPE,
        "A": A_SCALE_SHAPE,
        "G": G_SCALE_SHAPE,
        "E": E_SCALE_SHAPE,
        "D": D_SCALE_SHAPE
    }

    color_map = {
        "C": Fore.BLUE,
        "A": Fore.RED,
        "G": Fore.GREEN,
        "E": Fore.CYAN,
        "D": Fore.MAGENTA
    }

    inp = ""
    while True:
        inp = input("Shape,Root:")

        if inp == "":
            exit()

        if ',' not in inp:
            print("Needs a comma!! For example: C,C")
            continue

        shape, root = inp.split(',')

        if shape == "" or root == "":
            print("You silly cunt")
            continue

        if shape.upper() not in shape_map:
            print("Shape must be C | A | G | E | D")
            continue

        if root.upper() not in NOTES_ASC:
            print(f"root must be one of the following: {NOTES_ASC}")
            continue

        print(f"SHAPE: {shape.upper()}, ROOT: {root.upper()}")

        scale = scale_map(shape_map[shape.upper()], root.upper())

        fretboard_asc_to_str(scale, color=color_map[shape])

if __name__ == "__main__":
    main()