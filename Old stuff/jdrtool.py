import random

# Todo Eng translation

"""
Simulateur de jet de dés
Si vous souhaitez quelque chose de plus soigné que de répéter random.randint(1, X) + random.randint(1, X)
avec X étant 4, 6 ou 8 pour chaque dé de chaque pair
dans la console Python quand vous jouez à PokéStories ou tout autre jdr papier "propulsé par l'Apocalypse"

Dice roll simulator
If you want something more polished than spamming random.randint(1, X) + random.randint(1, X)
with X being 4, 6 or 8 for each dice in each pairing
in the Python Console when you want to play PokéStories or any other PbtA TTRPG
"""

# TODO find how to use tuple/dict with randint/randrange or similar tools SO IT'S CLEAN AS FUCK
"""
facile = (1, 8)
normal = (1, 6)
difficile = (1, 4)

dice_roll = {
    "facile": (1, 8),
    "normal": (1, 6),
    "difficile": (1, 4)
}
"""


def facile():
    v = random.randint(1, 8)
    print("1d8 = {}".format(v), end="")
    return v


def normal():
    v = random.randint(1, 6)
    print("1d6 = {}".format(v), end="")
    return v


def difficile():
    v = random.randint(1, 4)
    print("1d4 = {}".format(v), end="")
    return v


# color the meaningful output
OKGREEN = "\033[92m"
OKCYAN = "\033[96m"
OKBLUE = "\033[94m"
ENDC = "\033[0m"
"""
HEADER = '\033[95m'
WARNING = '\033[93m'
FAIL = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
"""


def colors(target, color_type=OKBLUE):
    return color_type + str(target) + ENDC


while True:
    # light version :
    print(" 0        1        2        3        4")
    print("2d4    1d4+1d6    2d6    1d6+1d8    2d8")
    print("dur             normal            facile")

    # verbose version :
    print("0 : très difficile")
    print("1 : difficile")
    print("2 : normal")
    print("3 : facile")
    print("4 : très facile")

    choice = int(input("Number please : "))
    result = 0

    # error and end handling
    if choice == -1:
        exit()
    if choice < 0 or choice > 4:
        continue

    # main process v1, TODO refactor this shit
    """
    if choice == 0:
        result += difficile()
        print(" + ", end='')
        result += difficile()
    if choice == 1:
        result += difficile()
        print(" + ", end='')
        result += normal()
    if choice == 2:
        result += normal()
        print(" + ", end='')
        result += normal()
    if choice == 3:
        result += normal()
        print(" + ", end='')
        result += facile
    if choice == 4:
        result += facile()
        print(" + ", end='')
        result += facile()
    """

    # main process v2, TODO refactor more

    if choice == 0 or choice == 1:
        result += difficile()
    if choice == 2 or choice == 3:
        result += normal()
    if choice == 4:
        result += facile()
    print(" + ", end="")
    if choice == 0:
        result += difficile()
    if choice == 1 or choice == 2:
        result += normal()
    if choice == 3 or choice == 4:
        result += facile()

    print(" => {} : ".format(result), end="")

    if result >= 10:
        print(colors("Oui et ...", OKGREEN))
    elif result > 6:
        print(colors("Oui mais ...", OKCYAN))
    else:
        print(colors("Non mais ...", OKBLUE))
