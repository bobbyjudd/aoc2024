# https://adventofcode.com/2024/day/1
import re

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

print('Part 1')
print(sum([abs(left_list[i] - right_list[i]) for i in range(len(left_list))]))

# https://adventofcode.com/2024/day/1#part2

right_id_count_map = {}
for id in right_list:
    if id not in right_id_count_map:
        right_id_count_map[id] = 0
    right_id_count_map[id] += 1

print('Part 2')
print(
    sum(
        [
            id * (right_id_count_map[id] if id in right_id_count_map else 0)
            for id in left_list
        ]
    )
)
