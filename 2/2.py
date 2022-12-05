# Day 2

def loadData(path="input.txt"):
    """Loads data from text-file at provided path. Returns full file contents."""
    with open(path, "r") as inputFile:
        return inputFile.read()

def rps(opponentShape, myShape):
    # Convert shapes into numbers [0, 1, 2]
    o = ord(opponentShape) - ord("A")
    # m = ord(myShape) - ord("X")                   # 1st part
    m = (o + (ord(myShape) - ord("X") - 1 )) % 3    # 2nd part

    # Give points based on shapes:
    opponentPoints = o + 1
    myPoints = m + 1

    # Determine winner:
    diff = o - m
    if diff == 1 or diff == -2:
        opponentPoints += 6
    elif diff == -1 or diff == 2:
        myPoints += 6
    elif diff == 0:
        opponentPoints += 3
        myPoints += 3
    
    return opponentPoints, myPoints


def main():
    data = loadData()
    shapes = [row.split(" ") for row in data.split("\n")]
    
    opponentPoints = 0
    myPoints = 0
    for round in shapes:
        o, m = rps(*round)
        opponentPoints += o
        myPoints += m
    
    print("After following the strategy guide your score will be %d points. Your opponents score will be %d." % (myPoints, opponentPoints))


if __name__ == "__main__":
    main()
