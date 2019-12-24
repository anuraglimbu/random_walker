"""
    This is just a demo of a single drunkard's walk in 2D space
"""

import turtle
import random

drunkard = turtle.Turtle()
drunkard.shapesize(0.7, 0.7)
drunkard.speed(1)

print("Enter number of steps to take:", end="")
n = int(input())
k = 5


def getch():
    raw = input()


def drunk_coord(num_walk):
    x, y = 0, 0
    for i in range(1, 1001):
        (dx, dy) = random.choice([(0, k), (0, -k), (k, 0), (-k, 0)])
        x = x + dx
        y = y + dy

        if dy > 0:
            drunkard.left(90)
        elif dy < 0:
            drunkard.right(90)

        drunkard.goto(x, y)
    drunkard.clear()
    drunkard.reset()
    return(x, y)


def main():
    total_distance = 0
    for i in range(1, n+1):
        num_walk = i
        get_coord = drunk_coord(num_walk)
        steps = ((get_coord[0])**2+(get_coord[1])**2)**0.5
        total_distance = total_distance + steps

    avg = total_distance / n
    print("Average: {}".format(avg))


if __name__ == "__main__":
    main()
    getch()
