# AOC22 day 05
from copy import deepcopy


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def decode(data):
    parts = data.split("\n\n")
    raw_stacks = parts[0]
    raw_ops = parts[1]
    return decode_stacks(raw_stacks), decode_ops(raw_ops)


def decode_stacks(raw):
    lines = raw.splitlines()
    drawing_width = max(map(len, lines))
    stack_count = (drawing_width + 1) // 4
    stacks = []
    for i in range(stack_count):
        stacks.append([])
    for i in range(stack_count):
        for line in range(len(lines)-2, -1, -1):
            if len(lines[line]) >= i*4+1:
                c = lines[line][i*4+1]
                if c != ' ':
                    stacks[i].append(c)
                else:
                    break
    return stacks


def decode_ops(raw):
    ops = []
    for line in raw.splitlines():
        items = line.split(' ')
        ops.append((int(items[1]), int(items[3]), int(items[5])))
    return ops


def move_stacks(stacks, ops):
    for count, source, dest in ops:
        for i in range(count):
            stacks[dest-1].append(stacks[source-1].pop())


def move_stacks2(stacks, ops):
    for count, source, dest in ops:
        temp = stacks[source-1][-count:]
        stacks[source-1] = stacks[source-1][:-count]
        stacks[dest-1].extend(temp)


def get_top(stacks):
    top = "".join(stack[-1] for stack in stacks)
    return top


def run():
    data = load_data("Day05.txt")
    stacks, ops = decode(data)
    stacks2 = deepcopy(stacks)
    move_stacks(stacks, ops)
    print(get_top(stacks))
    #VCTFTJQCG
    move_stacks2(stacks2, ops)
    print(get_top(stacks2))
    #GCFGLDNJZ


if __name__ == "__main__":
    run()