from pathlib import Path
import math


# file_path = Path(__file__).parent / 'example.txt'
file_path = Path(__file__).parent / 'input.txt'

print(f'running with {file_path.parts[-1]}')

# part 1

dial_position = 50
encountered_0 = 0
with open(file_path) as f:
    for line in f.readlines():
        turns_right = line[0] == 'R'
        number_of_turns = int(line[1::])

        if turns_right:
            dial_position += number_of_turns
        else:
            dial_position -= number_of_turns
        
        dial_position = (dial_position + 100) % 100

        if dial_position == 0:
            encountered_0 += 1

print('Solution part 1:', encountered_0)

# part 2

dial_position = 50
encountered_0 = 0
passed_0 = 0
new_dial_position = 0
with open(file_path) as f:
    for line in f.readlines():
        turns_right = line[0] == 'R'
        number_of_turns = int(line[1::])

        if turns_right:
            new_dial_position = dial_position + number_of_turns
        else:
            new_dial_position = dial_position - number_of_turns

        if new_dial_position == 0:
            # this case is not dealt with in below func, but should be counted
            encountered_0 += 1
        else:
            # this includes landing on a resulting 0's like -200, -100, 100, 200, but not 0 itself
            passed_0 += math.floor(abs(new_dial_position) / 100)  # abs necessary because of negative numbers not working as intended with floor
            
            # also count when traversing over 0 in the negative direction
            if new_dial_position < 0 and dial_position > 0:
                passed_0 += 1

            new_dial_position = (new_dial_position + 100) % 100

        dial_position = new_dial_position
        

print('Solution:', encountered_0 + passed_0)
