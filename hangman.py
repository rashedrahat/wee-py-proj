# a program about guessing the correct word.

import random

i = random.randint(0, 10)
list = [["H*ng*a*", "Hangman"], ["B*n**a", "Banana"], ["*wk*ar*", "Awkward"], ["B*n**", "Banjo"], ["Ba*pi*e*", "Bagpipes"], ["H*p**n", "Hyphen"], ["J*k*b*x", "Jukebox"], ["O*y**n", "Oxygen"], ["Num*sk*l*", "Numbskull"], ["P*j*m*", "Pajama"], ["Rh*t*m*c", "Rhythmic"]]

print("Welcome to HANGMAN game :)")
print("Guess the below word..")
print(list[i][0])
print("You have only one attempt to guess!")
while True:
	left = input("Enter the left hidden letter: ")
	mid = input("Enter the mid hidden letter: ")
	right = input("Enter the right hidden letter: ")

	if len(left) == 0 or len(mid) == 0 or len(right) == 0:
		print("Empty field(s) not allowed! Please type a letter.")
		continue

	elif len(left) > 1 or len(mid) > 1 or len(right) > 1:
		print("More than one letter(s) not allowed! Please type only a letter.")
		continue

	else:
		letters = [left, mid, right]
		pos = 0
		word = list[i][0]
		guess_word = ""
		for l in word:
			if l == "*":
				guess_word = guess_word + letters[pos]
				pos += 1
			else:
				guess_word = guess_word + l
		guess_word = guess_word.capitalize()
		if guess_word == list[i][1]:
			print("Hurrah! You guessed the correct word '", guess_word, "'")
			break
		else:
			print("Sorry! Better luck next time.", "The word is:", list[i][1])
			break
