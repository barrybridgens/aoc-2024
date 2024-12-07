# Advent of Code 2024
# Problems 1 and 2
# Barry Bridgens - barry@bridgens.me.uk

list_1 = []
list_2 = []

def read_data():
    with open('AoC-2024-1.dat', 'r') as file:
        for line in file:
            # print(line.strip())
            while '  ' in line: line = line.replace('  ', ' ')
            a, b = map(int, line.split(' '))
            list_1.append(a)
            list_2.append(b)
    print(len(list_1))
    print(len(list_2))

def process_data():
    total = 0
    list_1.sort()
    list_2.sort()
    for x in range(len(list_1)):
        a = list_1[x]
        b = list_2[x]
        total = total + abs(a - b)
    print(total)

    total = 0
    for x in list_1:
        count = 0
        for y in list_2:
            if (y == x):
                count = count + 1
        total = total + (x * count)
    print(total)

if __name__ == "__main__":
    read_data()
    process_data()
