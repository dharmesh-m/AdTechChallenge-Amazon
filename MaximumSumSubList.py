gsum = None


""" Helper function for DFS """

def getMaxSumHelper(ar, index, acc):
    global gsum
    if index >= len(ar):
        return    
    acc = acc + ar[index]
    if gsum == None or acc > gsum:
        gsum = acc
    for i in xrange(index + 2, len(ar)):
        getMaxSumHelper(ar, i, acc)


""" Function which calculates the maximum sum
    This is entry point """

def getMaxSum(ar):
    for i in range(len(ar)):
        getMaxSumHelper(ar, i, 0)
    
if __name__ == "__main__":
    ar = [-2,-1,-16]
    getMaxSum(ar)
    print gsum
