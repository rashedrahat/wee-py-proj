# a program that is a game where it's all about guess the correct number.

import random
actual_num = random.randint(1, 1000)
low = 1
high = 1000
attempts = 0

while True:
	print("Welcome to GUESS THE NUMBER :)")
	print("Choice the playing mood..")
	option = input("Enter 1 for playing yourself or 2 for computer mode. 0 to to exit! ")
	option = int(option)

	if option == 0:
		print("Program terminated!")
		break
	elif option == 1:
		while True:
			in_num = input("Enter a number between 1 to 1000 to guess: ")
			in_num = int(in_num)
			attempts += 1

			if in_num == actual_num:
				print("Yahoo! You guess the correct number!")
				break
			elif in_num > actual_num:
				print("Sorry! Please try to guess a smaller number.")
			else:
				print("Sorry! Please try to guess a larger number.")

		print("You tried", attempts, "times to guess the correct number.")
	elif option not in [1, 2]:
		print("Invalid choice mood! Please choice a valid mood.")
		continue
	else:
		while True:
			print("Guess a number between 1 to 1000: ")
			guess_num = (low + high) // 2
			print("My guess number:", guess_num)
			attempts += 1

			if guess_num == actual_num:
				print("Yahoo! You guess the correct number!")
				break
			elif guess_num > actual_num:
				print("Sorry! Please try to guess a smaller number.")
				high = guess_num - 1
			else:
				print("Sorry! Please try to guess a larger number.")
				low = guess_num + 1

		print("You tried", attempts, "times to guess the correct number.")