import random

# Declare variables
words = ['python', 'swift', 'java', 'javascript', 'autocode', 'basic', 'c',
         'prolog', 'speakeasy', 'pascal', 'sql', 'matlab', 'perl', 'rubi', 'r',
         'php', 'kotlin', 'rust', 'nim']
win_number = 0
lost_number = 0


# Declare functions
def position(w, le):
    res = list()
    i = 0
    p = 0
    while p >= 0:
        p = w.find(le, i)
        res.append(p)
        i = p + 1
    res.pop()
    return res


def replace(wfp, w, p):
    wfp = list(wfp)
    for i in p:
        wfp[i] = w[i]
    wfp = ''.join(wfp)
    return wfp


def game():
    global win_number
    global lost_number
    index = random.randint(0, len(words) - 1)
    word = words[index]
    word_for_print = '-' * len(word)
    used_letters = set()
    lives = 8

    while lives > 0:
        print()
        print(word_for_print)
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print('Please, input a single letter.')
        elif not letter.isalpha() or not letter.islower():
            print('Please, enter a lowercase letter from the English alphabet.')
        elif letter in used_letters:
            print("You've already guessed this letter.")
        else:
            used_letters.add(letter)
            if word.count(letter) == 0:
                lives -= 1
                print("That letter doesn't appear in the word.")
            else:
                pos = position(word, letter)
                word_for_print = replace(word_for_print, word, pos)
                if word_for_print.count('-') == 0:
                    win_number += 1
                    print()
                    print(f'You guessed the word {word}!')
                    print('You survived!')
                    break
    if lives == 0:
        lost_number += 1
        print()
        print('You lost!')


# Menu
print('H A N G M A N')
while True:
    menu = input('Type "play" to play the game, '
                 '"results" to show the scoreboard, and '
                 '"exit" to quit: ')
    if menu == 'play':
        game()
    if menu == 'results':
        print(f'You won: {win_number} times')
        print(f'You lost: {lost_number} times')
    if menu == 'exit':
        break
