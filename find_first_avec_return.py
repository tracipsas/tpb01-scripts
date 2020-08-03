def find_first(string, char):
    for i in range(len(string)):
        if string[i] == char:
            return i
    return -1
