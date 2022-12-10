# AOC22 day 08
def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def make_grid(data):
    grid = []
    for line in data.splitlines():
        row = []
        for char in line:
            row.append(int(char))
        grid.append(row)
    return grid


def count_visible(grid):
    tree_count = 0
    width = len(grid[0])
    height = len(grid)
    for row in range(height):
        for col in range(width):
            current = grid[row][col]
            visible = False
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                in_direction = True
                r = row
                c = col
                while True:
                    r += dr
                    c += dc
                    if r < 0 or r >= height or c < 0 or c >= width:
                        break
                    if grid[r][c] >= current:
                        in_direction = False
                        break
                if in_direction:
                    visible = True
                    break
            if visible:
                tree_count += 1
    return tree_count


def highest_scenic_score(grid):
    scenic_score = 0
    width = len(grid[0])
    height = len(grid)
    for row in range(height):
        for col in range(width):
            current = grid[row][col]
            scores = []
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                score_dir = 0
                r = row
                c = col
                while True:
                    r += dr
                    c += dc
                    if r < 0 or r >= height or c < 0 or c >= width:
                        break
                    score_dir += 1
                    if grid[r][c] >= current:
                        break
                scores.append(score_dir)
            mult = scores[0] * scores[1] * scores[2] * scores[3]
            if scenic_score < mult:
                scenic_score = mult
    return scenic_score


def run():
    data = load_data("Day08.txt")
    grid = make_grid(data)
    print(count_visible(grid))
    #1792
    print(highest_scenic_score(grid))
    #334880


if __name__ == "__main__":
    run()
