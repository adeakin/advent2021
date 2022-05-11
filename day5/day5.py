# takes an input of 
# ["0,9 -> 5,9", "8,0 -> 0,8"]
# and returns a nested list 
# [
#   [
#       [0,9],[5,9]
#   ],
#   [
#       [8,0],[0,8]
#   ]
# ]
def parse_lines(lines):
    step1 = [line.strip().split(' -> ') for line in lines]
    step2 = [[item.split(',') for item in line] for line in step1]
    step3 = [[[int(k) for k in j] for j in i] for i in step2]
    return step3

# takes a single line as a nested list of points
# [[0,9],[5,9]]
# returns ine direction (N/E/S/w) and size
def line_direction_size(line):

    if line[0] == line[1]:
        return None # no change in position, line is 0 length

    xdiff = line[0][0]-line[1][0]
    ydiff = line[0][1]-line[1][1]
    if xdiff == 0: # no change in x, it's either North or South
        if ydiff > 0:
            return 'N', abs(ydiff)
        if ydiff < 0:
            return 'S', abs(ydiff)

    if ydiff == 0: # no change in y, it's either East or West
        if xdiff > 0:
            return 'W', abs(xdiff)
        if xdiff < 0:
            return 'E', abs(xdiff)

    if xdiff != 0 and ydiff != 0: # diagonal line
        if xdiff > 0 and ydiff > 0:
            return 'NW', abs(xdiff)
        if xdiff > 0 and ydiff < 0:
            return 'SW', abs(xdiff)
        if xdiff < 0 and ydiff > 0:
            return 'NE', abs(xdiff)
        if xdiff < 0 and ydiff < 0:
            return 'SE', abs(xdiff)


    return None, None

# finds the max x,y values in the list returned from parse_lines
def find_extents(lines_list):
    x=0
    y=0
    for i in lines_list:
        for j in i:
            if j[0] > x:
                x = j[0]
            if j[1] > y:
                y = j[1]
    return x,y