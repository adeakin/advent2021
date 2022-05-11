depth = 0
distance = 0
with open('input.txt') as file:
    for line in file:
        line = line.split(' ')
        command = line[0]
        value = int(line[1])

        match command:
            case 'forward':
                distance+=value
            case 'down':
                depth+=value
            case 'up':
                depth-=value

print('Final depth : {0}. Final distance : {1}'.format(depth,distance))
print('Final depth x Final distance : {0}'.format(distance*depth))