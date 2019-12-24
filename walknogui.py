import random

print("Enter number of walks to take:", end="")
n = int(input())
k = 1


def getch():
    print("\nPress any key to continue...")
    raw = input()


def drunk_coord(num_walk):
    x, y = 0, 0
    for i in range(1, 1001):
        (dx, dy) = random.choice([(0, k), (0, -k), (k, 0), (-k, 0)])
        x = x + dx
        y = y + dy
    return(x, y)


def main():
    total_distance = 0
    steps = 0
    for i in range(1, n+1):
        num_walk = i
        distance = 0
        get_coord = drunk_coord(num_walk)
        steps = ((get_coord[0])**2+(get_coord[1])**2)**0.5
        total_distance = (total_distance + steps)

    avg = total_distance / n
    print("Average: {}".format(avg))
    return avg


if __name__ == "__main__":
    avg_dt = 0
    for i in range(10):
        avg_dt = avg_dt + main()

    avg = avg_dt / 10
    print("Final Average: {}".format(avg))
    getch()
