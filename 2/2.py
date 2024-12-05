# https://adventofcode.com/2024/day/2
from typing import List


def report_is_safe(report: List[int]) -> bool:
    level_diffs = [report[i - 1] - report[i] for i in range(1, len(report))]
    safe, negative = True, level_diffs[0] < 0
    for l in level_diffs:
        if (
            (abs(l) < 1 or 3 < abs(l))
            or (negative and l > 0)
            or (not negative and l < 0)
        ):
            safe = False
            break
    return safe


def part_1(reports: List[List[int]]):
    safe_reports = 0
    for levels in reports:
        safe_reports += 1 if report_is_safe(levels) else 0
    return safe_reports


def part_2(reports: List[List[int]]):
    safe_reports = 0
    for levels in reports:
        if report_is_safe(levels):
            safe_reports += 1
            continue
        for removed_index in range(len(levels)):
            dampened_levels = levels[:removed_index] + levels[removed_index + 1 :]
            if report_is_safe(dampened_levels):
                safe_reports += 1
                break
    return safe_reports


def main():
    reports = []
    with open("input.txt") as f:
        for l in f.readlines():
            reports.append([int(level) for level in l.split(" ")])
    print(f"Part 1: {part_1(reports)}")
    print(f"Part 2: {part_2(reports)}")


if __name__ == "__main__":
    main()
