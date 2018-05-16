import random

print('-----------------------------------')
print('      GUESS THE NUMBER APP')
print('-----------------------------------')
print()

the_number = random.randint(0, 100)
guess = -99

while guess != the_number:

    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry but is LOWER than the number.')

    elif guess > the_number:
        print('Sorry but is HIGHER than the number.')

    else:
        print('Congratulations, you guessed correctly!')


