data = [0]*30000
index = 0
def bf_add(x):
    global index
    data[index] = (data[index] + x) % 256
def bf_sub(x):
    global index
    data[index] = (data[index] - x) % 256
def bf_clear():
    global index
    data[index] = 0
def bf_output():
    global index
    print(chr(data[index]), end='')
def bf_input():
    global index
    data[index] = ord(input())
def zero_cell():
    global index
    data[index] = 0
bf_add(13)
while data[index] != 0:
    bf_sub(1)
    index += 1
    bf_add(2)
    index += 3
    bf_add(5)
    index += 1
    bf_add(2)
    index += 1
    bf_add(1)
    index -= 6
# End of loop
index += 5
bf_add(6)
index += 1
bf_sub(3)
index += 10
bf_add(15)
while data[index] != 0:
    while data[index] != 0:
        index += 9
    # End of loop
    bf_add(1)
    while data[index] != 0:
        index -= 9
    # End of loop
    index += 9
    bf_sub(1)
# End of loop
bf_add(1)
while data[index] != 0:
    index += 8
    while data[index] != 0:
        bf_sub(1)
    # End of loop
    index += 1
# End of loop
index -= 9
while data[index] != 0:
    index -= 9
# End of loop
index += 8
while data[index] != 0:
    bf_sub(1)
# End of loop
bf_add(1)
index -= 7
bf_add(5)
while data[index] != 0:
    bf_sub(1)
    while data[index] != 0:
        bf_sub(1)
        index += 9
        bf_add(1)
        index -= 9
    # End of loop
    index += 9
# End of loop
index += 7
bf_add(1)
index += 26
index += 1
bf_add(1)
index -= 17
while data[index] != 0:
    index -= 9
# End of loop
index += 3
while data[index] != 0:
    bf_sub(1)
# End of loop
bf_add(1)
while data[index] != 0:
    index += 6
    while data[index] != 0:
        index += 7
        while data[index] != 0:
            bf_sub(1)
        # End of loop
        index += 2
    # End of loop
    index -= 9
    while data[index] != 0:
        index -= 9
    # End of loop
    index += 2
    index += 5
    while data[index] != 0:
        bf_sub(1)
    # End of loop
    bf_add(1)
    index -= 6
    bf_add(4)
    while data[index] != 0:
        bf_sub(1)
        while data[index] != 0:
            bf_sub(1)
            index += 9
            bf_add(1)
            index -= 9
        # End of loop
        index += 9
    # End of loop
    index += 6
    bf_add(1)
    index -= 6
    bf_add(7)
    while data[index] != 0:
        bf_sub(1)
        while data[index] != 0:
            bf_sub(1)
            index += 3
            index += 6
            bf_add(1)
            index -= 9
        # End of loop
        index += 9
    # End of loop
    index += 6
    bf_add(1)
    index -= 16
    while data[index] != 0:
        index -= 9
    # End of loop
    index += 3
    while data[index] != 0:
        while data[index] != 0:
            bf_sub(1)
        # End of loop
        index += 6
        while data[index] != 0:
            index += 5
            index += 2
            while data[index] != 0:
                bf_sub(1)
                index -= 6
                bf_add(1)
                index += 6
            # End of loop
            index -= 6
            while data[index] != 0:
                bf_sub(1)
                index += 6
                bf_add(1)
                index -= 2
                bf_add(1)
                index -= 3
                bf_add(1)
                index -= 1
            # End of loop
            index += 8
        # End of loop
        index -= 9
        while data[index] != 0:
            index -= 9
        # End of loop
        index += 9
        while data[index] != 0:
            index += 8
            while data[index] != 0:
                bf_sub(1)
                index -= 7
                bf_add(1)
                index += 7
            # End of loop
            index -= 7
            while data[index] != 0:
                bf_sub(1)
                index += 7
                bf_add(1)
                index -= 2
                bf_add(1)
                index -= 3
                bf_add(1)
                index -= 2
            # End of loop
            index += 8
        # End of loop
        index -= 9
        while data[index] != 0:
            index -= 7
            index -= 2
        # End of loop
        index += 7
        while data[index] != 0:
            bf_sub(1)
            index -= 7
            bf_add(1)
            index += 7
        # End of loop
        index -= 7
        while data[index] != 0:
            bf_sub(1)
            index += 7
            bf_add(1)
            index -= 2
            bf_add(1)
            index -= 5
        # End of loop
        index += 9
        bf_add(15)
        while data[index] != 0:
            while data[index] != 0:
                index += 9
            # End of loop
            bf_add(1)
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            bf_sub(1)
        # End of loop
        bf_add(1)
        while data[index] != 0:
            index += 1
            bf_add(1)
            index += 8
        # End of loop
        index -= 9
        while data[index] != 0:
            index -= 9
        # End of loop
        index += 9
        while data[index] != 0:
            index += 1
            bf_sub(1)
            index += 4
            while data[index] != 0:
                bf_sub(1)
                index -= 4
                bf_add(1)
                index += 4
            # End of loop
            index -= 4
            while data[index] != 0:
                bf_sub(1)
                index += 4
                bf_add(1)
                index -= 5
                while data[index] != 0:
                    bf_sub(1)
                    index += 2
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 2
                        bf_add(1)
                        index += 2
                    # End of loop
                    index -= 2
                    while data[index] != 0:
                        bf_sub(1)
                        index += 2
                        bf_add(1)
                        index += 2
                        bf_add(1)
                        index -= 4
                    # End of loop
                    bf_add(1)
                    index += 9
                # End of loop
                index -= 8
                while data[index] != 0:
                    index -= 9
                # End of loop
            # End of loop
            index += 9
            while data[index] != 0:
                index += 9
            # End of loop
            index -= 7
            index -= 2
            while data[index] != 0:
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                    index += 9
                    bf_add(1)
                    index -= 9
                # End of loop
                index -= 10
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
                index += 9
                bf_add(1)
                index -= 9
            # End of loop
            index -= 1
            bf_add(1)
            index += 8
        # End of loop
        index -= 9
        while data[index] != 0:
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index -= 1
            bf_sub(1)
            index += 4
            while data[index] != 0:
                bf_sub(1)
                index -= 4
                bf_add(1)
                index += 1
                while data[index] != 0:
                    index -= 1
                    bf_sub(1)
                    index += 1
                    bf_sub(1)
                    index -= 6
                    bf_add(1)
                    index += 6
                # End of loop
                index -= 1
                while data[index] != 0:
                    bf_sub(1)
                    index += 1
                    bf_add(1)
                    index -= 1
                # End of loop
                index += 4
            # End of loop
            index -= 3
            while data[index] != 0:
                bf_sub(1)
                index += 3
                bf_add(1)
                index -= 3
            # End of loop
            index -= 1
            bf_add(1)
            index -= 9
        # End of loop
        index += 5
        index += 4
        while data[index] != 0:
            index += 1
            bf_add(1)
            index += 8
        # End of loop
        index -= 9
        while data[index] != 0:
            index -= 9
        # End of loop
        index += 9
        while data[index] != 0:
            index += 1
            bf_sub(1)
            index += 5
            while data[index] != 0:
                bf_sub(1)
                index -= 5
                bf_add(1)
                index += 5
            # End of loop
            index -= 5
            while data[index] != 0:
                bf_sub(1)
                index += 5
                bf_add(1)
                index -= 6
                while data[index] != 0:
                    bf_sub(1)
                    index += 3
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 3
                        bf_add(1)
                        index += 3
                    # End of loop
                    index -= 3
                    while data[index] != 0:
                        bf_sub(1)
                        index += 3
                        bf_add(1)
                        index += 1
                        bf_add(1)
                        index -= 4
                    # End of loop
                    bf_add(1)
                    index += 9
                # End of loop
                index -= 8
                while data[index] != 0:
                    index -= 9
                # End of loop
            # End of loop
            index += 9
            while data[index] != 0:
                index += 2
                index += 7
            # End of loop
            index -= 9
            while data[index] != 0:
                index += 2
                while data[index] != 0:
                    bf_sub(1)
                    index += 9
                    bf_add(1)
                    index -= 9
                # End of loop
                index -= 11
            # End of loop
            index += 2
            while data[index] != 0:
                bf_sub(1)
                index += 9
                bf_add(1)
                index -= 9
            # End of loop
            index -= 2
            bf_add(1)
            index += 8
        # End of loop
        index -= 9
        while data[index] != 0:
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index -= 1
            bf_sub(1)
            index += 4
            while data[index] != 0:
                bf_sub(1)
                index -= 4
                bf_add(1)
                index += 1
                while data[index] != 0:
                    index -= 1
                    bf_sub(1)
                    index += 1
                    bf_sub(1)
                    index -= 6
                    bf_add(1)
                    index += 6
                # End of loop
                index -= 1
                while data[index] != 0:
                    bf_sub(1)
                    index += 1
                    bf_add(1)
                    index -= 1
                # End of loop
                index += 4
            # End of loop
            index -= 3
            while data[index] != 0:
                bf_sub(1)
                index += 3
                bf_add(1)
                index -= 2
                index -= 1
            # End of loop
            index -= 1
            bf_add(1)
            index -= 9
        # End of loop
        index += 9
        while data[index] != 0:
            index += 4
            while data[index] != 0:
                bf_sub(1)
                index -= 36
                bf_add(1)
                index += 13
                index += 23
            # End of loop
            index += 5
        # End of loop
        index -= 9
        while data[index] != 0:
            index -= 9
        # End of loop
        index += 9
        bf_add(15)
        while data[index] != 0:
            while data[index] != 0:
                index += 4
                index += 5
            # End of loop
            index -= 9
            bf_sub(1)
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            bf_sub(1)
        # End of loop
        bf_add(1)
        index += 21
        bf_add(1)
        index -= 3
        while data[index] != 0:
            index -= 6
            index -= 3
        # End of loop
        index += 9
        while data[index] != 0:
            index += 3
            while data[index] != 0:
                bf_sub(1)
                index -= 3
                bf_sub(1)
                index += 3
            # End of loop
            bf_add(1)
            index -= 3
            while data[index] != 0:
                bf_sub(1)
                index += 3
                bf_sub(1)
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                    index -= 4
                    bf_add(1)
                    index += 4
                # End of loop
                index -= 4
                while data[index] != 0:
                    bf_sub(1)
                    index += 4
                    bf_add(1)
                    index -= 13
                    while data[index] != 0:
                        index -= 5
                        index -= 4
                    # End of loop
                    index += 4
                    while data[index] != 0:
                        bf_sub(1)
                    # End of loop
                    bf_add(1)
                    index += 5
                    while data[index] != 0:
                        index += 9
                    # End of loop
                    index += 1
                    bf_add(1)
                    index -= 1
                # End of loop
            # End of loop
            bf_add(1)
            index += 4
            while data[index] != 0:
                bf_sub(1)
                index -= 4
                bf_sub(1)
                index += 4
            # End of loop
            bf_add(1)
            index -= 4
            while data[index] != 0:
                bf_sub(1)
                index += 4
                bf_sub(1)
                index -= 1
                while data[index] != 0:
                    bf_sub(1)
                    index -= 3
                    bf_add(1)
                    index += 3
                # End of loop
                index -= 3
                while data[index] != 0:
                    bf_sub(1)
                    index += 1
                    index += 2
                    bf_add(1)
                    index -= 12
                    while data[index] != 0:
                        index -= 9
                    # End of loop
                    index += 3
                    while data[index] != 0:
                        bf_sub(1)
                    # End of loop
                    bf_add(1)
                    index += 6
                    while data[index] != 0:
                        index += 9
                    # End of loop
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                    # End of loop
                    bf_add(1)
                    index -= 1
                # End of loop
            # End of loop
            bf_add(1)
            index += 1
            while data[index] != 0:
                bf_sub(1)
                index -= 1
                while data[index] != 0:
                    index += 9
                # End of loop
                index -= 6
                index -= 2
            # End of loop
            index += 8
        # End of loop
        index -= 9
        while data[index] != 0:
            index -= 9
        # End of loop
        index -= 7
        while data[index] != 0:
            bf_sub(1)
            index += 1
            bf_add(1)
            index += 3
            bf_sub(1)
            index -= 4
        # End of loop
        index += 9
        bf_add(19)
        bf_add(7)
        index += 2
        while data[index] != 0:
            bf_sub(1)
            index -= 4
            bf_add(1)
            index += 4
        # End of loop
        index -= 4
        while data[index] != 0:
            bf_sub(1)
            index += 4
            bf_add(1)
            index -= 2
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index -= 2
        # End of loop
        index += 2
        while data[index] != 0:
            index -= 7
            bf_add(1)
            index -= 1
            while data[index] != 0:
                bf_sub(1)
                index -= 1
                bf_add(1)
                index += 4
                bf_add(1)
                index -= 2
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
                index -= 2
                while data[index] != 0:
                    bf_sub(1)
                    index += 1
                    bf_add(1)
                    index += 3
                    bf_sub(1)
                    index -= 4
                # End of loop
                index += 3
            # End of loop
            index += 13
            while data[index] != 0:
                index += 2
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 5
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 3
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 6
            while data[index] != 0:
                index += 5
                while data[index] != 0:
                    bf_sub(1)
                    index -= 4
                    bf_add(1)
                    index += 4
                # End of loop
                index -= 4
                while data[index] != 0:
                    bf_sub(1)
                    index += 4
                    bf_add(1)
                    index -= 3
                    bf_add(1)
                    index -= 1
                # End of loop
                index += 8
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 2
                while data[index] != 0:
                    bf_sub(1)
                    index -= 8
                    index -= 1
                    bf_add(1)
                    index += 9
                # End of loop
                index += 7
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            bf_add(15)
            while data[index] != 0:
                while data[index] != 0:
                    index += 9
                # End of loop
                bf_add(1)
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index -= 9
                while data[index] != 0:
                    index -= 9
                # End of loop
                index += 9
                bf_sub(1)
            # End of loop
            bf_add(1)
            while data[index] != 0:
                index += 1
                bf_add(1)
                index += 8
            # End of loop
            index -= 3
            index -= 6
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 1
                bf_sub(1)
                index += 5
                while data[index] != 0:
                    bf_sub(1)
                    index -= 5
                    bf_add(1)
                    index += 5
                # End of loop
                index -= 5
                while data[index] != 0:
                    bf_sub(1)
                    index += 5
                    bf_add(1)
                    index -= 6
                    while data[index] != 0:
                        bf_sub(1)
                        index += 2
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 2
                            bf_add(1)
                            index += 2
                        # End of loop
                        index -= 1
                        index -= 1
                        while data[index] != 0:
                            bf_sub(1)
                            index += 2
                            bf_add(1)
                            index += 1
                            bf_add(1)
                            index -= 3
                        # End of loop
                        bf_add(1)
                        index += 9
                    # End of loop
                    index -= 8
                    while data[index] != 0:
                        index -= 9
                    # End of loop
                # End of loop
                index += 9
                while data[index] != 0:
                    index += 9
                # End of loop
                index -= 9
                while data[index] != 0:
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 4
                        index += 5
                        bf_add(1)
                        index -= 9
                    # End of loop
                    index -= 10
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                    index += 9
                    bf_add(1)
                    index -= 9
                # End of loop
                index -= 1
                bf_add(1)
                index += 8
            # End of loop
            index -= 9
            while data[index] != 0:
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index -= 1
                bf_sub(1)
                index += 3
                while data[index] != 0:
                    bf_sub(1)
                    index -= 3
                    bf_add(1)
                    index += 1
                    while data[index] != 0:
                        index -= 1
                        bf_sub(1)
                        index += 1
                        bf_sub(1)
                        index -= 7
                        bf_add(1)
                        index += 7
                    # End of loop
                    index -= 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 1
                        bf_add(1)
                        index -= 1
                    # End of loop
                    index += 3
                # End of loop
                index -= 2
                while data[index] != 0:
                    bf_sub(1)
                    index += 2
                    bf_add(1)
                    index -= 2
                # End of loop
                index -= 1
                bf_add(1)
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 6
                while data[index] != 0:
                    bf_sub(1)
                    index -= 1
                    index -= 4
                    bf_add(1)
                    index += 5
                # End of loop
                index -= 5
                while data[index] != 0:
                    bf_sub(1)
                    index += 5
                    bf_add(1)
                    index -= 4
                    bf_add(1)
                    index -= 1
                # End of loop
                index += 8
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 1
                bf_add(1)
                index += 8
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 1
                bf_sub(1)
                index += 5
                while data[index] != 0:
                    bf_sub(1)
                    index -= 5
                    bf_add(1)
                    index += 5
                # End of loop
                index -= 5
                while data[index] != 0:
                    bf_sub(1)
                    index += 5
                    bf_add(1)
                    index -= 6
                    while data[index] != 0:
                        bf_sub(1)
                        index += 2
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 2
                            bf_add(1)
                            index += 2
                        # End of loop
                        index -= 2
                        while data[index] != 0:
                            bf_sub(1)
                            index += 2
                            bf_add(1)
                            index += 2
                            bf_add(1)
                            index -= 4
                        # End of loop
                        bf_add(1)
                        index += 9
                    # End of loop
                    index -= 8
                    while data[index] != 0:
                        index -= 9
                    # End of loop
                # End of loop
                index += 9
                while data[index] != 0:
                    index += 9
                # End of loop
                index -= 9
                while data[index] != 0:
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 9
                        bf_add(1)
                        index -= 9
                    # End of loop
                    index -= 10
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                    index += 9
                    bf_add(1)
                    index -= 9
                # End of loop
                index -= 1
                bf_add(1)
                index += 8
            # End of loop
            index -= 9
            while data[index] != 0:
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index -= 1
                bf_sub(1)
                index += 4
                while data[index] != 0:
                    bf_sub(1)
                    index -= 4
                    bf_add(1)
                    index += 1
                    while data[index] != 0:
                        index -= 1
                        bf_sub(1)
                        index += 1
                        bf_sub(1)
                        index -= 6
                        bf_add(1)
                        index += 6
                    # End of loop
                    index -= 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 1
                        bf_add(1)
                        index -= 1
                    # End of loop
                    index += 4
                # End of loop
                index -= 3
                while data[index] != 0:
                    bf_sub(1)
                    index += 3
                    bf_add(1)
                    index -= 3
                # End of loop
                index -= 1
                bf_add(1)
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 4
                while data[index] != 0:
                    bf_sub(1)
                    index -= 36
                    bf_add(1)
                    index += 36
                # End of loop
                index += 5
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 3
                while data[index] != 0:
                    bf_sub(1)
                    index -= 36
                    bf_add(1)
                    index += 1
                    index += 35
                # End of loop
                index += 6
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            bf_add(8)
            bf_add(7)
            while data[index] != 0:
                while data[index] != 0:
                    index += 9
                # End of loop
                index -= 9
                bf_sub(1)
                index -= 9
                while data[index] != 0:
                    index -= 9
                # End of loop
                index += 9
                bf_sub(1)
            # End of loop
            bf_add(1)
            while data[index] != 0:
                index += 8
                while data[index] != 0:
                    bf_sub(1)
                    index -= 7
                    bf_add(1)
                    index += 7
                # End of loop
                index -= 7
                while data[index] != 0:
                    bf_sub(1)
                    index += 7
                    bf_add(1)
                    index -= 6
                    bf_add(1)
                    index -= 1
                # End of loop
                index += 8
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 6
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 3
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 4
            bf_add(1)
            index += 1
            while data[index] != 0:
                bf_sub(1)
                index -= 1
                bf_sub(1)
                index -= 4
                bf_add(1)
                index += 5
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
                index -= 6
                while data[index] != 0:
                    bf_sub(1)
                    index += 5
                    bf_add(1)
                    index -= 1
                    bf_add(2)
                    index -= 4
                # End of loop
                index += 5
                while data[index] != 0:
                    bf_sub(1)
                    index -= 1
                    index -= 4
                    bf_add(1)
                    index += 5
                # End of loop
                index -= 1
                bf_sub(1)
                index += 1
                bf_add(1)
                index += 1
            # End of loop
            index -= 1
            while data[index] != 0:
                bf_sub(1)
                index += 1
                bf_add(1)
                index -= 1
            # End of loop
            index -= 5
            while data[index] != 0:
                bf_sub(1)
                index += 5
                bf_add(1)
                index -= 5
            # End of loop
            index += 6
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index -= 6
            bf_add(1)
            index += 4
            while data[index] != 0:
                bf_sub(1)
                index -= 4
                bf_sub(1)
                index += 4
            # End of loop
            bf_add(1)
            index -= 4
            while data[index] != 0:
                bf_sub(1)
                index += 4
                bf_sub(1)
                index += 5
                while data[index] != 0:
                    index += 2
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 2
                        bf_sub(1)
                        index += 2
                    # End of loop
                    bf_add(1)
                    index -= 2
                    while data[index] != 0:
                        bf_sub(1)
                        index += 2
                        bf_sub(1)
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 3
                            bf_add(1)
                            index += 3
                        # End of loop
                        index -= 3
                        while data[index] != 0:
                            bf_sub(1)
                            index += 3
                            bf_add(1)
                            index -= 12
                            while data[index] != 0:
                                index -= 9
                            # End of loop
                            index += 3
                            while data[index] != 0:
                                bf_sub(1)
                            # End of loop
                            bf_add(1)
                            index += 6
                            while data[index] != 0:
                                index += 9
                            # End of loop
                            index += 1
                            bf_add(1)
                            index -= 1
                        # End of loop
                    # End of loop
                    bf_add(1)
                    index += 3
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 3
                        bf_sub(1)
                        index += 3
                    # End of loop
                    bf_add(1)
                    index -= 3
                    while data[index] != 0:
                        bf_sub(1)
                        index += 3
                        bf_sub(1)
                        index -= 1
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 2
                            bf_add(1)
                            index += 2
                        # End of loop
                        index -= 2
                        while data[index] != 0:
                            bf_sub(1)
                            index += 2
                            bf_add(1)
                            index -= 11
                            while data[index] != 0:
                                index -= 5
                                index -= 4
                            # End of loop
                            index += 4
                            while data[index] != 0:
                                bf_sub(1)
                            # End of loop
                            bf_add(1)
                            index += 5
                            while data[index] != 0:
                                index += 9
                            # End of loop
                            index += 1
                            while data[index] != 0:
                                bf_sub(1)
                            # End of loop
                            bf_add(1)
                            index -= 1
                        # End of loop
                    # End of loop
                    bf_add(1)
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 1
                        while data[index] != 0:
                            index += 9
                        # End of loop
                        index -= 8
                    # End of loop
                    index += 8
                # End of loop
                index -= 9
                while data[index] != 0:
                    index -= 9
                # End of loop
                index += 4
                while data[index] != 0:
                    bf_sub(1)
                    index -= 4
                    bf_add(1)
                    index += 4
                # End of loop
                index -= 4
                while data[index] != 0:
                    bf_sub(1)
                    index += 4
                    bf_add(1)
                    index += 5
                    while data[index] != 0:
                        index += 1
                        bf_add(1)
                        index += 2
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 2
                            bf_sub(1)
                            index += 2
                        # End of loop
                        index -= 2
                        while data[index] != 0:
                            bf_sub(1)
                            index += 2
                            bf_add(1)
                            index -= 2
                        # End of loop
                        index += 8
                    # End of loop
                    index -= 5
                    index -= 3
                    bf_add(1)
                    index -= 1
                    while data[index] != 0:
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index += 5
                            bf_add(1)
                            index -= 4
                            while data[index] != 0:
                                bf_sub(1)
                                index += 4
                                bf_sub(1)
                                index -= 14
                                bf_add(1)
                                index += 11
                                while data[index] != 0:
                                    bf_sub(1)
                                    index += 3
                                    bf_add(1)
                                    index -= 3
                                # End of loop
                                index -= 1
                            # End of loop
                            index += 1
                            while data[index] != 0:
                                bf_sub(1)
                                index += 3
                                bf_sub(1)
                                index -= 9
                                index -= 5
                                bf_add(1)
                                index += 11
                            # End of loop
                            index -= 2
                        # End of loop
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index += 4
                            bf_add(1)
                            index -= 3
                            while data[index] != 0:
                                bf_sub(1)
                                index += 3
                                bf_sub(1)
                                index -= 14
                                bf_add(1)
                                index += 11
                            # End of loop
                            index -= 1
                        # End of loop
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index += 3
                            bf_add(1)
                            index -= 3
                        # End of loop
                        index -= 2
                        index -= 10
                    # End of loop
                    index += 4
                    while data[index] != 0:
                        bf_sub(1)
                    # End of loop
                    index -= 4
                # End of loop
                index += 3
                while data[index] != 0:
                    bf_sub(1)
                    index -= 3
                    bf_add(1)
                    index += 3
                # End of loop
                index -= 3
                while data[index] != 0:
                    bf_sub(1)
                    index += 3
                    bf_add(1)
                    index += 6
                    while data[index] != 0:
                        index += 1
                        bf_add(1)
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 1
                            bf_sub(1)
                            index += 1
                        # End of loop
                        index -= 1
                        while data[index] != 0:
                            bf_sub(1)
                            index += 1
                            bf_add(1)
                            index -= 1
                        # End of loop
                        index += 8
                    # End of loop
                    index -= 3
                    index -= 5
                    bf_add(1)
                    index -= 1
                    while data[index] != 0:
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index += 5
                            bf_add(1)
                            index -= 3
                            while data[index] != 0:
                                bf_sub(1)
                                index += 3
                                bf_sub(1)
                                index -= 14
                                bf_add(1)
                                index += 10
                                while data[index] != 0:
                                    bf_sub(1)
                                    index += 4
                                    bf_add(1)
                                    index -= 4
                                # End of loop
                                index += 1
                            # End of loop
                            index -= 1
                            while data[index] != 0:
                                bf_sub(1)
                                index += 4
                                bf_sub(1)
                                index -= 7
                                index -= 7
                                bf_add(1)
                                index += 10
                            # End of loop
                            index -= 1
                        # End of loop
                        index += 2
                        while data[index] != 0:
                            bf_sub(1)
                            index += 3
                            bf_add(1)
                            index -= 4
                            while data[index] != 0:
                                bf_sub(1)
                                index += 4
                                bf_sub(1)
                                index -= 14
                                bf_add(1)
                                index += 10
                            # End of loop
                            index += 1
                        # End of loop
                        index -= 1
                        while data[index] != 0:
                            bf_sub(1)
                            index += 4
                            bf_add(1)
                            index -= 4
                        # End of loop
                        index -= 11
                    # End of loop
                    index += 6
                    bf_add(1)
                    index -= 6
                # End of loop
            # End of loop
            index += 4
            while data[index] != 0:
                bf_sub(1)
                index -= 4
                bf_add(1)
                index += 4
            # End of loop
            index -= 4
            while data[index] != 0:
                bf_sub(1)
                index += 4
                bf_add(1)
                index += 5
                while data[index] != 0:
                    index += 9
                # End of loop
                index -= 9
                while data[index] != 0:
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 5
                        bf_add(1)
                        index -= 4
                        while data[index] != 0:
                            bf_sub(1)
                            index += 4
                            bf_sub(1)
                            index -= 14
                            bf_add(1)
                            index += 11
                            while data[index] != 0:
                                bf_sub(1)
                                index += 3
                                bf_add(1)
                                index -= 3
                            # End of loop
                            index -= 1
                        # End of loop
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index += 3
                            bf_sub(1)
                            index -= 14
                            bf_add(1)
                            index += 11
                        # End of loop
                        index -= 2
                    # End of loop
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 4
                        bf_add(1)
                        index -= 3
                        while data[index] != 0:
                            bf_sub(1)
                            index += 3
                            bf_sub(1)
                            index -= 14
                            bf_add(1)
                            index += 11
                        # End of loop
                        index -= 1
                    # End of loop
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 3
                        bf_add(1)
                        index -= 3
                    # End of loop
                    index -= 7
                    index -= 5
                # End of loop
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 2
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 5
            while data[index] != 0:
                index += 2
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 6
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 5
                while data[index] != 0:
                    bf_sub(1)
                    index -= 1
                    index -= 3
                    bf_add(1)
                    index += 4
                # End of loop
                index -= 4
                while data[index] != 0:
                    bf_sub(1)
                    index += 4
                    bf_add(1)
                    index -= 3
                    bf_add(1)
                    index -= 1
                # End of loop
                index += 8
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            bf_add(15)
            while data[index] != 0:
                while data[index] != 0:
                    index += 9
                # End of loop
                bf_add(1)
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index -= 9
                while data[index] != 0:
                    index -= 9
                # End of loop
                index += 9
                bf_sub(1)
            # End of loop
            bf_add(1)
            while data[index] != 0:
                index += 1
                bf_add(1)
                index += 8
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 1
                bf_sub(1)
                index += 4
                while data[index] != 0:
                    bf_sub(1)
                    index -= 4
                    bf_add(1)
                    index += 4
                # End of loop
                index -= 4
                while data[index] != 0:
                    bf_sub(1)
                    index += 4
                    bf_add(1)
                    index -= 5
                    while data[index] != 0:
                        bf_sub(1)
                        index += 2
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 2
                            bf_add(1)
                            index += 2
                        # End of loop
                        index -= 2
                        while data[index] != 0:
                            bf_sub(1)
                            index += 2
                            bf_add(1)
                            index += 1
                            bf_add(1)
                            index -= 3
                        # End of loop
                        bf_add(1)
                        index += 9
                    # End of loop
                    index -= 8
                    while data[index] != 0:
                        index -= 9
                    # End of loop
                # End of loop
                index += 9
                while data[index] != 0:
                    index += 9
                # End of loop
                index -= 8
                index -= 1
                while data[index] != 0:
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 9
                        bf_add(1)
                        index -= 9
                    # End of loop
                    index -= 10
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                    index += 9
                    bf_add(1)
                    index -= 9
                # End of loop
                index -= 1
                bf_add(1)
                index += 8
            # End of loop
            index -= 9
            while data[index] != 0:
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index -= 1
                bf_sub(1)
                index += 3
                while data[index] != 0:
                    bf_sub(1)
                    index -= 3
                    bf_add(1)
                    index += 1
                    while data[index] != 0:
                        index -= 1
                        bf_sub(1)
                        index += 1
                        bf_sub(1)
                        index -= 7
                        bf_add(1)
                        index += 7
                    # End of loop
                    index -= 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 1
                        bf_add(1)
                        index -= 1
                    # End of loop
                    index += 3
                # End of loop
                index -= 2
                while data[index] != 0:
                    bf_sub(1)
                    index += 2
                    bf_add(1)
                    index -= 2
                # End of loop
                index -= 1
                bf_add(1)
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 3
                while data[index] != 0:
                    bf_sub(1)
                    index -= 36
                    bf_add(1)
                    index += 36
                # End of loop
                index += 1
                index += 5
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 5
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 4
            bf_add(15)
            while data[index] != 0:
                while data[index] != 0:
                    index += 9
                # End of loop
                index -= 9
                bf_sub(1)
                index -= 5
                index -= 4
                while data[index] != 0:
                    index -= 9
                # End of loop
                index += 9
                bf_sub(1)
            # End of loop
            bf_add(1)
            while data[index] != 0:
                index += 3
                while data[index] != 0:
                    bf_sub(1)
                    index -= 3
                    bf_sub(1)
                    index += 3
                # End of loop
                bf_add(1)
                index -= 3
                while data[index] != 0:
                    bf_sub(1)
                    index += 3
                    bf_sub(1)
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 4
                        bf_add(1)
                        index += 4
                    # End of loop
                    index -= 4
                    while data[index] != 0:
                        bf_sub(1)
                        index += 4
                        bf_add(1)
                        index -= 5
                        index -= 8
                        while data[index] != 0:
                            index -= 9
                        # End of loop
                        index += 4
                        while data[index] != 0:
                            bf_sub(1)
                        # End of loop
                        bf_add(1)
                        index += 5
                        while data[index] != 0:
                            index += 9
                        # End of loop
                        index += 1
                        bf_add(1)
                        index -= 1
                    # End of loop
                # End of loop
                bf_add(1)
                index += 4
                while data[index] != 0:
                    bf_sub(1)
                    index -= 4
                    bf_sub(1)
                    index += 4
                # End of loop
                bf_add(1)
                index -= 4
                while data[index] != 0:
                    bf_sub(1)
                    index += 4
                    bf_sub(1)
                    index -= 1
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 3
                        bf_add(1)
                        index += 3
                    # End of loop
                    index -= 3
                    while data[index] != 0:
                        bf_sub(1)
                        index += 3
                        bf_add(1)
                        index -= 12
                        while data[index] != 0:
                            index -= 9
                        # End of loop
                        index += 3
                        while data[index] != 0:
                            bf_sub(1)
                        # End of loop
                        bf_add(1)
                        index += 6
                        while data[index] != 0:
                            index += 9
                        # End of loop
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                        # End of loop
                        bf_add(1)
                        index -= 1
                    # End of loop
                # End of loop
                bf_add(1)
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                    index -= 1
                    while data[index] != 0:
                        index += 2
                        index += 7
                    # End of loop
                    index -= 8
                # End of loop
                index += 8
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 3
            while data[index] != 0:
                bf_sub(1)
                index -= 3
                bf_add(1)
                index += 3
            # End of loop
            index -= 3
            while data[index] != 0:
                bf_sub(1)
                index += 3
                bf_add(1)
                index += 6
                while data[index] != 0:
                    index += 1
                    bf_add(1)
                    index += 3
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 3
                        bf_sub(1)
                        index += 3
                    # End of loop
                    index -= 3
                    while data[index] != 0:
                        bf_sub(1)
                        index += 3
                        bf_add(1)
                        index -= 3
                    # End of loop
                    index += 8
                # End of loop
                index -= 8
                bf_add(1)
                index -= 1
                while data[index] != 0:
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 1
                        bf_add(1)
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 1
                            bf_sub(1)
                            index -= 10
                            bf_add(1)
                            index += 12
                            while data[index] != 0:
                                bf_sub(1)
                                index -= 2
                                bf_add(1)
                                index += 2
                            # End of loop
                            index -= 1
                        # End of loop
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 2
                            bf_sub(1)
                            index -= 10
                            bf_add(1)
                            index += 12
                        # End of loop
                        index -= 3
                    # End of loop
                    index += 2
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 1
                        bf_add(1)
                        index += 2
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 2
                            bf_sub(1)
                            index -= 10
                            bf_add(1)
                            index += 12
                        # End of loop
                        index -= 1
                    # End of loop
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 2
                        bf_add(1)
                        index += 2
                    # End of loop
                    index -= 13
                # End of loop
            # End of loop
            index += 4
            while data[index] != 0:
                bf_sub(1)
                index -= 4
                bf_add(1)
                index += 4
            # End of loop
            index -= 4
            while data[index] != 0:
                bf_sub(1)
                index += 4
                bf_add(1)
                index += 5
                while data[index] != 0:
                    index += 1
                    bf_add(1)
                    index += 2
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 2
                        bf_sub(1)
                        index += 2
                    # End of loop
                    index -= 2
                    while data[index] != 0:
                        bf_sub(1)
                        index += 2
                        bf_add(1)
                        index -= 2
                    # End of loop
                    index += 2
                    index += 6
                # End of loop
                index -= 8
                bf_add(1)
                index -= 1
                while data[index] != 0:
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 1
                        bf_add(1)
                        index += 2
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 2
                            bf_sub(1)
                            index -= 10
                            bf_add(1)
                            index += 11
                            while data[index] != 0:
                                bf_sub(1)
                                index -= 1
                                bf_add(1)
                                index += 1
                            # End of loop
                            index += 1
                        # End of loop
                        index -= 1
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 1
                            bf_sub(1)
                            index -= 10
                            bf_add(1)
                            index += 4
                            index += 7
                        # End of loop
                        index -= 2
                    # End of loop
                    index += 3
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 2
                        bf_add(1)
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 1
                            bf_sub(1)
                            index -= 10
                            bf_add(1)
                            index += 11
                        # End of loop
                        index += 1
                    # End of loop
                    index -= 1
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 1
                        bf_add(1)
                        index += 1
                    # End of loop
                    index -= 12
                # End of loop
                index += 5
                bf_add(1)
                index -= 5
            # End of loop
            index += 9
            while data[index] != 0:
                index += 3
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 4
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 3
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 5
            while data[index] != 0:
                index += 7
                while data[index] != 0:
                    bf_sub(1)
                    index -= 5
                    index -= 1
                    bf_add(1)
                    index += 6
                # End of loop
                index -= 6
                while data[index] != 0:
                    bf_sub(1)
                    index += 6
                    bf_add(1)
                    index -= 4
                    bf_add(1)
                    index -= 2
                # End of loop
                index += 8
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 4
            bf_add(1)
            index += 1
            while data[index] != 0:
                bf_sub(1)
                index -= 1
                bf_sub(1)
                index -= 4
                bf_add(1)
                index += 4
                index += 1
            # End of loop
            index += 2
            while data[index] != 0:
                bf_sub(1)
                index -= 7
                while data[index] != 0:
                    bf_sub(1)
                    index += 5
                    bf_add(1)
                    index -= 1
                    bf_add(2)
                    index -= 4
                # End of loop
                index += 5
                while data[index] != 0:
                    bf_sub(1)
                    index -= 5
                    bf_add(1)
                    index += 5
                # End of loop
                index -= 1
                bf_sub(1)
                index += 1
                bf_add(1)
                index += 2
            # End of loop
            index -= 2
            while data[index] != 0:
                bf_sub(1)
                index += 2
                bf_add(1)
                index -= 2
            # End of loop
            index -= 5
            while data[index] != 0:
                bf_sub(1)
                index += 5
                bf_add(1)
                index -= 2
                index -= 3
            # End of loop
            bf_add(1)
            index += 4
            while data[index] != 0:
                bf_sub(1)
                index -= 4
                bf_sub(1)
                index += 4
            # End of loop
            bf_add(1)
            index -= 4
            while data[index] != 0:
                bf_sub(1)
                index += 4
                bf_sub(1)
                index += 5
                while data[index] != 0:
                    index += 3
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 3
                        bf_sub(1)
                        index += 3
                    # End of loop
                    bf_add(1)
                    index -= 3
                    while data[index] != 0:
                        bf_sub(1)
                        index += 3
                        bf_sub(1)
                        index -= 1
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 2
                            bf_add(1)
                            index += 2
                        # End of loop
                        index -= 2
                        while data[index] != 0:
                            bf_sub(1)
                            index += 2
                            bf_add(1)
                            index -= 2
                            index -= 9
                            while data[index] != 0:
                                index -= 9
                            # End of loop
                            index += 4
                            while data[index] != 0:
                                bf_sub(1)
                            # End of loop
                            bf_add(1)
                            index += 5
                            while data[index] != 0:
                                index += 9
                            # End of loop
                            index += 1
                            bf_add(1)
                            index -= 1
                        # End of loop
                    # End of loop
                    bf_add(1)
                    index += 2
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 2
                        bf_sub(1)
                        index += 2
                    # End of loop
                    bf_add(1)
                    index -= 2
                    while data[index] != 0:
                        bf_sub(1)
                        index += 2
                        bf_sub(1)
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 3
                            bf_add(1)
                            index += 3
                        # End of loop
                        index -= 1
                        index -= 2
                        while data[index] != 0:
                            bf_sub(1)
                            index += 3
                            bf_add(1)
                            index -= 12
                            while data[index] != 0:
                                index -= 9
                            # End of loop
                            index += 3
                            while data[index] != 0:
                                bf_sub(1)
                            # End of loop
                            bf_add(1)
                            index += 6
                            while data[index] != 0:
                                index += 9
                            # End of loop
                            index += 1
                            while data[index] != 0:
                                bf_sub(1)
                            # End of loop
                            bf_add(1)
                            index -= 1
                        # End of loop
                    # End of loop
                    bf_add(1)
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 1
                        while data[index] != 0:
                            index += 9
                        # End of loop
                        index -= 1
                        index -= 7
                    # End of loop
                    index += 8
                # End of loop
                index -= 9
                while data[index] != 0:
                    index -= 9
                # End of loop
                index += 3
                while data[index] != 0:
                    bf_sub(1)
                    index -= 3
                    bf_add(1)
                    index += 3
                # End of loop
                index -= 3
                while data[index] != 0:
                    bf_sub(1)
                    index += 3
                    bf_add(1)
                    index += 6
                    while data[index] != 0:
                        index += 1
                        bf_add(1)
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 1
                            bf_sub(1)
                            index += 1
                        # End of loop
                        index -= 1
                        while data[index] != 0:
                            bf_sub(1)
                            index += 1
                            bf_add(1)
                            index -= 1
                        # End of loop
                        index += 8
                    # End of loop
                    index -= 8
                    bf_add(1)
                    index -= 1
                    while data[index] != 0:
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index += 4
                            bf_add(1)
                            index -= 2
                            while data[index] != 0:
                                bf_sub(1)
                                index += 2
                                bf_sub(1)
                                index -= 13
                                bf_add(1)
                                index += 10
                                while data[index] != 0:
                                    bf_sub(1)
                                    index += 3
                                    bf_add(1)
                                    index -= 3
                                # End of loop
                                index += 1
                            # End of loop
                            index -= 1
                            while data[index] != 0:
                                bf_sub(1)
                                index += 3
                                bf_sub(1)
                                index -= 13
                                bf_add(1)
                                index += 10
                            # End of loop
                            index -= 1
                        # End of loop
                        index += 2
                        while data[index] != 0:
                            bf_sub(1)
                            index += 2
                            bf_add(1)
                            index -= 3
                            while data[index] != 0:
                                bf_sub(1)
                                index += 3
                                bf_sub(1)
                                index -= 13
                                bf_add(1)
                                index += 10
                            # End of loop
                            index += 1
                        # End of loop
                        index -= 1
                        while data[index] != 0:
                            bf_sub(1)
                            index += 3
                            bf_add(1)
                            index -= 3
                        # End of loop
                        index -= 11
                    # End of loop
                    index += 5
                    while data[index] != 0:
                        bf_sub(1)
                    # End of loop
                    index += 2
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 7
                        bf_add(1)
                        index += 7
                    # End of loop
                    index -= 7
                    while data[index] != 0:
                        bf_sub(1)
                        index += 7
                        bf_add(1)
                        index -= 2
                        bf_add(1)
                        index -= 5
                    # End of loop
                # End of loop
                index += 4
                while data[index] != 0:
                    bf_sub(1)
                    index -= 4
                    bf_add(1)
                    index += 1
                    index += 3
                # End of loop
                index -= 4
                while data[index] != 0:
                    bf_sub(1)
                    index += 4
                    bf_add(1)
                    index += 5
                    while data[index] != 0:
                        index += 1
                        bf_add(1)
                        index += 2
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 2
                            bf_sub(1)
                            index += 2
                        # End of loop
                        index -= 2
                        while data[index] != 0:
                            bf_sub(1)
                            index += 2
                            bf_add(1)
                            index -= 2
                        # End of loop
                        index += 8
                    # End of loop
                    index -= 8
                    bf_add(1)
                    index -= 1
                    while data[index] != 0:
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index += 4
                            bf_add(1)
                            index -= 3
                            while data[index] != 0:
                                bf_sub(1)
                                index += 3
                                bf_sub(1)
                                index -= 13
                                bf_add(1)
                                index += 11
                                while data[index] != 0:
                                    bf_sub(1)
                                    index += 2
                                    bf_add(1)
                                    index -= 2
                                # End of loop
                                index -= 1
                            # End of loop
                            index += 1
                            while data[index] != 0:
                                bf_sub(1)
                                index += 2
                                bf_sub(1)
                                index -= 13
                                bf_add(1)
                                index += 11
                            # End of loop
                            index -= 2
                        # End of loop
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index += 3
                            bf_add(1)
                            index -= 2
                            while data[index] != 0:
                                bf_sub(1)
                                index += 2
                                bf_sub(1)
                                index -= 13
                                bf_add(1)
                                index += 11
                            # End of loop
                            index -= 1
                        # End of loop
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index += 2
                            bf_add(1)
                            index -= 2
                        # End of loop
                        index -= 12
                    # End of loop
                # End of loop
                index += 4
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index -= 4
            # End of loop
            index += 4
            while data[index] != 0:
                bf_sub(1)
                index -= 4
                bf_add(1)
                index += 2
                index += 2
            # End of loop
            index -= 4
            while data[index] != 0:
                bf_sub(1)
                index += 4
                bf_add(1)
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 2
                while data[index] != 0:
                    bf_sub(1)
                    index -= 7
                    bf_add(1)
                    index += 7
                # End of loop
                index -= 7
                while data[index] != 0:
                    bf_sub(1)
                    index += 7
                    bf_add(1)
                    index -= 2
                    bf_add(1)
                    index -= 5
                # End of loop
                index += 9
                while data[index] != 0:
                    index += 6
                    index += 3
                # End of loop
                index -= 9
                while data[index] != 0:
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 4
                        bf_add(1)
                        index -= 3
                        while data[index] != 0:
                            bf_sub(1)
                            index += 3
                            bf_sub(1)
                            index -= 13
                            bf_add(1)
                            index += 11
                            while data[index] != 0:
                                bf_sub(1)
                                index += 2
                                bf_add(1)
                                index -= 2
                            # End of loop
                            index -= 1
                        # End of loop
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                            index += 2
                            bf_sub(1)
                            index -= 8
                            index -= 5
                            bf_add(1)
                            index += 11
                        # End of loop
                        index -= 2
                    # End of loop
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 3
                        bf_add(1)
                        index -= 2
                        while data[index] != 0:
                            bf_sub(1)
                            index += 2
                            bf_sub(1)
                            index -= 13
                            bf_add(1)
                            index += 11
                        # End of loop
                        index -= 1
                    # End of loop
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 2
                        bf_add(1)
                        index -= 2
                    # End of loop
                    index -= 8
                    index -= 4
                # End of loop
            # End of loop
            index += 9
            while data[index] != 0:
                index += 2
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 6
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 3
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 5
            while data[index] != 0:
                index += 5
                while data[index] != 0:
                    bf_sub(1)
                    index -= 4
                    bf_add(1)
                    index += 4
                # End of loop
                index -= 4
                while data[index] != 0:
                    bf_sub(1)
                    index += 4
                    bf_add(1)
                    index -= 3
                    bf_add(1)
                    index -= 1
                # End of loop
                index += 8
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 6
                while data[index] != 0:
                    bf_sub(1)
                    index -= 5
                    bf_add(1)
                    index += 5
                # End of loop
                index -= 5
                while data[index] != 0:
                    bf_sub(1)
                    index += 5
                    bf_add(1)
                    index -= 3
                    bf_add(1)
                    index -= 2
                # End of loop
                index += 8
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            bf_add(15)
            while data[index] != 0:
                while data[index] != 0:
                    index += 4
                    index += 5
                # End of loop
                bf_add(1)
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index -= 9
                while data[index] != 0:
                    index -= 9
                # End of loop
                index += 9
                bf_sub(1)
            # End of loop
            bf_add(1)
            while data[index] != 0:
                index += 1
                bf_add(1)
                index += 2
                index += 6
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 1
                bf_sub(1)
                index += 4
                while data[index] != 0:
                    bf_sub(1)
                    index -= 4
                    bf_add(1)
                    index += 4
                # End of loop
                index -= 4
                while data[index] != 0:
                    bf_sub(1)
                    index += 4
                    bf_add(1)
                    index -= 5
                    while data[index] != 0:
                        bf_sub(1)
                        index += 2
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 2
                            bf_add(1)
                            index += 2
                        # End of loop
                        index -= 2
                        while data[index] != 0:
                            bf_sub(1)
                            index += 2
                            bf_add(1)
                            index += 2
                            bf_add(1)
                            index -= 4
                        # End of loop
                        bf_add(1)
                        index += 9
                    # End of loop
                    index -= 8
                    while data[index] != 0:
                        index -= 9
                    # End of loop
                # End of loop
                index += 9
                while data[index] != 0:
                    index += 9
                # End of loop
                index -= 9
                while data[index] != 0:
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 9
                        bf_add(1)
                        index -= 9
                    # End of loop
                    index -= 10
                # End of loop
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                    index += 9
                    bf_add(1)
                    index -= 9
                # End of loop
                index -= 1
                bf_add(1)
                index += 8
            # End of loop
            index -= 9
            while data[index] != 0:
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index -= 1
                bf_sub(1)
                index += 4
                while data[index] != 0:
                    bf_sub(1)
                    index -= 4
                    bf_add(1)
                    index += 1
                    while data[index] != 0:
                        index -= 1
                        bf_sub(1)
                        index += 1
                        bf_sub(1)
                        index -= 6
                        bf_add(1)
                        index += 6
                    # End of loop
                    index -= 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 1
                        bf_add(1)
                        index -= 1
                    # End of loop
                    index += 4
                # End of loop
                index -= 3
                while data[index] != 0:
                    bf_sub(1)
                    index += 3
                    bf_add(1)
                    index -= 3
                # End of loop
                index -= 1
                bf_add(1)
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 1
                bf_add(1)
                index += 8
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 1
                bf_sub(1)
                index += 5
                while data[index] != 0:
                    bf_sub(1)
                    index -= 5
                    bf_add(1)
                    index += 5
                # End of loop
                index -= 5
                while data[index] != 0:
                    bf_sub(1)
                    index += 5
                    bf_add(1)
                    index -= 4
                    index -= 2
                    while data[index] != 0:
                        bf_sub(1)
                        index += 3
                        while data[index] != 0:
                            bf_sub(1)
                            index -= 3
                            bf_add(1)
                            index += 3
                        # End of loop
                        index -= 3
                        while data[index] != 0:
                            bf_sub(1)
                            index += 3
                            bf_add(1)
                            index += 1
                            bf_add(1)
                            index -= 4
                        # End of loop
                        bf_add(1)
                        index += 9
                    # End of loop
                    index -= 8
                    while data[index] != 0:
                        index -= 9
                    # End of loop
                # End of loop
                index += 9
                while data[index] != 0:
                    index += 6
                    index += 3
                # End of loop
                index -= 9
                while data[index] != 0:
                    index += 2
                    while data[index] != 0:
                        bf_sub(1)
                        index += 9
                        bf_add(1)
                        index -= 9
                    # End of loop
                    index -= 11
                # End of loop
                index += 2
                while data[index] != 0:
                    bf_sub(1)
                    index += 9
                    bf_add(1)
                    index -= 9
                # End of loop
                index -= 2
                bf_add(1)
                index += 3
                index += 5
            # End of loop
            index -= 9
            while data[index] != 0:
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index -= 1
                bf_sub(1)
                index += 4
                while data[index] != 0:
                    bf_sub(1)
                    index -= 4
                    bf_add(1)
                    index += 1
                    while data[index] != 0:
                        index -= 1
                        bf_sub(1)
                        index += 1
                        bf_sub(1)
                        index -= 6
                        bf_add(1)
                        index += 6
                    # End of loop
                    index -= 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 1
                        bf_add(1)
                        index -= 1
                    # End of loop
                    index += 4
                # End of loop
                index -= 3
                while data[index] != 0:
                    bf_sub(1)
                    index += 3
                    bf_add(1)
                    index -= 3
                # End of loop
                index -= 1
                bf_add(1)
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 4
                while data[index] != 0:
                    bf_sub(1)
                    index -= 36
                    bf_add(1)
                    index += 17
                    index += 19
                # End of loop
                index += 5
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            bf_add(15)
            while data[index] != 0:
                while data[index] != 0:
                    index += 8
                    index += 1
                # End of loop
                index -= 9
                bf_sub(1)
                index -= 9
                while data[index] != 0:
                    index -= 9
                # End of loop
                index += 9
                bf_sub(1)
            # End of loop
            bf_add(1)
            index += 21
            bf_add(1)
            index -= 3
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 3
                while data[index] != 0:
                    bf_sub(1)
                    index -= 3
                    bf_sub(1)
                    index += 3
                # End of loop
                bf_add(1)
                index -= 3
                while data[index] != 0:
                    bf_sub(1)
                    index += 3
                    bf_sub(1)
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 4
                        bf_add(1)
                        index += 4
                    # End of loop
                    index -= 4
                    while data[index] != 0:
                        bf_sub(1)
                        index += 4
                        bf_add(1)
                        index -= 13
                        while data[index] != 0:
                            index -= 9
                        # End of loop
                        index += 4
                        while data[index] != 0:
                            bf_sub(1)
                        # End of loop
                        bf_add(1)
                        index += 5
                        while data[index] != 0:
                            index += 9
                        # End of loop
                        index += 1
                        bf_add(1)
                        index -= 1
                    # End of loop
                # End of loop
                bf_add(1)
                index += 4
                while data[index] != 0:
                    bf_sub(1)
                    index -= 4
                    bf_sub(1)
                    index += 4
                # End of loop
                bf_add(1)
                index -= 4
                while data[index] != 0:
                    bf_sub(1)
                    index += 4
                    bf_sub(1)
                    index -= 1
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 3
                        bf_add(1)
                        index += 3
                    # End of loop
                    index -= 3
                    while data[index] != 0:
                        bf_sub(1)
                        index += 3
                        bf_add(1)
                        index -= 1
                        index -= 11
                        while data[index] != 0:
                            index -= 9
                        # End of loop
                        index += 3
                        while data[index] != 0:
                            bf_sub(1)
                        # End of loop
                        bf_add(1)
                        index += 6
                        while data[index] != 0:
                            index += 9
                        # End of loop
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                        # End of loop
                        bf_add(1)
                        index -= 1
                    # End of loop
                # End of loop
                bf_add(1)
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                    index -= 1
                    while data[index] != 0:
                        index += 9
                    # End of loop
                    index -= 8
                # End of loop
                index += 1
                index += 7
            # End of loop
            index -= 9
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 2
            bf_sub(1)
            index += 2
            while data[index] != 0:
                bf_sub(1)
                index -= 4
                bf_add(1)
                index += 4
            # End of loop
            index -= 4
            while data[index] != 0:
                bf_sub(1)
                index += 4
                bf_add(1)
                index -= 2
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index -= 2
            # End of loop
            index += 2
        # End of loop
        index -= 2
        bf_add(1)
        index += 4
        while data[index] != 0:
            bf_sub(1)
            index -= 4
            bf_sub(1)
            index += 4
        # End of loop
        bf_add(1)
        index -= 4
        while data[index] != 0:
            bf_sub(1)
            index += 4
            bf_sub(1)
            index -= 6
            bf_output()
            index += 2
        # End of loop
        index += 4
        while data[index] != 0:
            bf_sub(1)
            index -= 7
            bf_output()
            index += 7
        # End of loop
        index -= 3
        while data[index] != 0:
            bf_sub(1)
        # End of loop
        index += 1
        while data[index] != 0:
            bf_sub(1)
        # End of loop
        index += 1
        while data[index] != 0:
            bf_sub(1)
        # End of loop
        index += 1
        while data[index] != 0:
            bf_sub(1)
        # End of loop
        index += 1
        while data[index] != 0:
            bf_sub(1)
        # End of loop
        index += 1
        while data[index] != 0:
            bf_sub(1)
        # End of loop
        index += 3
        while data[index] != 0:
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 3
        # End of loop
        index -= 9
        while data[index] != 0:
            index -= 9
        # End of loop
        index += 9
        while data[index] != 0:
            index += 5
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 4
        # End of loop
        index -= 9
        while data[index] != 0:
            index -= 9
        # End of loop
        index += 1
        bf_add(11)
        while data[index] != 0:
            bf_sub(1)
            while data[index] != 0:
                bf_sub(1)
                index += 9
                bf_add(1)
                index -= 9
            # End of loop
            index += 9
        # End of loop
        index += 4
        bf_add(1)
        index += 9
        bf_add(1)
        index -= 8
        index -= 6
        while data[index] != 0:
            index -= 9
        # End of loop
        index += 7
        while data[index] != 0:
            bf_sub(1)
            index -= 7
            bf_add(1)
            index += 7
        # End of loop
        index -= 7
        while data[index] != 0:
            bf_sub(1)
            index += 7
            bf_add(1)
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index += 2
            while data[index] != 0:
                index += 9
            # End of loop
            index -= 5
            index -= 4
            while data[index] != 0:
                index += 7
                while data[index] != 0:
                    bf_sub(1)
                    index -= 6
                    bf_add(1)
                    index += 6
                # End of loop
                index -= 6
                while data[index] != 0:
                    bf_sub(1)
                    index += 6
                    bf_add(1)
                    index -= 7
                    while data[index] != 0:
                        index -= 9
                    # End of loop
                    index += 7
                    while data[index] != 0:
                        bf_sub(1)
                    # End of loop
                    bf_add(1)
                    index += 3
                # End of loop
                index -= 4
                index -= 6
            # End of loop
        # End of loop
        index += 7
        while data[index] != 0:
            bf_sub(1)
            index -= 7
            bf_add(1)
            index += 7
        # End of loop
        index -= 7
        while data[index] != 0:
            bf_sub(1)
            index += 7
            bf_add(1)
            index += 2
            while data[index] != 0:
                index += 1
                bf_add(1)
                index += 4
                while data[index] != 0:
                    bf_sub(1)
                    index -= 4
                    bf_sub(1)
                    index += 4
                # End of loop
                index -= 4
                while data[index] != 0:
                    bf_sub(1)
                    index += 3
                    index += 1
                    bf_add(1)
                    index -= 4
                # End of loop
                index += 8
            # End of loop
            index -= 2
            bf_add(1)
            index -= 7
            while data[index] != 0:
                index += 5
                while data[index] != 0:
                    bf_sub(1)
                    index += 2
                    bf_add(1)
                    index -= 2
                # End of loop
                index -= 14
            # End of loop
            index += 9
            while data[index] != 0:
                index += 9
            # End of loop
            index -= 5
            index -= 4
            while data[index] != 0:
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index -= 1
                bf_sub(1)
                index += 7
                while data[index] != 0:
                    bf_sub(1)
                    index -= 7
                    bf_add(1)
                    index += 1
                    while data[index] != 0:
                        index -= 1
                        bf_sub(1)
                        index += 1
                        bf_sub(1)
                        index -= 3
                        bf_add(1)
                        index += 3
                    # End of loop
                    index -= 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 1
                        bf_add(1)
                        index -= 1
                    # End of loop
                    index += 7
                # End of loop
                index -= 6
                while data[index] != 0:
                    bf_sub(1)
                    index += 6
                    bf_add(1)
                    index -= 6
                # End of loop
                index -= 1
                bf_add(1)
                index -= 9
            # End of loop
            index += 7
            bf_sub(1)
            index -= 4
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            bf_add(1)
            index -= 3
        # End of loop
        bf_add(1)
        index += 7
        while data[index] != 0:
            bf_sub(1)
            index -= 7
            bf_sub(1)
            index += 7
        # End of loop
        bf_add(1)
        index -= 7
        while data[index] != 0:
            bf_sub(1)
            index += 7
            bf_sub(1)
            index += 2
            while data[index] != 0:
                index += 2
                index += 3
                while data[index] != 0:
                    bf_sub(1)
                    index += 2
                    bf_add(1)
                    index -= 2
                # End of loop
                index += 4
            # End of loop
            index -= 9
            while data[index] != 0:
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                index -= 1
                bf_sub(1)
                index += 7
                while data[index] != 0:
                    bf_sub(1)
                    index -= 7
                    bf_add(1)
                    index += 1
                    while data[index] != 0:
                        index -= 1
                        bf_sub(1)
                        index += 1
                        bf_sub(1)
                        index -= 3
                        bf_add(1)
                        index += 3
                    # End of loop
                    index -= 1
                    while data[index] != 0:
                        bf_sub(1)
                        index += 1
                        bf_add(1)
                        index -= 1
                    # End of loop
                    index += 7
                # End of loop
                index -= 2
                index -= 4
                while data[index] != 0:
                    bf_sub(1)
                    index += 6
                    bf_add(1)
                    index -= 6
                # End of loop
                index -= 1
                bf_add(1)
                index -= 9
            # End of loop
            index += 1
            bf_add(5)
            while data[index] != 0:
                bf_sub(1)
                while data[index] != 0:
                    bf_sub(1)
                    index += 9
                    bf_add(1)
                    index -= 9
                # End of loop
                index += 9
            # End of loop
            index += 4
            bf_add(1)
            index -= 3
            index -= 2
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 9
            while data[index] != 0:
                index += 5
                while data[index] != 0:
                    bf_sub(1)
                    index -= 5
                    bf_sub(1)
                    index += 5
                # End of loop
                bf_add(1)
                index -= 5
                while data[index] != 0:
                    bf_sub(1)
                    index += 5
                    bf_sub(1)
                    index += 2
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 7
                        bf_add(1)
                        index += 7
                    # End of loop
                    index -= 4
                    index -= 3
                    while data[index] != 0:
                        bf_sub(1)
                        index += 7
                        bf_add(1)
                        index -= 16
                        while data[index] != 0:
                            index -= 9
                        # End of loop
                        index += 4
                        while data[index] != 0:
                            bf_sub(1)
                        # End of loop
                        bf_add(1)
                        index += 5
                        while data[index] != 0:
                            index += 9
                        # End of loop
                        index += 1
                        bf_add(1)
                        index -= 1
                    # End of loop
                # End of loop
                bf_add(1)
                index += 7
                while data[index] != 0:
                    bf_sub(1)
                    index -= 1
                    index -= 6
                    bf_sub(1)
                    index += 7
                # End of loop
                bf_add(1)
                index -= 7
                while data[index] != 0:
                    bf_sub(1)
                    index += 7
                    bf_sub(1)
                    index -= 2
                    while data[index] != 0:
                        bf_sub(1)
                        index -= 5
                        bf_add(1)
                        index += 5
                    # End of loop
                    index -= 5
                    while data[index] != 0:
                        bf_sub(1)
                        index += 5
                        bf_add(1)
                        index -= 14
                        while data[index] != 0:
                            index -= 3
                            index -= 6
                        # End of loop
                        index += 3
                        while data[index] != 0:
                            bf_sub(1)
                        # End of loop
                        bf_add(1)
                        index += 6
                        while data[index] != 0:
                            index += 9
                        # End of loop
                        index += 1
                        while data[index] != 0:
                            bf_sub(1)
                        # End of loop
                        bf_add(1)
                        index -= 1
                    # End of loop
                # End of loop
                bf_add(1)
                index += 1
                while data[index] != 0:
                    bf_sub(1)
                    index -= 1
                    while data[index] != 0:
                        index += 9
                    # End of loop
                    index -= 8
                # End of loop
                index += 8
            # End of loop
            index -= 7
            index -= 2
            while data[index] != 0:
                index -= 9
            # End of loop
            index += 4
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index -= 3
            bf_add(5)
            while data[index] != 0:
                bf_sub(1)
                while data[index] != 0:
                    bf_sub(1)
                    index += 9
                    bf_add(1)
                    index -= 9
                # End of loop
                index += 9
            # End of loop
            index += 4
            bf_sub(1)
            index -= 5
            while data[index] != 0:
                index -= 7
                index -= 2
            # End of loop
        # End of loop
        index += 3
    # End of loop
    index -= 4
    bf_output()
    index += 10
    while data[index] != 0:
        index += 6
        while data[index] != 0:
            bf_sub(1)
        # End of loop
        index += 3
    # End of loop
    index -= 9
    while data[index] != 0:
        index -= 9
    # End of loop
    index += 1
    bf_add(10)
    while data[index] != 0:
        bf_sub(1)
        while data[index] != 0:
            bf_sub(1)
            index += 8
            index += 1
            bf_add(1)
            index -= 9
        # End of loop
        index += 9
    # End of loop
    index += 5
    bf_add(1)
    index += 9
    bf_add(1)
    index -= 15
    while data[index] != 0:
        index -= 9
    # End of loop
    index += 8
    while data[index] != 0:
        bf_sub(1)
        index -= 6
        index -= 2
        bf_add(1)
        index += 8
    # End of loop
    index -= 8
    while data[index] != 0:
        bf_sub(1)
        index += 8
        bf_add(1)
        while data[index] != 0:
            bf_sub(1)
        # End of loop
        index += 1
        while data[index] != 0:
            index += 9
        # End of loop
        index -= 9
        while data[index] != 0:
            index += 8
            while data[index] != 0:
                bf_sub(1)
                index -= 7
                bf_add(1)
                index += 6
                index += 1
            # End of loop
            index -= 7
            while data[index] != 0:
                bf_sub(1)
                index += 7
                bf_add(1)
                index -= 8
                while data[index] != 0:
                    index -= 9
                # End of loop
                index += 8
                while data[index] != 0:
                    bf_sub(1)
                # End of loop
                bf_add(1)
                index += 2
            # End of loop
            index -= 10
        # End of loop
    # End of loop
    index += 8
    while data[index] != 0:
        bf_sub(1)
        index -= 5
        index -= 3
        bf_add(1)
        index += 8
    # End of loop
    index -= 8
    while data[index] != 0:
        bf_sub(1)
        index += 8
        bf_add(1)
        index += 1
        while data[index] != 0:
            index += 1
            bf_add(1)
            index += 5
            while data[index] != 0:
                bf_sub(1)
                index -= 5
                bf_sub(1)
                index += 5
            # End of loop
            index -= 5
            while data[index] != 0:
                bf_sub(1)
                index += 5
                bf_add(1)
                index -= 5
            # End of loop
            index += 6
            index += 2
        # End of loop
        index -= 1
        bf_add(1)
        index -= 8
        while data[index] != 0:
            index += 6
            while data[index] != 0:
                bf_sub(1)
                index += 2
                bf_add(1)
                index -= 2
            # End of loop
            index -= 15
        # End of loop
        index += 9
        while data[index] != 0:
            index += 9
        # End of loop
        index -= 9
        while data[index] != 0:
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index -= 1
            bf_sub(1)
            index += 8
            while data[index] != 0:
                bf_sub(1)
                index -= 8
                bf_add(1)
                index += 1
                while data[index] != 0:
                    index -= 1
                    bf_sub(1)
                    index += 1
                    bf_sub(1)
                    index -= 2
                    bf_add(1)
                    index += 2
                # End of loop
                index -= 1
                while data[index] != 0:
                    bf_sub(1)
                    index += 1
                    bf_add(1)
                    index -= 1
                # End of loop
                index += 8
            # End of loop
            index -= 7
            while data[index] != 0:
                bf_sub(1)
                index += 7
                bf_add(1)
                index -= 7
            # End of loop
            index -= 1
            bf_add(1)
            index -= 6
            index -= 3
        # End of loop
        index += 8
        bf_sub(1)
        index -= 5
        while data[index] != 0:
            bf_sub(1)
        # End of loop
        bf_add(1)
        index -= 3
    # End of loop
    bf_add(1)
    index += 8
    while data[index] != 0:
        bf_sub(1)
        index -= 8
        bf_sub(1)
        index += 8
    # End of loop
    bf_add(1)
    index -= 8
    while data[index] != 0:
        bf_sub(1)
        index += 8
        bf_sub(1)
        index += 1
        while data[index] != 0:
            index += 3
            index += 3
            while data[index] != 0:
                bf_sub(1)
                index += 2
                bf_add(1)
                index -= 2
            # End of loop
            index += 3
        # End of loop
        index -= 9
        while data[index] != 0:
            index += 1
            while data[index] != 0:
                bf_sub(1)
            # End of loop
            index -= 1
            bf_sub(1)
            index += 8
            while data[index] != 0:
                bf_sub(1)
                index -= 8
                bf_add(1)
                index += 1
                while data[index] != 0:
                    index -= 1
                    bf_sub(1)
                    index += 1
                    bf_sub(1)
                    index -= 2
                    bf_add(1)
                    index += 2
                # End of loop
                index -= 1
                while data[index] != 0:
                    bf_sub(1)
                    index += 1
                    bf_add(1)
                    index -= 1
                # End of loop
                index += 8
            # End of loop
            index -= 2
            index -= 5
            while data[index] != 0:
                bf_sub(1)
                index += 7
                bf_add(1)
                index -= 7
            # End of loop
            index -= 1
            bf_add(1)
            index -= 9
        # End of loop
        index += 1
        bf_add(5)
        while data[index] != 0:
            bf_sub(1)
            while data[index] != 0:
                bf_sub(1)
                index += 9
                bf_add(1)
                index -= 9
            # End of loop
            index += 9
        # End of loop
        index += 5
        bf_add(1)
        index += 27
        bf_add(1)
        index -= 6
        while data[index] != 0:
            index -= 9
        # End of loop
        index += 9
        while data[index] != 0:
            index += 6
            while data[index] != 0:
                bf_sub(1)
                index -= 6
                bf_sub(1)
                index += 6
            # End of loop
            bf_add(1)
            index -= 1
            index -= 5
            while data[index] != 0:
                bf_sub(1)
                index += 6
                bf_sub(1)
                index += 2
                while data[index] != 0:
                    bf_sub(1)
                    index -= 8
                    bf_add(1)
                    index += 8
                # End of loop
                index -= 8
                while data[index] != 0:
                    bf_sub(1)
                    index += 8
                    bf_add(1)
                    index -= 17
                    while data[index] != 0:
                        index -= 7
                        index -= 2
                    # End of loop
                    index += 4
                    while data[index] != 0:
                        bf_sub(1)
                    # End of loop
                    bf_add(1)
                    index += 5
                    while data[index] != 0:
                        index += 9
                    # End of loop
                    index += 1
                    bf_add(1)
                    index -= 1
                # End of loop
            # End of loop
            bf_add(1)
            index += 8
            while data[index] != 0:
                bf_sub(1)
                index -= 8
                bf_sub(1)
                index += 8
            # End of loop
            bf_add(1)
            index -= 8
            while data[index] != 0:
                bf_sub(1)
                index += 8
                bf_sub(1)
                index -= 2
                while data[index] != 0:
                    bf_sub(1)
                    index -= 6
                    bf_add(1)
                    index += 6
                # End of loop
                index -= 6
                while data[index] != 0:
                    bf_sub(1)
                    index += 6
                    bf_add(1)
                    index -= 15
                    while data[index] != 0:
                        index -= 9
                    # End of loop
                    index += 3
                    while data[index] != 0:
                        bf_sub(1)
                    # End of loop
                    bf_add(1)
                    index += 6
                    while data[index] != 0:
                        index += 6
                        index += 3
                    # End of loop
                    index += 1
                    while data[index] != 0:
                        bf_sub(1)
                    # End of loop
                    bf_add(1)
                    index -= 1
                # End of loop
            # End of loop
            bf_add(1)
            index += 1
            while data[index] != 0:
                bf_sub(1)
                index -= 1
                while data[index] != 0:
                    index += 9
                # End of loop
                index -= 8
            # End of loop
            index += 8
        # End of loop
        index -= 9
        while data[index] != 0:
            index -= 9
        # End of loop
        index += 4
        while data[index] != 0:
            bf_sub(1)
        # End of loop
        index -= 3
        bf_add(4)
        bf_add(1)
        while data[index] != 0:
            bf_sub(1)
            while data[index] != 0:
                bf_sub(1)
                index += 9
                bf_add(1)
                index -= 9
            # End of loop
            index += 9
        # End of loop
        index += 5
        bf_sub(1)
        index += 27
        bf_sub(1)
        index -= 6
        while data[index] != 0:
            index -= 4
            index -= 5
        # End of loop
    # End of loop
    index += 3
# End of loop