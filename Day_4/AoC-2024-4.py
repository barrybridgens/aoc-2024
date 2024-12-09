# Advent of Code 2024
# Day 4
# Problems 1 and 2
# Barry Bridgens - barry@bridgens.me.uk

max_x = 0
max_y = 0
total = 0

left = right = up = down = left_up = right_up = left_down = right_down = False

grid = []

def check_left(x , y):
    if ((grid[x][y] == 'X') and (grid[x - 1][y] == 'M') and (grid[x - 2][y] == 'A') and (grid[x - 3][y] == 'S')):
        ret = 1
    else:
        ret = 0
    return(ret)

def check_right(x , y):
    if ((grid[x][y] == 'X') and (grid[x + 1][y] == 'M') and (grid[x + 2][y] == 'A') and (grid[x + 3][y] == 'S')):
        ret = 1
    else:
        ret = 0
    return(ret)

def check_up(x , y):
    if ((grid[x][y] == 'X') and (grid[x][y - 1] == 'M') and (grid[x][y - 2] == 'A') and (grid[x][y - 3] == 'S')):
        ret = 1
    else:
        ret = 0
    return(ret)

def check_down(x , y):
    if ((grid[x][y] == 'X') and (grid[x][y + 1] == 'M') and (grid[x][y + 2] == 'A') and (grid[x][y + 3] == 'S')):
        ret = 1
    else:
        ret = 0
    return(ret)

def check_left_up(x , y):
    if ((grid[x][y] == 'X') and (grid[x - 1][y - 1] == 'M') and (grid[x - 2][y - 2] == 'A') and (grid[x - 3][y - 3] == 'S')):
        ret = 1
    else:
        ret = 0
    return(ret)

def check_left_down(x , y):
    if ((grid[x][y] == 'X') and (grid[x - 1][y + 1] == 'M') and (grid[x - 2][y + 2] == 'A') and (grid[x - 3][y + 3] == 'S')):
        ret = 1
    else:
        ret = 0
    return(ret)

def check_right_up(x , y):
    if ((grid[x][y] == 'X') and (grid[x + 1][y - 1] == 'M') and (grid[x + 2][y - 2] == 'A') and (grid[x + 3][y - 3] == 'S')):
        ret = 1
    else:
        ret = 0
    return(ret)

def check_right_down(x , y):
    if ((grid[x][y] == 'X') and (grid[x + 1][y + 1] == 'M') and (grid[x + 2][y + 2] == 'A') and (grid[x + 3][y + 3] == 'S')):
        ret = 1
    else:
        ret = 0
    return(ret)

if __name__ == "__main__":

    with open('AoC-2024-4.dat', 'r') as file:
        for line in file:
            max_x = len(line.strip())
            grid.append(line.strip())
            max_y = max_y + 1

        print(max_x, max_y)

        # print(grid)

        for x in range(max_x):
            for y in range(max_y):
                print(x, y)
                # calculate valid directions
                if (x >= 3):
                    left = True
                    if (y >= 3):
                        left_up = True
                    else:
                        left_up = False
                    if (y < (max_y - 3)):
                        left_down = True
                    else:
                        left_down = False
                else:
                    left = False
                    left_up = False
                    left_down = False
                if (x < (max_x - 3)):
                    right = True
                    if (y >= 3):
                        right_up = True
                    else:
                        right_up = False
                    if (y < (max_y - 3)):
                        right_down = True
                    else:
                        right_down = False
                else:
                    right = False
                    right_up = False
                    right_down = False
                if (y >= 3):
                    up = True
                else:
                    up = False
                if (y < (max_y - 3)):
                    down = True
                else:
                    down = False
                        
                if (left):
                    total = total + check_left(x, y)
                if (right):
                    total = total + check_right(x, y)
                if (up):
                    total = total + check_up(x, y)
                if (down):
                    total = total + check_down(x, y)
                if (left_up):
                    total = total + check_left_up(x, y)
                if (left_down):
                    total = total + check_left_down(x, y)
                if (right_up):
                    total = total + check_right_up(x, y)
                if (right_down):
                    total = total + check_right_down(x, y)
    print(total)
    
        
            
