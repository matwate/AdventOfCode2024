def get_input():
    with open("02_input.txt", "r") as f:
        data = [[int(d) for d in line.split()] for line in f]
    return data


def is_safe(data: list):
    ascending = all(data[i] >= data[i + 1] for i in range(len(data) - 1))
    descending = all(data[i] <= data[i + 1] for i in range(len(data) - 1))
    max_diff = all(
        abs(data[i] - data[i + 1]) in [1, 2, 3] for i in range(len(data) - 1)
    )
    return (ascending or descending) and max_diff


def main():
    sum = 0
    for line in get_input():
        if is_safe(line):
            sum += 1
        else:
            data_without = []
            for i in range(len(line)):
                data_without.append(line[:i] + line[i + 1 :])
            for data in data_without:
                if is_safe(data):
                    sum += 1
                    break

    print(sum)


if __name__ == "__main__":
    main()
