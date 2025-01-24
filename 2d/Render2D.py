import math
from os.path import exists

import numpy as np


origin = (20,40)

a = 3.141592653589793
# a = int(np.pi/2)

def calc_x(x,y,t):
    return int((x * (np.cos(t))) - (y * (np.sin(t))))
def calc_y(x,y,t):
    return int((x * (np.sin(t))) + (y * (np.cos(t))))


def calc_slope(co1, co2):
    return [(co2[1] - co1[1]),(co2[0] - co1[0])]
def render():
    rows = 90
    cols = 45
    content = [["."] * cols for _ in range(rows)]

    # (x,y, char)
    grid = [(20,40, "*"), (calc_x(30,40, a), calc_y(30,40, a), "@"), (calc_x(30,50, a), calc_y(30,50, a),"O"),]
    slopes = []
    for i in range(len(grid)):
        for k in range(len(grid)):
            if not k <= i :
                slopes.append((grid[i],grid[k],calc_slope(grid[i], grid[k])))

    print(slopes)

    for (y, x, c) in grid: content[x][y] = c
    width = len(str(max(rows, cols) - 1))
    content_line = "# | values |"

    dashes = "-".join("-" * width for _ in range(cols))
    frame_line = content_line.replace("values", dashes)
    frame_line = frame_line.replace("#", " " * width)
    frame_line = frame_line.replace("| ", "+-").replace(" |", "-+")

    print(frame_line)
    for i, row in enumerate(reversed(content), 1):
        values = " ".join(f"{v:{width}s}" for v in row)
        line = content_line.replace("values", values)
        line = line.replace("#", f"{rows - i:{width}d}")
        print(line)
    print(frame_line)

    num_line = content_line.replace("|", " ")
    num_line = num_line.replace("#", " " * width)
    col_nums = " ".join(f"{i:<{width}d}" for i in range(cols))
    num_line = num_line.replace("values", col_nums)
    print(num_line)