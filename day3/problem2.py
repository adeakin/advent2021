from day3 import generate_o2_co2

with open('input.txt') as file:
    lines = file.readlines()

o2, co2 = generate_o2_co2(lines)

print('O2 : {0}. CO2 : {1}'.format(o2,co2))
print('Life support rating : {0}'.format(o2*co2))