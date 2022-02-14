from wordle_solver import *


def test_check_green_letters():
    assert check_green_letters("chase", ["c", "", "", "s", "e"]) == True
    assert check_green_letters("hello", ["h", "e", "l", "l", "o"]) == True
    assert check_green_letters("chase", ["c", "l", "", "s", "e"]) == False
    assert check_green_letters("earth", ["", "", "", "", ""]) == True
    assert check_green_letters("earth", []) == True
    assert check_green_letters("pairs", ["c", "h", "a", "s", "e"]) == False


def test_check_yellow_letters():
    assert check_yellow_letters("shear", ["", "s", "r", "", ""]) == True
    assert check_yellow_letters("shear", []) == True
    assert check_yellow_letters("about", ["t", "a", "u", "", ""]) == True
    assert check_yellow_letters("steer", ["s", "t", "e", "", ""]) == False


def test_check_grey_letters():
    assert check_grey_letters("hello", ["x", "y", "z"]) == True
    assert check_grey_letters("hello", ["h", "y", "z"]) == False
    assert check_grey_letters("hello", ["x", "l", "z", "w", "h"]) == False


def test_possible_words():

    with open("wordle-answers-alphabetical.txt", "r") as file:
        content = file.read()
        solution_list = content.split("\n")

    assert possible_words(solution_list[0:10], ["a", "b", "a", "", ""], ["e"], []) == [
        "abase",
        "abate",
    ]
    assert possible_words(
        solution_list[0:10], ["a", "b", "a", "", ""], ["", "", "", "e", ""], ["t"]
    ) == ["abase"]
    assert (
        possible_words(solution_list[0:10], ["", "", "", "", ""], [""], [])
        == solution_list[0:10]
    )
    assert (
        possible_words(
            solution_list,
            ["", "i", "n", "", "e"],
            ["", "e", "i", "", ""],
            ["a", "r", "o", "s", "u", "t", "l", "h", "g", "m"],
        )
        == ["wince"]
    )


def test_get_letter_colours():
    assert get_letter_colours("hello", "hello") == (
        ["h", "e", "l", "l", "o"],
        ["", "", "", "", ""],
        [],
    )
    assert get_letter_colours("truth", "teeth") == (
        ["t", "", "", "t", "h"],
        ["", "", "", "", ""],
        ["r", "u"],
    )
    assert get_letter_colours("broth", "chase") == (
        ["", "", "", "", ""],
        ["", "", "", "", "h"],
        ["b", "r", "o", "t"],
    )
    assert get_letter_colours("spike", "green") == (
        ["", "", "", "", ""],
        ["", "", "", "", "e"],
        ["s", "p", "i", "k"],
    )
    assert get_letter_colours("close", "chase") == (
        ["c", "", "", "s", "e"],
        ["", "", "", "", ""],
        ["l", "o"],
    )


def test_num_eliminations():

    with open("wordle-answers-alphabetical.txt", "r") as file:
        content = file.read()
        solution_list = content.split("\n")

    assert num_eliminations("aeros", "wince", solution_list) == 2181
