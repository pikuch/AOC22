# AOC22 day 03
def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def make_list(data):
    return data.split("\n")


def char_value(c):
    if ord(c) > ord('Z'):
        return ord(c)-ord('a')+1
    else:
        return ord(c)-ord('A')+27


def part1(bp):
    s1 = set(bp[:len(bp)//2])
    s2 = set(bp[len(bp)//2:])
    ss = s1.intersection(s2)
    c = ss.pop()
    return char_value(c)


def part2(bps):
    total = 0
    for i in range(len(bps) // 3):
        group = bps[i * 3:i * 3 + 3]
        ss = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        c = ss.pop()
        total += char_value(c)
    return total


def run():
    data = load_data("Day03.txt")
    backpacks = make_list(data)
    print(sum(map(part1, backpacks)))
    #7691
    print(part2(backpacks))
    #2508


if __name__ == "__main__":
    run()