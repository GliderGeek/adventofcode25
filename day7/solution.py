from pathlib import Path
import math
import re


# file_path = Path(__file__).parent / 'example.txt'
file_path = Path(__file__).parent / 'input.txt'

print(f'running with {file_path.parts[-1]}')


# part 1

splits = 0
with open(file_path) as f:
    lines = f.read().splitlines()
    beams = set({lines[0].index('S')})

    for line in lines:
        splitters = set(m.start() for m in re.finditer(r'(\^)', line))

        hit_splitter = beams & splitters
        for beam in hit_splitter:
            splits += 1
            beams.remove(beam)
            beams.add(beam-1)
            beams.add(beam+1)

        # print(beams)

print('solution 1:', splits)


# part 2

with open(file_path) as f:
    lines = f.read().splitlines()
    beams = {lines[0].index('S'): 1}

    for line in lines:
        splitters = set(m.start() for m in re.finditer(r'(\^)', line))

        hit_splitter = beams.keys() & splitters
        for beam in hit_splitter:

            options = beams[beam]

            del beams[beam]

            if (beam-1) not in beams:
                beams[beam-1]=0
            beams[beam-1] += options

            if (beam+1) not in beams:
                beams[beam+1]=0
            beams[beam+1] += options

        # print(beams)

worls = sum(val for val in beams.values())

print('solution 2:', worls)
