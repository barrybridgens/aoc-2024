# Advent of Code 2024
# Day 2
# Problems 1 and 2
# Barry Bridgens - barry@bridgens.me.uk

def read_and_process_data():
    safe = 0
    with open('AoC-2024-2.dat', 'r') as file:
        for line in file:
            levels = list(map(int, line.split(' ')))
            level_deltas = []
            for x in range(len(levels)):
                if (x > 0):
                    level_deltas.append(levels[x] - levels[x - 1])
            safe = safe + process_deltas(level_deltas)
            print(level_deltas)
        print(safe)
            
def process_deltas(deltas):
    max = 0
    min = 99999
    pos = 0
    neg = 0
    ret = 0
    for delta in deltas:
        if (abs(delta) > max):
            max = abs(delta)
        if (abs(delta) < min):
            min = abs(delta)
        if (delta > 0):
            pos = pos + 1
        if (delta < 0):
            neg = neg + 1
    if (((min > 0) and (max < 4)) and ((pos == 0) or (neg == 0))):
        ret = 1
    return(ret)
    
            
if __name__ == "__main__":
    read_and_process_data()
