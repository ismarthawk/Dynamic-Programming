memo = dict()


def gridTravelRec(row, col) :
    if row == 0 or col == 0 : return 0
    if row == 1 and col == 1 : return 1
    return gridTravel(row - 1, col) + gridTravel(row, col - 1)

def gridTravel(row, col, memo) :
    if row == 0 or col == 0 : return 0
    if row == 1 and col == 1 : return 1
    if (row, col) in memo : return memo[(row, col)]
    memo[(row, col)]  = gridTravel(row -1, col, memo) + gridTravel(row, col -1, memo)
    return memo[(row, col)]

print(gridTravel(10, 20, memo))
