import random
from hangman_words import word_list as word_list
from hangman_art import *

game_over, life = False, 7

print(logo)
chosen_word = random.choice(word_list)
# Next step to generate blanks
display = []
for _ in range(len(chosen_word)):
    display.append('_')
print(''.join(display))
# Now asking user to guess and all


def user_guses():
    return input().lower()


#print(chosen_word)

while not game_over:
    guess = user_guses()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You have entered wrong word: {guess}")
        life -=1
        print(stages[life])
        if life == 0:
            game_over = True
            break
    if '_' not in display:
        break

    print(' '.join(display))

if '_' not in display:
    print("You win")
    print(' '.join(display))
if game_over:
    print("Game over !")
    print(chosen_word)
