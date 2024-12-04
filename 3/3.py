# https://adventofcode.com/2024/day/3

import re


def part_1(text: str) -> int:
    regex = re.compile(r"mul\((\d+),(\d+)\)")
    return sum([int(x) * int(y) for x, y in regex.findall(text)])


def part_2(text: str) -> int:
    do = True
    total = 0
    regex = re.compile(r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))")
    for x, y, dont_str, do_str in regex.findall(text):
        if do_str:
            do = True
        elif dont_str:
            do = False
        elif do:
            total += int(x) * int(y)
    return total


def main():
    with open("input.txt") as f:
        text = "".join(f.readlines())
    print(f"Part 1: {part_1(text)}")
    print(f"Part 2: {part_2(text)}")


if __name__ == "__main__":
    main()
