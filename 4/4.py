# Day 4

def loadData(path="input.txt"):
    """Loads data from text-file at provided path. Returns full file contents."""
    with open(path, "r") as inputFile:
        return inputFile.read()

def part1(sections):
    """Counts and returns how many sections in provided data have full overlap between pairs."""
    count = 0
    for pair in sections:
        inter = pair[0].intersection(pair[1])
        if inter == pair[0] or inter == pair[1]:    # Full overlap means the intersection will equal one of the sets.
            count += 1
    return count

def part2(sections):
    """Counts and returns how many sections in provided data have any overlap between pairs."""
    count = 0
    for pair in sections:
        if len(pair[0].intersection(pair[1])):  # If there exists an intersection, the pairs overlap.
            count += 1
    return count

def main():
    data = loadData()

    sections = list()
    for row in data.split("\n"):
        section = list()
        for sec in row.split(","):
            nums = [int(num) for num in sec.split("-")]
            section.append(set(range(nums[0], nums[1] + 1)))
        sections.append(section)
    
    count1 = part1(sections)    
    print("Number of pairs with full overlap: %d" % count1)

    count2 = part2(sections)    
    print("Number of pairs with any overlap: %d" % count2)

if __name__ == "__main__":
    main()
