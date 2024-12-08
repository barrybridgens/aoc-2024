# Advent of Code 2024
# Day 3
# Problems 1 and 2
# Barry Bridgens - barry@bridgens.me.uk

instruction = ''
valid_instruction = False
n1_flag = False
n2_flag = False
n1_string = ""
n2_string = ""
n1 = 0
n2 = 0
total = 0

with open("AoC-2024-3.dat") as f:
    while True:
        c = f.read(1)
        if not c:
            print("End of file")
            break
        
        # Look for the start of a mul
        if (c == 'm'):
            valid_instruction = True
            c = f.read(1)
            if not c:
                print("End of file")
                break
        if (valid_instruction):
            if (c != 'u'):
                valid_instruction = False
            else:
                c = f.read(1)
                if not c:
                    print("End of file")
                    break
                if (c != "l"):
                    valid_instruction = False
                else:
                    c = f.read(1)
                    if not c:
                        print("End of file")
                        break
                    if (c != '('):
                        valid_instruction = False
                    else:
                        print("Found start of instruction")
                        # Process n1
                        c = f.read(1)
                        if not c:
                            print("End of file")
                            break
                        if (c.isnumeric() == False):
                            valid_instruction = False
                        else:
                            n1_flag = True
                            n1_string = n1_string + c
                            print("Found start of n1")
                            while (c.isnumeric() and n1_flag):
                                c = f.read(1)
                                if not c:
                                    print("End of file")
                                    break
                                if (c.isnumeric() == False):
                                    if (c == ','):
                                        n1 = int(n1_string)
                                        n1_string = ""
                                        n1_flag = False
                                        n2_flag = True
                                        print("   n1 is ", n1)
                                    else:
                                        valid_instruction = False
                                        n1_flag = False
                                        n1_string = ""
                                else:
                                    n1_string = n1_string + c
                            c = f.read(1)
                            if not c:
                                print("End of file")
                                break
                            if (c.isnumeric() == False):
                                valid_instruction = False
                                n2_flag = False
                            else:
                                n2_string = n2_string + c
                                print("Found start of n2")
                                while (c.isnumeric() and n2_flag):
                                    c = f.read(1)
                                    if not c:
                                        print("End of file")
                                        break
                                    if (c.isnumeric() == False):
                                        if (c == ')'):
                                            n2 = int(n2_string)
                                            n2_string = ""
                                            n2_flag = False
                                            print("   n2 is ", n2)
                                            print("Found valid instruction")
                                            total = total + (n1 * n2)
                                            valid_instruction = False
                                        else:
                                            valid_instruction = False
                                            n2_flag = False
                                            n2_string = ""
                                    else:
                                        n2_string = n2_string + c

                                        
print(total)



