# Day 3

def loadData(path="input.txt"):
    """Loads data from text-file at provided path. Returns full file contents."""
    with open(path, "r") as inputFile:
        return inputFile.read()

def getItemPriority(item):
    if item.isupper():
        return ord(item) - ord("A") + 27
    else:
        return ord(item) - ord("a") + 1

def part1(data):
    sacks = [(sack[:len(sack)//2], sack[len(sack)//2:]) for sack in data.split("\n")]   # Convert data into sacks with tuples of compartments.

    p = 0
    for sack in sacks:
        for item in sack[0]:
            if item in sack[1]:
                p += getItemPriority(item)
                break
                
    return p

def part2(data):
    sacks = [sack for sack in data.split("\n")]
    p = 0
    for i in range(0, len(sacks), 3):
        s0 = set(sacks[i])
        s1 = set(sacks[i + 1])
        s2 = set(sacks[i + 2])

        badge = "".join(s0.intersection(s1).intersection(s2))
        p += getItemPriority(badge)
    return p

def main():
    data = loadData()
    
    p1 = part1(data)
    print("Sum of priorities of double-packed items: %d" % p1)

    p2 = part2(data)
    print("Sum of priorities of badges: %d" % p2)


if __name__ == "__main__":
    main()
