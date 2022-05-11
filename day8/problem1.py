with open('input.txt') as file:
    lines = file.readlines()

counter = 0

# Numbers 1,4,7,8 are unique segment lengths
# so we can just look for digits with those lengths
for line in lines:
    line = line.split(' | ')
    for digit in line[1].split(' '):
        if len(digit.strip()) in [2,4,3,7]:
            counter+=1

print('Number of times 1,4,7,8 appear : {0}'.format(counter))