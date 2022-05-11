with open('input.txt') as file:
    prev = None
    larger_count = 0

    for cur_line in file:
        cur_line = int(cur_line)
        if(prev is not None and (cur_line > prev)):
            larger_count+=1
        prev = cur_line
    
    print("Number of increasing values in input.txt : {0}".format(larger_count))