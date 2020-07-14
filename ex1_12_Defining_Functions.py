import random


def generate_string(string_length):
    """generates a string 27 chars long from dictionary 26 plus space"""
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    match_string = ""
    for i in range(string_length):
        match_string += alphabet[random.randrange(27)]
    return match_string


def score(goal, test_string):
    """compare generated string to test string."""
    num_same = 0
    for i in range(len(goal)):
        if goal[i] == test_string[i]:
            num_same += 1
    return num_same / len(goal)


def main():
    """repeatedly call generate and score. If 100% correct will complete.
       If letters are incorrect, a new string is generated. Print string and
       score so far every 1000 tries."""
    goal_string = "methinks it is like a weasel"
    new_string = generate_string(28)
    best_score = 0
    count = 0
    new_score = score(goal_string, new_string)
    while new_score < 1:
        if new_score > best_score:
            print(count, new_score, new_string)
            best_score = new_score
        count += 1
        if count in range(1000, 10000000, 1000):
            print(count, best_score)
        new_string = generate_string(28)
        new_score = score(goal_string, new_string)


main()
