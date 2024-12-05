# https://adventofcode.com/2024/day/4

from typing import List


def get_xmas_count(i: int, j: int, text: List[str]):
    if text[i][j] != "X":
        return 0
    count = 0
    left_ok = j > 2
    right_ok = j + 3 < len(text[i])
    up_ok = i > 2
    down_ok = i + 3 < len(text)
    # left
    if left_ok and text[i][j - 1 : j] == "SAM":
        count += 1
    # right
    if right_ok and text[i][j + 1 : j + 4] == "MAS":
        count += 1
    # up
    if up_ok:
        if f"{text[i-1][j]}{text[i-2][j]}{text[i-3][j]}" == "MAS":
            count += 1
    # down
    if down_ok:
        if f"{text[i+1][j]}{text[i+2][j]}{text[i+3][j]}" == "MAS":
            count += 1
    # diagonals
    # top-left
    if up_ok and left_ok:
        if f"{text[i-1][j-1]}{text[i-2][j-2]}{text[i-3][j-3]}" == "MAS":
            count += 1
    # top-right
    if up_ok and right_ok:
        if f"{text[i-1][j+1]}{text[i-2][j+2]}{text[i-3][j+3]}" == "MAS":
            count += 1
    # bottom-left
    if down_ok and left_ok:
        if f"{text[i+1][j-1]}{text[i+2][j-2]}{text[i+3][j-3]}" == "MAS":
            count += 1
    # bottom-right
    if down_ok and right_ok:
        if f"{text[i+1][j+1]}{text[i+2][j+2]}{text[i+3][j+3]}" == "MAS":
            count += 1
    return count


MS_SET = frozenset(["M", "S"])


def get_x_mas_count(i: int, j: int, text: List[str]) -> int:
    if text[i][j] != "A":
        return 0
    # diagonals
    # top-left to bottom-right
    tl_br = set([text[i - 1][j - 1], text[i + 1][j + 1]])

    # top-right bottom-left
    tr_bl = set([text[i - 1][j + 1], text[i + 1][j - 1]])

    if tl_br == MS_SET and tr_bl == MS_SET:
        return 1
    return 0


def part_1(text: List[str]) -> int:
    count = 0
    for i in range(len(text)):
        for j in range(len(text[i])):
            count += get_xmas_count(i, j, text)
    return count


def part_2(text: List[str]) -> int:
    count = 0
    for i in range(1, len(text) - 1):
        for j in range(1, len(text[i]) - 1):
            count += get_x_mas_count(i, j, text)
    return count


def main():
    with open("input.txt") as f:
        text = [l.replace("\n", "") for l in f.readlines()]

    print(f"Part 1: {part_1(text)}")
    print(f"Part 2: {part_2(text)}")


if __name__ == "__main__":
    main()
