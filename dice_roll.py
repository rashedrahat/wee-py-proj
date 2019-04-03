# a program that will print a number between 1 to 6 randomly.

import random

def rollDice():
	num = random.randint(1, 6)
	return num

program_status = True

while program_status:
	print("After rolling the dice..")
	print("The number is:", rollDice())

	while True:
		wish = input("Wanna roll again the dice? Type 'Yes' to roll again or 'No' for exit: ")
		if wish in ["Yes", "yes", "YES"]:
			break
		elif wish in ["Exit", "exit", "EXIT"]:
			program_status = False
			print("Program terminated!")
			break
		else:
			print("Unknown operation! Type a valid request.")
			continue