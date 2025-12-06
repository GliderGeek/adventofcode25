from pathlib import Path
import math
import re


# file_path = Path(__file__).parent / 'example.txt'
file_path = Path(__file__).parent / 'input.txt'

print(f'running with {file_path.parts[-1]}')


# part 1

problems = []

total = 0
values = True
with open(file_path) as f:
    line_nr = 0
    for line in f.read().splitlines():
         
        values = '*' not in line and '+' not in line

        if values:
            for i, numb in enumerate(re.findall(r"(\d+)", line)):
                if line_nr == 0:
                    problems.append([])
                problems[i].append(int(numb))
        else:
            for i, operator in enumerate(re.findall(r"([*+])", line)):
                if operator == '+':
                    subtotal = sum(num for num in problems[i])
                elif operator == '*':
                    subtotal = 1
                    for num in problems[i]:
                        subtotal = subtotal * num
                
                # print('subtotal', subtotal)
                total += subtotal

        line_nr += 1

print('solution 1', total)

# part 2

total = 0
with open(file_path) as f:

    lines = f.read().splitlines()

    cols = []
    subtotals = []
    for i, char in enumerate(lines[-1]):
        if char in ('*', '+'):
            if i != 0:
                cols.append([start_char, start_i, i-2])
            start_i = i
            start_char = char
    cols.append([start_char, start_i, len(lines[-1])-1])

    # print(cols)

    vals = []
    total = 0
    for i, (operator, start, end) in enumerate(cols):

        if operator == '+':
            subtotal = 0
        elif operator == '*':
            subtotal = 1

        for j in range(start, end+1):

            val = ''
            for line in lines[:-1]:
                if line[j] == ' ':
                    continue
                else:
                    val = val + line[j]
            
            num = int(val)

            # print('num', num)

            if operator == '+':
                subtotal += num
            elif operator == '*':
                subtotal = subtotal * num

            # print('subtotal', subtotal)
            
        total += subtotal
        # print('total', total)

print('solution 2', total)
