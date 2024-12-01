def get_input():
    with open("01_input.txt", "r") as f:
        data = [[int(d) for d in line.split()] for line in f]
    return data


def main():
    data = get_input()
    # Make a list with the first element of each line and another one with the second
    data_left = []
    data_right = []
    for d in data:
        data_left.append(d[0])
        data_right.append(d[1])
    data_left.sort()
    data_right.sort()
    sum = 0
    for l, r in zip(data_left, data_right):
        sum += abs(l - r)

    print(sum)


if __name__ == "__main__":
    main()
