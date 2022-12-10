# AOC22 day 07
class Node:
    def __init__(self, name, is_file, parent):
        self.name = name
        self.is_file = is_file
        self.parent = parent
        self.size = None
        self.contents = []

    def get_size(self):
        if self.is_file:
            return self.size
        else:
            if self.size is None:
                self.size = sum([x.get_size() for x in self.contents])
            return self.size

    def get_child(self, name):
        for c in self.contents:
            if c.name == name:
                return c

    def __str__(self):
        par = self.parent.name if self.parent is not None else "-"
        children = ','.join([x.name for x in self.contents])
        return f"{self.name} size:{self.size} parent:{par} [{children}]"


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def make_list(data):
    return [tuple(line.split(' ')) for line in data.splitlines()]


def make_tree(commands):
    root = Node("/", False, None)
    current = root
    for c in commands:
        if c[0] == "$":
            if c[1] == "cd":
                if c[2] == "/":
                    current = root
                elif c[2] == "..":
                    current = current.parent
                else:
                    current = current.get_child(c[2])
            elif c[1] != "ls":
                print(f"bad data: {c}")
        elif c[0] == "dir":
            directory = Node(c[1], False, current)
            current.contents.append(directory)
        else:
            file = Node(c[1], True, current)
            file.size = int(c[0])
            current.contents.append(file)
    return root


def calculate(limit, to_free, tree):
    sum_sizes = 0
    dir_size = tree.size
    to_check = [tree]
    while len(to_check):
        current = to_check.pop()
        if not current.is_file:
            if current.size <= limit:
                sum_sizes += current.size
            if dir_size > current.size >= to_free:
                dir_size = current.size
            to_check.extend(current.contents)
    return sum_sizes, dir_size


def run():
    data = load_data("Day07.txt")
    commands = make_list(data)
    tree = make_tree(commands)
    tree.get_size()
    sum_dirs_at_most, smallest_at_least = calculate(100_000, tree.get_size()-40_000_000, tree)
    print(sum_dirs_at_most)
    #1642503
    print(smallest_at_least)
    #6999588


if __name__ == "__main__":
    run()