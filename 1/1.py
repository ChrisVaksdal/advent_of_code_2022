# Day 1

def loadData(path="input.txt"):
    """Loads data from text-file at provided path. Returns full file contents."""
    with open(path, "r") as inputFile:
        return inputFile.read()

def getHighestNumber(elves):
    """Returns tuple of highest number in list and its index."""
    totals = [sum(elf) for elf in elves]
    highest = max(totals)
    index = totals.index(highest)
    return highest, index


def main():
    data = loadData()
    elves = [list()]    # All the elves' inventories.

    # Split data into separate elf-inventories:
    index = 0
    for row in data.split("\n"):
        if row == "":
            elves.append(list())
            index += 1
            continue
        elves[index].append(int(row))


    N = 3 # How many elves to be selected.
    richestElves = list()
    richestIndices = list()
    for _ in range(N):
        richestElf, richestIndex = getHighestNumber(elves)
        richestElves.append(richestElf)
        richestIndices.append(richestIndex)
        del(elves[richestIndex])


    # Print results:
    print("The %d elves with the most calories are:" % N)
    [print("Elf %d, with %d calories." % (richestIndices[index] + 1, calorieCount)) for index, calorieCount in enumerate(richestElves)]
    print("The total number of calories carried by these elves is %d." % sum(richestElves))
    

if __name__ == "__main__":
    main()
