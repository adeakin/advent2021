import copy

def parse_draw(lines):
    return [int(i) for i in lines[0].split(',')]

def parse_cards(lines):
    cards = []
    
    for num, line in enumerate(lines):
        if num == 0: # ignore the first row, it contains the draw
            continue

        if len(line.strip()) == 0:
            cards.append([]) # create a new card every time there's an empty line
            continue

        line = [int(line.strip()) for line in line.split(' ') if len(line) > 0]
        cards[len(cards)-1].append(line) # append each line into the latest card

    return cards

def sum_unmarked(winning_card):
    unmarked_sum = 0
    for row in winning_card:
        for item in row:
            if item != 'x':
                unmarked_sum+=item
    return unmarked_sum

# counts occurances of value in the provided list
def count_occurance(arr,value):
    occurances = 0
    for test_val in arr:
        if value == test_val:
            occurances+=1
    return occurances

# returns a list of each winning card num in order
def order_winning_cards(draw, orig_cards):
    cards = copy.deepcopy(orig_cards)
    card_dimensions = len(cards[0][0])
    winning_cards = []

    for num in draw: # for each number drawn
        for j in range(len(cards)): # for each card
            for k in range(len(cards[j])): # for each row in each card
                cards[j][k] = ['x' if x == num else x for x in cards[j][k]] # replace any instance of drawn num in the card with an 'x' marker
                if count_occurance(cards[j][k],'x') == card_dimensions: # check if this row is a winner
                    if count_occurance(winning_cards,j) == 0: # prevent the same card from showing up in the winners list again
                        winning_cards.append(j)
                
                for l in range(card_dimensions): # check every column in this card for a winning column
                    column = [m[l] for m in cards[j]]
                    if count_occurance(column,'x') == card_dimensions:
                        if count_occurance(winning_cards,j) == 0:  # prevent the same card from showing up in the winners list again
                            winning_cards.append(j)

    return winning_cards

# returns a tuple containing (the winning draw number, the winning card num, the winning card)
def find_winning_card(draw, orig_cards):
    cards = copy.deepcopy(orig_cards)
    card_dimensions = len(cards[0][0])

    for num in draw: # for each number drawn
        for j in range(len(cards)): # for each card
            for k in range(len(cards[j])): # for each row in each card
                cards[j][k] = ['x' if x == num else x for x in cards[j][k]] # replace any instance of drawn num in the card with an 'x' marker
                if count_occurance(cards[j][k],'x') == card_dimensions: # check if this row is a winner
                    return num, j, cards[j]
                
                for l in range(card_dimensions): # check every column in this card for a winning column
                    column = [m[l] for m in cards[j]]
                    if count_occurance(column,'x') == card_dimensions:
                        return num, j, cards[j]

    return None, None # didn't find a winner