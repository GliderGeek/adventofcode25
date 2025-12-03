from pathlib import Path
import math


# file_path = Path(__file__).parent / 'example.txt'
file_path = Path(__file__).parent / 'input.txt'

print(f'running with {file_path.parts[-1]}')


# part 1

with open(file_path) as f:
    sum = 0
    for line in f.read().splitlines():
        bank = [int(char) for char in line]
        max_val1 = max(bank[:-1])
        max_ind1 = bank[:-1].index(max_val1)
        max_val2 = max(bank[max_ind1+1::])

        sum += (max_val1*10 + max_val2)

print('solution 1:', sum)

# part 2

with open(file_path) as f:
    sum = 0
    for line in f.read().splitlines():
        bank = [int(char) for char in line]

        max_vals = []  # val, index
        number_batteries = 12

        min_ind = 0
        number_str = ''
        for i in range(1,number_batteries+1):

            if i == number_batteries:
                max_val = max(bank[min_ind::])
                max_ind = bank[min_ind::].index(max_val) + min_ind
            else:
                max_val = max(bank[min_ind:-(number_batteries-i)])
                max_ind = bank[min_ind:-(number_batteries-i)].index(max_val) + min_ind
            
            number_str += str(max_val)
            min_ind = max_ind + 1
        
        sum += int(number_str)

print('solution 2:', sum)
