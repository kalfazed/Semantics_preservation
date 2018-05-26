block_data = []
with open("input.mtg") as file:
    for line in file:
        block_data.append(line.split(None, 1)[0])

    print block_data
    
