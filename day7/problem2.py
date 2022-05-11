import statistics, math

with open('input.txt') as file:
    crab_positions = file.readline()

crab_positions = [int(crab.strip()) for crab in crab_positions.split(',')]
final_position = math.floor(statistics.mean(crab_positions))

def calc_fuel(dist):
    start = 1
    fuel_used = 0
    for i in range(dist):
        fuel_used+=start
        start+=1
    return fuel_used       

needed_fuel = [calc_fuel(abs(crab-final_position)) for crab in crab_positions]
print('Final position : {0}. Needed fuel : {1}'.format(final_position,sum(needed_fuel)))