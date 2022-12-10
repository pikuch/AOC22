# AOC22 day 02
def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def make_list(data):
    rounds = []
    for item in data.split("\n"):
        rounds.append(tuple(item.split(" ")))
    return rounds


def score1(pair):
    p1 = pair[0]
    p2 = pair[1]
    if p1 == "A":
        if p2 == "X":
            return 1 + 3
        elif p2 == "Y":
            return 2 + 6
        elif p2 == "Z":
            return 3 + 0
    elif p1 == "B":
        if p2 == "X":
            return 1 + 0
        elif p2 == "Y":
            return 2 + 3
        elif p2 == "Z":
            return 3 + 6
    elif p1 == "C":
        if p2 == "X":
            return 1 + 6
        elif p2 == "Y":
            return 2 + 0
        elif p2 == "Z":
            return 3 + 3


def score2(pair):
    p1 = pair[0]
    p2 = pair[1]
    if p1 == "A":
        if p2 == "X":
            return 3 + 0
        elif p2 == "Y":
            return 1 + 3
        elif p2 == "Z":
            return 2 + 6
    elif p1 == "B":
        if p2 == "X":
            return 1 + 0
        elif p2 == "Y":
            return 2 + 3
        elif p2 == "Z":
            return 3 + 6
    elif p1 == "C":
        if p2 == "X":
            return 2 + 0
        elif p2 == "Y":
            return 3 + 3
        elif p2 == "Z":
            return 1 + 6


def run():
    data = load_data("Day02.txt")
    pairs = make_list(data)
    print(sum(map(score1, pairs)))
    # 11666
    print(sum(map(score2, pairs)))
    # 12767


if __name__ == "__main__":
    run()