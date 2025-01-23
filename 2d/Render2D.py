import numpy as np

def render():
    rows = 90
    cols = 45
    content = [["."] * cols for _ in range(rows)]

    # (x,y, char)
    grid = [(20,40, "O"), (30,40, "O"), (30,50,"O"),]
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