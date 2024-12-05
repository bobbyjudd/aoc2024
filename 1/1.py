# https://adventofcode.com/2024/day/1
import re
from typing import List


def part_1(left_list: List[int], right_list: List[int]) -> int:
    return sum([abs(left_list[i] - right_list[i]) for i in range(len(left_list))])


def part_2(left_list: List[int], right_list: List[int]) -> int:
    right_id_count_map = {}
    for id in right_list:
        if id not in right_id_count_map:
            right_id_count_map[id] = 0
        right_id_count_map[id] += 1

    return sum(
        [
            id * (right_id_count_map[id] if id in right_id_count_map else 0)
            for id in left_list
        ]
    )


def main():
    regex = re.compile(r"(\d+)\s+(\d+)")

    left_list, right_list = [], []
    with open("input.txt") as f:
        for l in f.readlines():
            m = regex.match(l)
            assert m is not None
            left_list.append(int(m.group(1)))
            right_list.append(int(m.group(2)))

    assert len(left_list) == len(right_list)

    left_list.sort()
    right_list.sort()

    print(f"Part 1: {part_1(left_list, right_list)}")
    print(f"Part 2: {part_2(left_list, right_list)}")


if __name__ == "__main__":
    main()
