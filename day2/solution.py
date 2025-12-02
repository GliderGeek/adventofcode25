from pathlib import Path
import math


# file_path = Path(__file__).parent / 'example.txt'
file_path = Path(__file__).parent / 'input.txt'

print(f'running with {file_path.parts[-1]}')


# part 1
sum = 0
with open(file_path) as f:
    for range_str in f.read().split(','):
        start, end = range_str.split('-')
        start = int(start)
        end=int(end)

        for product_id in range(int(start), int(end)+1):
            pid = str(product_id)

            half = int(len(pid)/2)
            if len(pid) % 2 == 0 and pid[0:half] == pid[half::]:
                sum += product_id

print('part 1, solution:', sum)


# part 2
sum = 0
with open(file_path) as f:
    for range_str in f.read().split(','):
        start, end = range_str.split('-')
        start = int(start)
        end=int(end)

        for product_id in range(int(start), int(end)+1):
            pid = str(product_id)

            for i in range(1, len(pid)):
                str_part = pid[0:i]
                if len(pid) % len(str_part) == 0:
                    fits = int(len(pid)/len(str_part))
                    if fits >= 2 and fits * str_part == pid:
                        sum += product_id
                        break

print('part 2, solution:', sum)