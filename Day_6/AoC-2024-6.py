# Advent of Code 2024
# Day 6
# Problems 1 and 2
# Barry Bridgens - barry@bridgens.me.uk

grid = []
max_x = 0
max_y = 0

up = [0, -1]
down = [0, 1]
left = [-1, 0]
right = [1, 0]

position = [73, 75]
direction = up

total = 0

def display():
    for y in range(max_y):
        print(grid[y])
    print("")

def in_front_of(p, d):
    new_p = move(p, d)
    if ((new_p[0] >= 0) and (new_p[0] < max_x) and (new_p[1] >= 0) and (new_p[1] < max_y)):
        return(grid[new_p[1]][new_p[0]])
    else:
        # Out of bounds
        return('O')

def move(p, d):
    new_p = p.copy()
    new_p[0] = new_p[0] + d[0]
    new_p[1] = new_p[1] + d[1]
    return(new_p)


def turn(d):
    ret = up
    if (d == up):
        ret = right
    else:
        if (d == right):
            ret = down
        else:
            if (d == down):
                ret = left
            else:
                if (d == left):
                    ret = up
    return(ret)
        
        
if __name__ == "__main__":

    with open('AoC-2024-6.dat', 'r') as file:
        for line in file:
            max_x = len(line.strip())
            grid.append(line.strip())
            max_y = max_y + 1

        print(max_x, max_y)

        loops = 0
        
        while (loops < 100000):
            loops = loops + 1
            print("position", position)
            if ((in_front_of(position, direction) == '.') or (in_front_of(position, direction) == 'X')):
                # Move
                position = move(position, direction)
                l = grid[position[1]]
                l = list(l)
                l[position[0]] = 'X'
                grid[position[1]] = "".join(l)
            else:
                if (in_front_of(position, direction) == '#'):
                    direction = turn(direction)
                else:
                    if (in_front_of(position, direction) == 'O'):
                        break
            display()

        print("Counting...")
        for x in range(max_x):
            for y in range(max_y):
                if (grid[x][y] == 'X'):
                    total = total + 1
        print(total)
