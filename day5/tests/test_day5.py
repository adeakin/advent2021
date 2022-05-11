from day5.day5 import parse_lines, line_direction_size, find_extents
import pytest

lines=[]

@pytest.fixture(autouse=True)
def setup():
    with open('day5/tests/test_input.txt') as file:
        global lines
        lines = file.readlines()

def test_parse_lines():
    output = parse_lines(lines)
    expected = [[[0, 9], [5, 9]], [[8, 0], [0, 8]], [[9, 4], [3, 4]], [[2, 2], [2, 1]], [[7, 0], [7, 4]], [[6, 4], [2, 0]], [[0, 9], [2, 9]], [[3, 4], [1, 4]], [[0, 0], [8, 8]], [[5, 5], [8, 2]]]
    assert(output==expected)

def test_extents():
    parsed_lines = parse_lines(lines)
    output = find_extents(parsed_lines)
    expected = (9,9)
    assert(output==expected)

def test_size_direction():
    parsed_lines = parse_lines(lines)
    output = line_direction_size(parsed_lines[0])
    expected = ('E',5)
    assert(output==expected)