import random
from string import ascii_lowercase

def ask_repeat():
    wh = input('Type "play" to play the game, "exit" to quit: ')
    if wh == "quit":
        quit()
    elif wh == 'play':
        play()
    else:
        ask()

def ask():
    wh = input('Type "play" to play the game, "exit" to quit: ')
    if wh == "quit":
        quit()
    elif wh == 'play':
        play()

def play():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    correct_answer = random.choice(word_list)
    result = list('-' * len(correct_answer))
    recent_inputs = []
    correct_answer_letter = list(correct_answer)

    tries = 8
    while tries > 0:
        print(''.join(result))
        letter = input("Input a letter: ")

        if len(letter) != 1:
            print("You should input a single letter")
            print()
            continue
        if letter not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")
            print()
            continue
        if letter in result or letter in recent_inputs:
            print("You already typed this letter")
            print()
            continue
        if letter not in correct_answer_letter:
            print("No such letter in the word")
            tries -= 1
        recent_inputs.append(letter)

        for i, value in enumerate(correct_answer_letter):

            if value == letter and value not in result:
                result[i] = letter

        if result == correct_answer_letter:
            print("You guessed the word!")
            print("You survived!")
            break
        if tries == 0:
            if result != correct_answer_letter:
                print("You are hanged!")
            else:
                print("You survived!")
        print()

print("H A N G M A N")
print()
ask_repeat()
ask()

