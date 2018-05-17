import random

print('-----------------------------------')
print('      GUESS THE NUMBER APP')
print('-----------------------------------')
print()

the_number = random.randint(0, 100)
guess = -99
name = input("What is your name? ")

while guess != the_number:

    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry, {}, but {} is LOWER than the number.'.format(name, guess))

    elif guess > the_number:
        print('Sorry, {}, but {} is HIGHER than the number.'.format(name, guess))

    else:
        print('Congratulations, {}, you guessed correctly!'.format(name))

print('Stop')
