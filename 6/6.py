# Day 6

START_OF_PACKET_LEN = 4
START_OF_MESSAGE_LEN = 14

def loadData(path="input.txt"):
    """Loads data from text-file at provided path. Returns full file contents."""
    with open(path, "r") as inputFile:
        return inputFile.read()

def findFirstNUnique(seq, n):
    """Returns how many characters before the last n were all unique. Returns the length of the sequence up to and including n unqiue elements."""
    for i in range(len(seq) - n):
        runner = set([seq[j] for j in range(i, i + n)])
        if len(runner) == n:
            return i + n
    return -1

def main():
    data = loadData()
    sop = findFirstNUnique(data, START_OF_PACKET_LEN)
    som = findFirstNUnique(data, START_OF_MESSAGE_LEN)
    print("The first start-of-packet marker (length %d) is after %d characters." % (START_OF_PACKET_LEN, sop))
    print("The first start-of-message marker (length %d) is after %d characters." % (START_OF_MESSAGE_LEN, som))



if __name__ == "__main__":
    main()
