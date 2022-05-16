# The conciseness of this rendition makes it much more readable.

from random import randint

print('Hello! Let\'s play a game!') # character escaping
print('I am thinking of a number between 1 and 100.')

# defining three main variables before loop function
number = randint(1, 100) # random number between 1-100
guess = int(input('Take a guess: ')) # user inputted guess
chances = 0 # starting number of chances taken

while (guess != number): # will loop as long as the guess does not match the answer; infinite chances
   chances += 1 # addition assignment to number of chances taken
   if guess < number:
       print('The answer is higher')
   elif guess > number:
       print('The answer is lower')
   guess = int(input('Try again, enter a new guess: '))

print('You got it!')
print('It took ' + str(chances) + ' guesses.')

input('Enter any key to close the program.') #To prevent the python cmd prompt from closing immediately after last input
