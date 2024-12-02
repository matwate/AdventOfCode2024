def get_input():
    with open("02_input.txt", "r") as f:
        data = [[int(d) for d in line.split()] for line in f]
    return data


def is_ascending_or_descending(data):

    is_descending = all(data[i] >= data[i + 1] for i in range(len(data) - 1))

    return all(data[i] <= data[i + 1] for i in range(len(data) - 1)) or is_descending


def calculate_differences(data):
    return all(abs(data[i] - data[i + 1]) in [1, 2, 3] for i in range(len(data) - 1))


def main():
    sum = 0
    for line in get_input():
        # Check if its ascending or descending and also check if the difference of the two is between 1 and 3
        if is_ascending_or_descending(line) and calculate_differences(line):
            sum += 1
    print(sum)


if __name__ == "__main__":
    main()
