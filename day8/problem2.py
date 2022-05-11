DIGIT_LOOKUP = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9"
}

def determine_segment_lookup(patterns):

    segment_lookup = {"a":"","b":"","c":"","d":"","e":"","f":"","g":""}  

    # sort by length as we're going to look at the shortest 2 patterns first
    patterns = sorted(patterns,key=len)

    # a can be found by looking for the extra character in the smallest two patterns as they are unique
    # i.e cd = 1, cde = 7, therefore e must refer to segment a as that's the only segment in 7 but not in 1
    for char in patterns[1]:
        if patterns[0].find(char) == -1:
            segment_lookup['a']=char

    # count how many times each segment shows up
    segment_occurance_count = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0}
    for pattern in patterns:
        for char in pattern:
            segment_occurance_count[char]+=1  

    for k, v in segment_occurance_count.items():
        match v:
            case 4:
                segment_lookup['e']=k # e is the only segment that shows up 4 times
            case 6:
                segment_lookup['b']=k # b is the only segment that shows up 6 times
            case 8:
                if k != segment_lookup['a']:
                    segment_lookup['c']=k # c is the only segment that shows up 8 times, but is not a
            case 9:
                segment_lookup['f']=k # f is the only segment that shows up 9 times

    # there are 3 unique segments in the 6 len patterns (e, d & c)
    # we already know e & c, so we can eliminate those, leaving only d
    for i in range(6,9):
        unique = (set("abcdefg")-set(patterns[i])).pop()
        if unique != segment_lookup['e'] and unique != segment_lookup['c']:
            segment_lookup['d']=unique

    # which leaves g as the only remaining segment
    segment_lookup['g']=(set("abcdefg")-set(segment_lookup.values())).pop()
    
    return {v: k for k, v in segment_lookup.items()} # invert the dictionary so we can lookup our original values, rather than decoded

with open('input.txt') as file:
    lines = file.readlines()

total = 0
for line in lines:
    # collect each digit from both halves of each line and sort each one alphabetically
    output_patterns = ["".join(sorted(digit.strip())) for digit in line.split(' | ')[1].split(' ')]
    signal_patterns = ["".join(sorted(digit.strip())) for digit in line.split(' | ')[0].split(' ')]
    lookup = determine_segment_lookup(signal_patterns)

    output=""
    for pattern in output_patterns:
        digit=""
        for segment in pattern:
            digit+=lookup[segment]
        output+=DIGIT_LOOKUP["".join(sorted(digit))]

    total+=int(output)

print('Total for all digits : {0}'.format(total))