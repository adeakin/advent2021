from day4.day4 import parse_draw, parse_cards, find_winning_card, order_winning_cards
import pytest

lines=[]

@pytest.fixture(autouse=True)
def setup():
    with open('day4/tests/test_input.txt') as file:
        global lines
        lines = file.readlines()

def test_draw_parse():
    output = parse_draw(lines)
    expected = [69,39,67,58,53,97,46,91,37]
    assert(output==expected)

def test_card_parse():
    output = parse_cards(lines)
    expected = [[[46,91,37],[14,2,34],[58,57,99]],[[38,60,62],[39,58,91],[66,74,94]]]
    assert(output==expected)

def test_find_winning_card():
    draw = parse_draw(lines)
    cards = parse_cards(lines)
    output = find_winning_card(draw, cards)
    expected = (91,1,[[38,60,62],['x','x','x'],[66,74,94]])
    assert(output==expected)

def test_order_winning_card():
    draw = parse_draw(lines)
    cards = parse_cards(lines)
    output = order_winning_cards(draw, cards)
    expected = [1,0]
    assert(output==expected)