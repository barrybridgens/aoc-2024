# Advent of Code 2024
# Day 2
# Problems 1 and 2
# Barry Bridgens - barry@bridgens.me.uk

def read_and_process_data():
    safe = 0
    with open('AoC-2024-2.dat', 'r') as file:
        for line in file:
            levels = list(map(int, line.split(' ')))
            safe_test = 0
            for skip_level in range(len(levels)):
                level_deltas = []
                reduced_levels = levels.copy()
                reduced_levels.pop(skip_level)
                for x in range(len(reduced_levels)):
                    if (x > 0):
                        level_deltas.append(reduced_levels[x] - reduced_levels[x - 1])
                safe_test = safe_test + process_deltas(level_deltas)
            if (safe_test > 0):
                    safe = safe + 1
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
