
values = []
with open('input.txt') as file:
    for cur_line in file:
        values.append(int(cur_line))

prev = None
larger_count = 0
for i in range(2,len(values),1):
    cur_value = values[i]+values[i-1]+values[i-2]
    if prev is not None:
        if cur_value > prev:
            larger_count+=1
    prev = cur_value

print("Number of increasing values in input.txt : {0}".format(larger_count))