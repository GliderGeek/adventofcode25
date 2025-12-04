from pathlib import Path
import math


# file_path = Path(__file__).parent / 'example.txt'
file_path = Path(__file__).parent / 'input.txt'

print(f'running with {file_path.parts[-1]}')


# part 1

grid = []
neighbours = []    # how many neighbouring
with open(file_path) as f:
    for line in f.read().splitlines():
        grid.append([char=='@' for char in line])
        neighbours.append([0 for char in line])


def increment_if_exists(_grid, _i, _j):
    # make sure no negative indices are used
    if _i < 0 or _j < 0:
        return

    try:
        _grid[_i][_j] += 1
    except IndexError:
        pass


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]:
            increment_if_exists(neighbours, i-1, j-1)
            increment_if_exists(neighbours, i-1, j)
            increment_if_exists(neighbours, i-1, j+1)
            increment_if_exists(neighbours, i, j-1)
            increment_if_exists(neighbours, i, j+1)
            increment_if_exists(neighbours, i+1, j-1)
            increment_if_exists(neighbours, i+1, j)
            increment_if_exists(neighbours, i+1, j+1)

sum = 0
for i in range(len(grid)):
    print_line = []
    for j in range(len(grid[0])):
        if grid[i][j] and neighbours[i][j] < 4:
            sum += 1


print('solution 1:', sum)


# part 2


removed_total = 0

while True:

    # TODO: why [[0]*j]*i does not work?

    # empty neighbours matrix
    neighbours = []
    for i in range(len(grid)):
        neighbours.append([0 for j in range(len(grid[0]))])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                increment_if_exists(neighbours, i-1, j-1)
                increment_if_exists(neighbours, i-1, j)
                increment_if_exists(neighbours, i-1, j+1)
                increment_if_exists(neighbours, i, j-1)
                increment_if_exists(neighbours, i, j+1)
                increment_if_exists(neighbours, i+1, j-1)
                increment_if_exists(neighbours, i+1, j)
                increment_if_exists(neighbours, i+1, j+1)

    removed = 0
    for i in range(len(grid)):
        print_line = []
        for j in range(len(grid[0])):
            if grid[i][j] and neighbours[i][j] < 4:
                grid[i][j] = False
                removed += 1

    # print('removed', removed)

    if removed == 0:
        break
    else:
        removed_total += removed

print('solution 2:', removed_total)
