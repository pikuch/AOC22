# AOC22 day 01
def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def make_list(data):
    numbers = []
    for items in data.split("\n\n"):
        total = 0
        elements = items.split("\n")
        for element in elements:
            total += int(element)
        numbers.append(total)
    return numbers


def run():
    data = load_data("Day01.txt")
    elves = make_list(data)
    elves.sort()
    print(elves[-1])
    #68802
    print(sum(elves[-3:]))
    #205370


if __name__ == "__main__":
    run()