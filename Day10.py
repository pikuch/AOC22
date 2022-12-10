# AOC22 day 10
from Device22_Day10 import Device22


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day10.txt")
    device = Device22()
    device.load_signal(data)
    signal = device.run()
    result1 = sum([i * signal[i] for i in range(20, 221, 40)])
    print(f"signal strength = {result1}")
    #11820
    #EPJBRKAH


if __name__ == "__main__":
    run()
