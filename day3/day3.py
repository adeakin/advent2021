
def generate_o2_co2(lines):
    lines = [line.strip() for line in lines]
    line_length = len(lines[0])

    o2_lines = lines.copy()
    co2_lines = lines.copy()

    bitpos=0
    while len(o2_lines) > 1:
        epsilon, gamma = generate_epsilon_gamma(o2_lines)
        gamma = bin(gamma)[2:].zfill(line_length)
        o2_lines = [line for line in o2_lines if line[bitpos]==gamma[bitpos]] # only keep lines that match the gamma value at this bit position
        bitpos+=1

    bitpos=0
    while len(co2_lines) > 1:
        epsilon, gamma = generate_epsilon_gamma(co2_lines)
        epsilon = bin(epsilon)[2:].zfill(line_length)
        co2_lines = [line for line in co2_lines if line[bitpos]==epsilon[bitpos]]
        bitpos+=1

    return int(o2_lines[0],2), int(co2_lines[0],2)

def generate_epsilon_gamma(lines):

    lines = [line.strip() for line in lines]

    # initialize counter so it's the same length as the bitstring
    bitpos_counter = [0 for i in range(len(lines[0]))]

    # iterate over every char in every line
    # add 1 to counter if its a '1'
    # minus 1 otherwise
    for line in lines:
        for pos, char in enumerate(list(line.strip())):
            match char:
                case '0':
                    bitpos_counter[pos]-=1
                case '1':
                    bitpos_counter[pos]+=1

    gamma = 0b0
    epsilon = 0b0
    for pos, value in enumerate(bitpos_counter):
        
        # dont bitshift on the first iteration
        # to go from 0b0 to 12bits you only need 11 shifts
        if pos > 0:
            gamma <<= 1
            epsilon <<= 1    
        
        # any value >0 means case '1' was more frequent than '0' at that bitposition and vice versa
        # 0 means they were equally frequent
        if value >= 0:
            gamma ^= 1
        if value < 0:
            if abs(value) != len(lines): # fix edge case where there's only 0s, so they are both the most and least common values
                epsilon ^= 1

    return epsilon, gamma