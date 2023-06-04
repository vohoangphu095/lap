# Step 3

import random
from lib import word_list
from lib import stages

chosen_word = random.choice(word_list)

print(chosen_word)

display = []
for x in range(len(chosen_word)):
    display += "_"
print(display)
lives = 6

end_game = False
while not end_game:

    guess = input('type your guess word: ').lower()

    for x in range(len(chosen_word)):
        wordx = chosen_word[x]
        if guess == chosen_word[x]:
            display[x] = wordx
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f'you wrong, lives: {lives}', stages[lives])
    if lives == 0:
        print("you loose")
        end_game = True

    if "_" not in display:
        print('you win')
        end_game = True

