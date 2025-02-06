import math
from os.path import exists
import sys

import numpy as np

n = len(sys.argv)

origin = (0, 0)

a = (np.pi)
# op = float(sys.argv[1])
# a *= op
print("\nA:  ", a)


def calc_x(x, y, t):
    return int(np.abs(round((x * (np.cos(t))) - (y * (np.sin(t))), 1)))


def calc_y(x, y, t):
    return int(np.abs(round((x * (np.sin(t))) + (y * (np.cos(t))), 1)))


print("\n\n\n")
print((calc_x(6, 3, a), calc_y(6, 3, a)))
print("\n\n\n")


def calc_slope(co1, co2):
    return [(co2[1] - co1[1]), (co2[0] - co1[0])]


def render():
    rows = 30
    cols = 20
    q_row = int(cols / 2)
    q_col = int(rows / 2)
    quad1, quad2, quad3, quad4 = [["."] * cols for _ in range(q_row)], [["."] * cols for _ in range(q_row)], [
        ["."] * cols for _ in range(q_row)], [["."] * cols for _ in range(q_row)]
    content = [["."] * cols for _ in range(rows)]

    # (x,y, char)
    grid = [(0, 0, "*"), (calc_x(6, 0, a), calc_y(6, 0, a), "@"), (calc_x(6, 3, a), calc_y(6, 3, a), "O"), (0, 0, "&")]
    slopes = []
    for i in range(len(grid)):
        for k in range(len(grid)):
            if not k <= i:
                slopes.append((grid[i], grid[k], calc_slope(grid[i], grid[k])))

    print(slopes)

    width = len(str(max(rows, cols) - 1))
    content_line = "# ] values ]"
    # quad_line =  "# | quad + quad |"

    quad_dashes = "-".join("-" * width for _ in range(int(cols / 2)))
    dashes = quad_dashes + quad_dashes + "-" * (width + 1)

    # set the x and y axis

    # for(y,x) goes to content[x][y]. This runs (Large to small)
    for (x, y, c) in grid:
        if x >= 0 and y >= 0:  # quad 1 (S to L on X) (L to S on Y)
            quad1[x][y] = c
        elif x < 0 and y <= 0:  # quad 3 (L to S on X) (S to L on Y)
            quad3[np.abs(x)][np.abs(y)] = c
        elif x >= 0 > y:  # quad 4 (S to L on X) (S to L on Y)
            quad4[x][np.abs(y)] = c
        elif x < 0 > y:  # quad 2 (L to S on X) (L to S on Y)
            quad2[np.abs(x)][y] = c

    print(quad4[6][3])
    # dashes = "-".join("-" * width for _ in range(cols))
    frame_line = content_line.replace("values", dashes)
    frame_line = frame_line.replace("#", " " * width).replace(" ] ", "    +").replace(" ]", "----+")

    print(frame_line)

    y_mid = int(rows / 2)
    x_mid = int(cols / 2)
    for y in range(rows):
        values = ""
        for x in range(cols):
            if y < y_mid and x < x_mid:
                cell_value = quad2[x - x_mid][y - y_mid]
                values += cell_value + " " * width
            if y <= y_mid and x >= x_mid:
                cell_value = quad1[x - x_mid][y - y_mid]
                if x == x_mid and cell_value == ".":
                    values += "|" + " " * width
                if x == x_mid and y == y_mid:
                    values += "+" + "-" * width
                if y == y_mid:
                    values += "-" * (width + 1)
                if y != y_mid:
                    values += cell_value + " " * width
            if y >= y_mid and x < x_mid:
                cell_value = quad3[x - x_mid][y - y_mid]
                if y == y_mid and cell_value == ".":
                    values += "-" * (width + 1)
                if y != y_mid:
                    values += cell_value + " " * width
            if y > y_mid and x >= x_mid:
                cell_value = quad4[x - x_mid][y - y_mid]
                if x == x_mid:
                    values += "|" + " " * width
                values += cell_value + " " * width
        quad_line = content_line.replace("values", values)
        if y < y_mid:
            quad_line = quad_line.replace("#", f"  {y_mid - y:{width}d}")
        elif y == y_mid:
            quad_line = quad_line.replace(" ] ", "  +"+"-" * width).replace(" ]", "+").replace("#",f"  {0:{width}d}")
        elif y > y_mid:
            quad_line = quad_line.replace("#", f"- {y - y_mid:{width}d}")

        quad_line = quad_line.replace(" ] ", "  |" + " "*width).replace(" ]", "|")
        print(quad_line)
    print(frame_line)

    num_line = content_line.replace("]", " "*width)
    num_line = num_line.replace("#", " " * int(width + 3))
    pos_nums = " ".join(f"{i + 1:<{width}d}" for i in range(q_row))
    neg_nums = " ".join(f"{q_row-i:<{width}d}" for i in range(q_row))
    num_line = num_line.replace("values", f"{neg_nums} 0  {pos_nums}")
    print(num_line)
