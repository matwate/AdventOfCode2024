import time
import os


def get_input():
    with open("03_input.txt") as f:
        return f.read().strip()


def parse_multiplications(data):
    # Will parse the string finding mul(1-3digits, 1-3digits) and keep a running sum

    cur = ""
    number = ""
    res = 0
    valid = True
    for t in data:
        match t:
            case "m":
                cur = cur + t
            case "u":
                if "m" in cur:
                    cur = cur + t
                else:
                    cur = ""
            case "l":
                if cur == "mu":
                    cur = cur + t
                else:
                    cur = ""
            case "(":
                if cur == "mul":
                    cur = cur + t
                else:
                    cur = ""
            case ")":
                if number_stack_valid(number) and "mul(" in cur:
                    cur = cur + number + t
                    if number_stack_valid(number) and "mul(" in cur and ")" in cur:
                        if (
                            len(number) > 3
                            and len(number) < 8
                            and number.count(",") == 1
                        ):
                            valid = True
                        else:
                            valid = False
                        a, b = number.split(",")
                        print(cur, number)
                        res += int(a) * int(b)
                        cur = ""
                        number = ""
                    else:
                        cur = ""
                        number = ""
                else:
                    cur = ""
                    number = ""
            case _:
                if t in "1234567890,":
                    number = number + t
                    if number_stack_valid(number):
                        if (
                            len(number) > 3
                            and len(number) < 8
                            and number.count(",") == 1
                        ):
                            valid = True
                        if not valid:
                            cur = cur + number[:-1]
                    else:
                        valid = False
                else:
                    cur = ""
                    number = ""

    return res

import re

def parse_multiplications_re(data):
    multiply = True  # Flag to track whether to multiply
    total = 0
    idx = 0
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", re.IGNORECASE)

    while idx < len(data):
        match = pattern.search(data, idx)
        if not match:
            break
        token = match.group(0).lower()
        if token == "do()":
            multiply = True
        elif token == "don't()":
            multiply = False
        elif "mul" in token and multiply:
            x, y = match.groups()
            total += int(x) * int(y)
        idx = match.end()
    return total


def number_stack_valid(data):
    if data.count(",") > 1:
        return False
    split = data.split(",")
    if len(split) != 2:
        return False
    a, b = split
    if len(a) in [1, 2, 3] and len(b) in [1, 2, 3]:
        return True
    else:
        return False


def main():
    data = get_input()
    cur = parse_multiplications_re(data)
    print(cur)


if __name__ == "__main__":
    main()
