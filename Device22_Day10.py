# AOC22 device day 10
class Device22:
    def __init__(self):
        self.cycle = 1
        self.ops = []
        self.ptr = 0
        self.rx = 1
        self.signal = {}

    def load_signal(self, data):
        self.ops = [Op(line) for line in data.splitlines()]

    def draw(self):
        if abs(((self.cycle - 1) % 40) - self.rx) <= 1:
            print("#", end="")
        else:
            print(".", end="")
        if self.cycle % 40 == 0:
            print()

    def run(self):
        while self.ptr < len(self.ops):
            self.signal[self.cycle] = self.rx
            self.draw()
            current = self.ops[self.ptr]
            current.tick()
            if current.is_done():
                self.rx += current.arg
                self.ptr += 1

            self.cycle += 1

        return self.signal


class Op:
    def __init__(self, s):
        items = s.split(" ")
        self.val = items[0]
        if items[0] == "noop":
            self.arg = 0
            self.timer = 1
        elif items[0] == "addx":
            self.arg = int(items[1])
            self.timer = 2
        else:
            print(f"Bad data: {s}")
            exit(-1)

    def tick(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            print("Timer ticked below 0!")
            exit(-10)

    def is_done(self):
        return self.timer == 0
