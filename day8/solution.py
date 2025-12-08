from pathlib import Path
import math
import re


# file_path = Path(__file__).parent / 'example.txt'
# connections = 10

file_path = Path(__file__).parent / 'input.txt'
connections = 1000

print(f'running with {file_path.parts[-1]}')


# part 1

locations = []
with open(file_path) as f:
    for line in f.read().splitlines():
        loc = [int(val) for val in line.split(',')]
        locations.append(loc)

# print(locations)

distances = {}
for i, location1 in enumerate(locations):
    min_dist = None
    for j, location2 in enumerate(locations):
        if i == j:
            continue

        if (i,j) in distances or (j,i) in distances:
            continue

        dist = (location2[0] - location1[0])**2 + (location2[1] - location1[1])**2 + (location2[2] - location1[2])**2
        distances[(i, j)] = dist

sorted_locs = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
# print(sorted_locs)

# part 1

circuits = {}
circuit_number = 1
connection = 0
for (ind1, ind2), _ in sorted_locs.items():
    # print(ind1, ind2)
    if ind1 not in circuits and ind2 not in circuits:
        circuits[ind1] = circuit_number
        circuits[ind2] = circuit_number
        circuit_number += 1
    elif ind1 not in circuits and ind2 in circuits:
        circuits[ind1] = circuits[ind2]
    elif ind1 in circuits and ind2 not in circuits:
        circuits[ind2] = circuits[ind1]
    else:  #  ind1 in circuits and ind2 in circuits
        # remap from ind1 to ind2 (join circuits)
        if circuits[ind1] != circuits[ind2]:
            # print('here', ind1, ind2)
            orig_circuit = circuits[ind1]
            for k, v in circuits.items():
                if v == orig_circuit:
                    circuits[k] = circuits[ind2]
        else:
            # same circuit, nothing happens
            pass

    # print(circuits)

    connection += 1
    if connection >= connections:
        break

circuit_sizes = {}
for circuit_number in circuits.values():
    if circuit_number in circuit_sizes:
        circuit_sizes[circuit_number] += 1
    else:
        circuit_sizes[circuit_number] = 1

# print(circuit_sizes)

sorted_sizes = [v for k, v in sorted(circuit_sizes.items(), key=lambda item: item[1], reverse=True)]

total = 1
for i in range(3):
    total = total * sorted_sizes[i]

print('solution 1:', total)




# part 2

circuits = {}
circuit_number = 1
nr_circuits = 0
solution = 0
for (ind1, ind2), _ in sorted_locs.items():
    # print(f'({ind1}, {ind2})')
    if ind1 not in circuits and ind2 not in circuits:
        circuits[ind1] = circuit_number
        circuits[ind2] = circuit_number
        circuit_number += 1
        nr_circuits += 1
    elif ind1 not in circuits and ind2 in circuits:
        circuits[ind1] = circuits[ind2]
    elif ind1 in circuits and ind2 not in circuits:
        circuits[ind2] = circuits[ind1]
    else:  #  ind1 in circuits and ind2 in circuits
        # remap from ind1 to ind2 (join circuits)

        if nr_circuits > 1:
            nr_circuits -= 1

        if circuits[ind1] != circuits[ind2]:
            # print('here', ind1, ind2)
            orig_circuit = circuits[ind1]
            for k, v in circuits.items():
                if v == orig_circuit:
                    circuits[k] = circuits[ind2]
        else:
            # same circuit, nothing happens
            pass

    # print(circuits)

    # print(nr_circuits, len(circuits), len(locations))

    if len(circuits) == len(locations) and nr_circuits == 1:
        # this is last connection
        # print('found:', locations[ind1], locations[ind2])
        solution = locations[ind1][0] * locations[ind2][0]
        break

    
print('solution 2:', solution)


