# Advent of Code 2024
# Day 5
# Problems 1 and 2
# Barry Bridgens - barry@bridgens.me.uk

total = 0
rules = []
pages = []

if __name__ == "__main__":

    with open('AoC-2024-5.dat', 'r') as file:
        for line in file:

            if ('|' in line):
                r = (line.strip().split('|'))
                rules.append(list(map(int, r)))
            else:
                if (line.strip() != ""):
                    p = (line.strip().split(','))
                    pages.append(list(map(int, p)))

    # print(rules)
    # print(pages)

    for p in pages:
        print(p)
        ok = True
        for r in rules:
            if ((r[0] in p) and (r[1] in p)):
                # Rule applies
                if ((p.index(r[0])) > (p.index(r[1]))):
                    # Rule failes
                    ok = False
        if (ok):
            middle = p[int((len(p) -1) / 2)]
            print("Middle = ", middle)
            total = total + middle

    print(total)
