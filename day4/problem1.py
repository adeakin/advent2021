from day4 import parse_cards, parse_draw, find_winning_card, sum_unmarked

with open('input.txt') as file:
    lines = file.readlines()

draw = parse_draw(lines)
cards = parse_cards(lines)

winning_num, winning_card_num, winning_card = find_winning_card(draw,cards)
unmarked_sum = sum_unmarked(winning_card)

print('Winning Num : {0}. Winning Card Num : {1}. Unmarked Sum : {2}'.format(winning_num, winning_card_num, unmarked_sum))
print('Final Score : {0}'.format(winning_num*unmarked_sum))