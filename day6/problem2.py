with open('input.txt') as file:
    original_fish = file.readline()

original_fish = [int(fish.strip()) for fish in original_fish.split(',')]

# list of 8 elements, each element contains the number of fish that far away from duplicating
# i.e. current_fish_population[8] contains the number of fish that are 8 days away from duplicating
current_fish_population = [0 for i in range(9)]

for i in original_fish:
    current_fish_population[i]+=1

num_days = 256
for day in range(num_days):
    num_of_fish_to_duplicate = current_fish_population[0]
    for i in range(1,9):
        current_fish_population[i-1]=current_fish_population[i] # shift all the fish down a day
    
    current_fish_population[6]+=num_of_fish_to_duplicate # add to count as older fish (from day 8) will also be in here
    current_fish_population[8]=num_of_fish_to_duplicate

print('Current fish population after {0} days : {1}'.format(num_days,sum(current_fish_population)))