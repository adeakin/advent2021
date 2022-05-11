from day3 import generate_epsilon_gamma

with open('input.txt') as file:
    lines = file.readlines()

epsilon, gamma = generate_epsilon_gamma(lines)

print('Gamma : {0}. Epsilon : {1}'.format(gamma,epsilon))
print('Epsilon * Gamma : {0}'.format(epsilon*gamma))