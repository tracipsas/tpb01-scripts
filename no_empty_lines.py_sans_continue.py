with open("data.txt", "r", encoding="utf-8") as file:
    for i, line in enumerate(file):
        if len(line.strip()) != 0:
            line = line.upper().strip()
            nb_chars = len(line)
            print("{}: {} ({} caractères)".format(i + 1, line, nb_chars))
