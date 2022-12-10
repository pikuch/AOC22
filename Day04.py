# AOC22 day 04
def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


class Rangex:
    def __init__(self, s):
        (self.low, self.high) = map(int, s.split("-"))

    def contains(self, other):
        return self.low <= other.low and self.high >= other.high

    def overlaps(self, other):
        return (other.low <= self.low <= other.high) or \
               (other.low <= self.high <= other.high) or \
               (self.low <= other.low <= self.high) or \
               (self.low <= other.high <= self.high)

    def __str__(self):
        return f"[{self.low}-{self.high}]"


def make_list(data):
    pairs = []
    for item in data.split("\n"):
        ranges = item.split(",")
        pairs.append(tuple(map(Rangex, ranges)))
    return pairs


def run():
    data = load_data("Day04.txt")
    pairs = make_list(data)
    print(sum(map(lambda rs: rs[0].contains(rs[1]) or rs[1].contains(rs[0]), pairs)))
    #431
    print(sum(map(lambda rs: rs[0].overlaps(rs[1]), pairs)))
    #823


if __name__ == "__main__":
    run()