def remove_first_occur(string, char):

    string2 = ""
    length = len(string)
    i = 0

    while i < length:
        if string[i] == char:
            string2 = string[0:i] + string[i + 1 : length]
            break
        i = i + 1

    return string2


def check_green_letters(word, green_letters):
    if green_letters:
        for index, letter in enumerate(word):
            if green_letters[index] and not letter == green_letters[index]:
                return False

    return True


def check_yellow_letters(word, yellow_letters):

    word_copy = word

    for index, letter in enumerate(yellow_letters):

        isInWord = letter in word_copy
        isInSamePosition = letter == word_copy[index]
        inWordInSamePosition = isInWord and isInSamePosition

        eliminate_word = not isInWord or inWordInSamePosition

        if eliminate_word:
            return False

    return True


def check_grey_letters(word, grey_letters):

    for letter in grey_letters:
        if letter in word:
            return False

    return True


def possible_words(solution_list, green_letters, yellow_letters, grey_letters):

    possible_words = solution_list.copy()

    for word in solution_list:
        if not check_green_letters(word, green_letters):
            possible_words.remove(word)
            continue

        if not check_yellow_letters(word, yellow_letters):
            possible_words.remove(word)
            continue

        if not check_grey_letters(word, grey_letters):
            possible_words.remove(word)
            continue

    return possible_words


def get_letter_colours(guess, solution):

    green_letters = ["", "", "", "", ""]
    yellow_letters = ["", "", "", "", ""]
    grey_letters = []

    for index, letter in enumerate(guess):
        if letter == solution[index]:
            green_letters[index] = letter
        elif letter in solution:
            yellow_letters[index] = letter
        else:
            grey_letters.append(letter)

    return green_letters, yellow_letters, grey_letters


def num_eliminations(guess, solution, solution_list):

    # get green, yellow and grey letters for each word
    letter_colours = get_letter_colours(guess, solution)

    # plug into possible words function and get length of output
    poss_words = possible_words(
        solution_list, letter_colours[0], letter_colours[1], letter_colours[2]
    )

    # return no. of words each guess would eliminate
    return len(solution_list) - len(poss_words)


if __name__ == "__main__":

    with open("wordle-answers-alphabetical.txt", "r") as file:
        content = file.read()
        solution_list = content.split("\n")

    poss = possible_words(
        solution_list,
        ["", "", "n", "", ""],
        ["", "i", "", "n", "y"],
        ['s','l','a','t','e','r', 'u', 's', 'p', 'k'],
    )

    print(poss)
    print(len(solution_list))
