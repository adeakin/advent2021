from day5 import parse_lines, find_extents, line_direction_size

with open('input.txt') as file:
    lines = file.readlines()

parsed_lines=parse_lines(lines)

# initialize diagram of size x,y with all 0s
diagram = []
x,y = find_extents(parsed_lines)
for i in range(y+1):
    diagram.append([])
    for j in (range(x+1)):
        diagram[i].append(0)

# for each point along each line
# increase the diagram counter by 1
for line in parsed_lines:
    direction, size = line_direction_size(line)
    if direction is None or size is None:
        continue

    size+=1 # so it's inclusive of start/end points
    starty = line[0][1]
    startx = line[0][0]

    match direction:
        case 'N':
            for i in range(size):
                diagram[starty-i][startx]+=1
        case 'E':
            for i in range(size):
                diagram[starty][startx+i]+=1
        case 'S':
            for i in range(size):
                diagram[starty+i][startx]+=1
        case 'W':
            for i in range(size):
                diagram[starty][startx-i]+=1

overlap = 0
for row in diagram:
    for item in row:
        if item >= 2:
            overlap+=1

print('Number of overlapping points : {0}'.format(overlap))