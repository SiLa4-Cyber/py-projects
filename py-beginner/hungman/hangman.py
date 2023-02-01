import random
import string

won = 0
lost = 0
print('H A N G M A N')

while True:
    menu = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:")
    if menu == "play":
        word_list = ['python', 'java', 'swift', 'javascript']
        word = random.choice(word_list)
        attempts = 8
        chars = []
        hide_word = list(len(word) * '-')

        while True and attempts > 0:
            print(''.join(hide_word))
            if "-" not in hide_word:
                break

            letter = input('Input a letter: ')
            if len(letter) != 1:
                print("Please, input a single letter.")
            elif letter not in string.ascii_lowercase:
                print("Please, enter a lowercase letter from the English alphabet.")
            elif letter in chars:
                print("You've already guessed this letter.")
            elif letter not in word:  # if the users guess is not in the word
                print("That letter doesn't appear in the word.")
                attempts -= 1
            elif letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        hide_word[i] = letter
            chars.append(letter)

        if "-" in hide_word:
            lost += 1
            print("You lost!")

        else:
            print(f"You guessed the word {word}!")
            print("You survived!")
            won += 1

    elif menu == 'results':
        print(f"You won: {won} times\nYou lost: {lost} times")

    else:
        if menu == 'exit':
            break
