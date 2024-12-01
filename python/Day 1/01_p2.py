def get_input():
    with open("01_input.txt", "r") as f:
        data = [[int(d) for d in line.split()] for line in f]
    return data


def main():
    data = get_input()
    # Make a list with the first element of each line and another one with the second
    data_left = [d[0] for d in data]
    data_right = [d[1] for d in data]
    data_left.sort()
    data_right.sort()
    similarity = 0
    for l in data_left:
        similarity += data_right.count(l) * l
    print(similarity)


if __name__ == "__main__":
    main()
