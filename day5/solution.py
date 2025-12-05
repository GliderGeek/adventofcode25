from pathlib import Path
from copy import deepcopy


# file_path = Path(__file__).parent / 'example.txt'
file_path = Path(__file__).parent / 'input.txt'

print(f'running with {file_path.parts[-1]}')


# part 1

fresh_ids = set()

# # bruteforce does not work
# count = 0
# with open(file_path) as f:  
#     fresh_list = True
#     for line in f.read().splitlines():
#         if line == '':
#             fresh_list = False
#             continue

#         if fresh_list:
#             s, e = line.split('-')
#             start=int(s)
#             end=int(e)

#             for i in range(start, end+1):
#                 fresh_ids.add(i)
#         else:
#             if int(line) in fresh_ids:
#                 print(f'{line}: fresh')
#                 count += 1
#             else:
#                 print(f'{line}: spoiled')
        
count = 0
fresh_ranges = []  # tuple start, stop
with open(file_path) as f:  
    fresh_list = True
    for line in f.read().splitlines():
        if line == '':
            fresh_list = False
            continue

        if fresh_list:
            s, e = line.split('-')
            start=int(s)
            end=int(e)
            fresh_ranges.append((start, end))
        else:
            id = int(line)
            for (start, end) in fresh_ranges:
                if start <= id <= end:
                    # print('fresh')
                    count += 1
                    break
            # print('spoiled')

    
print('solution part 1:', count)

# part 2

count = 0
fresh_ranges = []  # tuple start, stop
with open(file_path) as f:  
    for line in f.read().splitlines():
        if line == '':
            break

        s, e = line.split('-')
        start=int(s)
        end=int(e)
        fresh_ranges.append([start, end])

fresh_ranges.sort()

while True:

    previous = None
    new_ranges = []

    # TODO: iteration previous, current
    for (start, end) in fresh_ranges:
        
        if previous is not None:
            p_start, p_end = previous
            if start <= p_end:
                if p_end < end:
                    new_ranges[-1][1] = end
                else:
                    # this one is skipped
                    # fully encompassed
                    pass
            else:
                new_ranges.append([start, end])
        else:
            new_ranges.append([start, end])

        previous = new_ranges[-1]

    if len(new_ranges) == len(fresh_ranges):
        fresh_ranges = new_ranges
        break

    fresh_ranges = deepcopy(new_ranges)
    
count = 0
for (start, end) in fresh_ranges:
    count += (end-start+1)
    
print('solution part 2:', count)