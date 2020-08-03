def find_first(string, char):
    found = False
    for i in range(len(string)):
        if string[i] == char:
            found = True
            break
    if found:
        return i
    else:
        return -1
