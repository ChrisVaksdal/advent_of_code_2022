# Day 5

def loadData(path="input.txt"):
    """Loads data from text-file at provided path. Returns full file contents."""
    with open(path, "r") as inputFile:
        return inputFile.read()

def parseCmd(cmd):
    """Returns usable parameters from cmd where cmd is in form 'move <num> from <f> to <t>'."""
    parts = cmd.split()
    num = int(parts[1])
    f = int(parts[3]) - 1
    t = int(parts[5]) - 1
    return num, f, t

def getCrateTops(crates):
    """Returns a single string containing the topmost item in all the provided crates in order."""
    return "".join([crate[-1] for crate in crates])

def crateMaster9000(crates, cmds):
    for cmd in cmds:
        num, f, t = parseCmd(cmd)
        [crates[t].append(crates[f].pop()) for _ in range(num)]
    
    top = getCrateTops(crates)
    return top

def crateMaster9001(crates, cmds):
    for cmd in cmds:
        num, f, t = parseCmd(cmd)
        # Move one column at a time instead.
        temp = crates[f][-num:]
        crates[f] = crates[f][:-num]
        crates[t] += temp

    top = getCrateTops(crates)
    return top

def main():
    data = loadData().split("\n")

    split = data.index("")
    init = data[:split]
    cmds = data[split + 1:]

    # Create initial state of all crates:
    numCrates = len(init.pop().split())
    crates = [list() for _ in range(numCrates)]

    for row in init:
        for i, w in enumerate(range(1, len(row), 4)):
            if row[w] != " ":
                crates[i].insert(0, row[w])
    
    # top = crateMaster9000(crates, cmds)
    top = crateMaster9001(crates, cmds)
    
    print("After the moving procedure the following crates will be on top: %s" % top)
    


if __name__ == "__main__":
    main()
