depth = 0
distance = 0
aim = 0
with open('input.txt') as file:
    for line in file:
        line = line.split(' ')
        command = line[0]
        value = int(line[1])

        match command:
            case 'forward':
                distance+=value
                depth+=(aim*value)
            case 'down':
                aim+=value
            case 'up':
                aim-=value

print('Final depth : {0}. Final distance : {1}. Final aim : {2}'.format(depth,distance,aim))
print('Final depth x Final distance : {}'.format(distance*depth))