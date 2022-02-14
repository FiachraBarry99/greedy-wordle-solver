from wordle_solver import *
import csv
import time
import os
import sys
from pathlib import Path


def resource_path(relative_path):
    # get absolute path to resource
    try:

        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


with open(resource_path("wordle-allowed-guesses.txt"), "r") as file:
    content = file.read()
    guess_list = content.split("\n")

with open(resource_path("wordle-answers-alphabetical.txt"), "r") as file:
    content = file.read()
    solution_list = content.split("\n")
    num_answers = len(solution_list)

with open(f'{Path.home()}/analysis.csv', "w+", newline="") as file:

    writer = csv.writer(file)
    writer.writerow(["SOLUTION/GUESS"] + guess_list + ["secs/solution"])

    for solution in solution_list:

        start = time.time()

        print(f"starting {solution} at {start}...")

        guess_eliminations = [solution]

        for guess in guess_list:

            # find no. of words each guess would eliminate and store in guess_eliminations
            guess_eliminations.append(num_eliminations(guess, solution, solution_list))

        writer.writerow(guess_eliminations + [time.time() - start])
