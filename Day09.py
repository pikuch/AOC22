# AOC22 day 09
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def move_after(self, other):
        if abs(other.x - self.x) > 1 or abs(other.y - self.y) > 1:
            if abs(other.x - self.x) == 0:
                if other.y > self.y:
                    self.y += 1
                else:
                    self.y -= 1
            elif abs(other.y - self.y) == 0:
                if other.x > self.x:
                    self.x += 1
                else:
                    self.x -= 1
            else:
                if other.x > self.x:
                    self.x += 1
                else:
                    self.x -= 1
                if other.y > self.y:
                    self.y += 1
                else:
                    self.y -= 1


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def make_list(data):
    deltas = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    moves = []
    for line in data.splitlines():
        direction, distance = line.split(' ')
        for i in range(int(distance)):
            moves.append(deltas[direction])
    return moves


def count_visited(moves, n):
    visited = set()
    rope = [Point(0, 0) for i in range(n)]

    for dx, dy in moves:
        rope[0].move_by(dx, dy)
        for i in range(len(rope)-1):
            rope[i+1].move_after(rope[i])
        visited.add((rope[-1].x, rope[-1].y))
    return len(visited)


def run():
    data = load_data("Day09.txt")
    moves = make_list(data)
    print(count_visited(moves, 2))
    #6037
    print(count_visited(moves, 10))
    #2485


if __name__ == "__main__":
    run()
