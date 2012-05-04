import random
import sys

low = 1
high = 30
limit = 5

print("Guess a number between {0} and {1}".format(low, high))
print("You have 5 guesses to get the right number")

guessnumb = 0
number = random.randint(1,15)

try:

	while guessnumb <= limit:
		guess = int(raw_input('What\'s your guess? '))
		guessnumb += 1
		
		if guess < number:
			print("Your guess was too low")
	
		if guess > number:
			print("Your guess was too high")
	
		if guess == number:
			break

except KeyboardInterrupt:
	print("\n  =^C detected, terminating...")
	sys.exit()

if guess == number:
	print("Great, you guessed the number in {0} trys".format(guessnumb))
else:
	print("No, I was thinking of th number {0}".format(number))
