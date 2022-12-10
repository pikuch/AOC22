# AOC22 day 06
def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def find_distinct(data, n):
    for i in range(len(data)):
        if len(set(data[max(i-n, 0):i])) == n:
            return i


def run():
    data = load_data("Day06.txt")
    print(find_distinct(data, 4))
    #1282
    print(find_distinct(data, 14))
    #3513


if __name__ == "__main__":
    run()