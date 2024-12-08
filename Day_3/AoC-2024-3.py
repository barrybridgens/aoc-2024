# Advent of Code 2024
# Day 3
# Problems 1 and 2
# Barry Bridgens - barry@bridgens.me.uk

import re

total = 0
instructions = []

with open("AoC-2024-3.dat") as f:
    data = f.read()

    iter = re.finditer(r"mul\([0-9]+\,[0-9]+\)", data)
    indices = [m.span(0) for m in iter]

    print(len(indices))

    for i in indices:
        instructions.append(data[i[0]:i[1]])

    for i in instructions:
        print(i)
        iter2 = re.finditer(r"[0-9]+", i)
        indices2 = [m.span(0) for m in iter2]

        n1 = int(i[int(indices2[0][0]): int(indices2[0][1])])
        print(n1)
        n2 = int(i[int(indices2[1][0]): int(indices2[1][1])])
        print(n2)

        total = total + (n1 * n2)

print(total)



