# Advent of Code 2024
# Day 5
# Problems 1 and 2
# Barry Bridgens - barry@bridgens.me.uk

from itertools import permutations

ok_total = 0
nok_total =0
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
        pp = p.copy()
        for r in rules:
            if ((r[0] in p) and (r[1] in p)):
                # Rule applies
                r0 = pp.index(r[0])
                r1 = pp.index(r[1])
                if (r0 > r1):
                    # Rule fails
                    ok = False

        if (ok == False):
            perm = permutations(pp)
            for pt in perm:
                p_ok = True
                for r in rules:
                    if ((r[0] in pt) and (r[1] in pt)):
                        # Rule applies
                        r0 = pt.index(r[0])
                        r1 = pt.index(r[1])
                        if (r0 > r1):
                            p_ok = False
                if (p_ok):
                    pp = list(pt).copy()
                    print("-->", pt)
                    break

        middle = pp[int((len(p) -1) / 2)]
        if (ok):
            ok_total = ok_total + middle
        else:
            nok_total = nok_total + middle

    print(ok_total)
    print(nok_total)
