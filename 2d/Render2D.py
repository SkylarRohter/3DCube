import math
from os.path import exists
import sys

import numpy as np

n = len(sys.argv)


origin = (0,0)

a = (np.pi)
op = float(sys.argv[1])
a*=op
print("\nA:  ", a)

def calc_x(x,y,t):
    return int(np.abs(round((x * (np.cos(t))) - (y * (np.sin(t))), 1)))
def calc_y(x,y,t):
    return int(np.abs(round((x * (np.sin(t))) + (y * (np.cos(t))), 1)))
print("\n\n\n")
print((calc_x(6,3,a), calc_y(6,3,a)))
print("\n\n\n")
def calc_slope(co1, co2):
    return [(co2[1] - co1[1]),(co2[0] - co1[0])]
def render():
    rows = 30
    cols = 20
    q_row=int(cols/2)
    q_col=int(rows/2)
    quad1, quad2, quad3, quad4 = [["."] * cols for _ in range(q_row)], [["."] * cols for _ in range(q_row)], [["."] * cols for _ in range(q_row)], [["."] * cols for _ in range(q_row)]
    content = [["."] * cols for _ in range(rows)]

    # (x,y, char)
    grid = [(0,0, "*"), (calc_x(6,0, a), calc_y(6,0, a), "@"), (calc_x(6,3, a), calc_y(6,3, a),"O"), (6,-3, "&")]
    slopes = []
    for i in range(len(grid)):
        for k in range(len(grid)):
            if not k <= i :
                slopes.append((grid[i],grid[k],calc_slope(grid[i], grid[k])))

    print(slopes)

    width = len(str(max(rows, cols) - 1))
    content_line = "# ] values ]"
    # quad_line =  "# | quad + quad |"

    quad_dashes = "-".join("-" * width for _ in range(int(cols/2)))
    dashes = quad_dashes + quad_dashes + "-"

    # set the x and y axis

    # for(y,x) goes to content[x][y]. This runs (Large to small)
    for (x, y, c) in grid:
        if x >=0 and y >= 0: #quad 1 (S to L on X) (L to S on Y)
            quad1[x][y] = c
        elif x < 0 and y <= 0: #quad 3 (L to S on X) (S to L on Y)
            quad3[np.abs(x)][np.abs(y)] = c
        elif x >= 0 > y: # quad 4 (S to L on X) (S to L on Y)
            quad4[x][np.abs(y)] = c
        elif x < 0 > y: # quad 2 (L to S on X) (L to S on Y)
            quad2[np.abs(x)][y] = c

    print(quad4[6][3])
    # dashes = "-".join("-" * width for _ in range(cols))
    frame_line = content_line.replace("values", dashes)
    frame_line = frame_line.replace("#", " " * width)
    frame_line = frame_line.replace("] ", "+-").replace(" ]", "-+")

    print(frame_line)

    y_mid = int(rows/2)
    x_mid = int(cols/2)
    for y in range(rows):
        values = ""
        for x in range(cols):
            if y <= y_mid:
                if y < y_mid and x < x_mid:
                    '''Quad 2'''
                    values = values + "*" + " "*width
                elif y == y_mid and x >= x_mid:
                    values = values + "+"
                elif y < y_mid and x >= x_mid:
                    values = values + "o" + " "*width
                    '''Quad 1'''

            elif y >= y_mid:
                if y == y_mid and x < x_mid:
                    values = values + "-" + "-"*width
                elif x < x_mid:
                    values = values + f"{quad3[x-x_mid][y-y_mid]}{" " * width}"
                    '''Quad 3'''

                elif x >= x_mid and y > y_mid:
                    '''Quad 4'''
                    if x == x_mid and quad4[x-x_mid][y-y_mid] == '.':
                        values = values + f"|{" "*width}"
                        '''nothing'''
                    else:
                        '''nothing'''
                        values = values + f"{quad4[x-x_mid][y-y_mid]}{" " * width}"
        quad_line = content_line.replace("values", values)
        if y == y_mid:
            quad_line = quad_line.replace(" ] ", "  +")
        quad_line = quad_line.replace(" ] ", "  |").replace("]", "|")
        quad_line = quad_line.replace(" ] ", "  |")
        print(quad_line)
    print(frame_line)
    # for i, row in enumerate(reversed(content), 1):
    #     iterator = 0
    #
    #     if i != rows/2:
    #         quad = " "
    #         for col in range(len(row)):
    #             v = row[col]
    #
    #             if  iterator < int(cols/2) or iterator > int(cols/2):
    #                 quad = quad.join(f"{v:{width}s}")
    #             else:
    #                 quad = quad.join("|")
    #         # values = " ".join(f"{v:{width}s}" for v in row)
    #             iterator += 1
    #
    #         line = content_line.replace("values", quad)
    #         line = line.replace("#", f"{rows - i:{width}d}")
    #     else:
    #         line = quad_line.replace("quad", quad_dashes)
    #         line = line.replace("| ", "+").replace(" |", "+")
    #         line = line.replace(" + ", "--+")
    #         line = line.replace("#", f"{rows - i:{width}d}")
    #
    #     print(line)
    # print(frame_line)
    #
    # num_line = content_line.replace("|", " ")
    # num_line = num_line.replace("#", " " * width)
    # col_nums = " ".join(f"{i:<{width}d}" for i in range(cols))
    # num_line = num_line.replace("values", col_nums)
    # print(num_line)