with open("input.mtg") as file:
    data = file.read()

    for line in data :
        words = line.split()
        print words
