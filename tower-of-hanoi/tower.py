import copy
import sys

TOTAL_DISKS = 5

SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}

    while True:
        displayTowers(towers)

        fromTower, toTower = getPlayerMove(towers)

        disk = towers[fromTower].pop()
        towers[toTower].append(disk)


def getPlayerMove(towers):
    pass


def displayTowers(towers):
    pass


def displayDisk(width):
    pass


if __name__ == "__main__":
    main()
