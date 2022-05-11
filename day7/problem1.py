import statistics

with open('input.txt') as file:
    crab_positions = file.readline()

crab_positions = [int(crab.strip()) for crab in crab_positions.split(',')]
final_position = statistics.median(crab_positions)
needed_fuel = [abs(crab-final_position) for crab in crab_positions]
print('Final position : {0}. Needed fuel : {1}'.format(final_position,sum(needed_fuel)))