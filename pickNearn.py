# a program that will print the earning value based on user's picking things.

import random

Ark1 = ["room1", "room2"]
Ark2 = ["room1", "room2"]
Ark1_room1 = ["apple", "banana", "mango", "orange", "pineapple", "jackfruit", "coconut", "olive"]
Ark1_room2 = ["mobile", "computer", "pc", "smartwatch", "watch", "clock", "tab", "tv"]
Ark2_room1 = ["richman", "polo", "zara", "louisVuitton", "gucci", "nike", "armani", "D&G"]
Ark2_room2 = ["nike", "adidas", "allStar", "northStar", "vans", "puma", "reebok", "newBalance"]

things_info = {"apple":20, "banana":10, "mango":25, "orange":30, "pineapple":40, "jackfruit":100, "coconut":50, "olive":80, "mobile":130000, "computer":99000, "pc":157000, "smartwatch":20000, "watch":200000, "clock":125000, "tab":40000, "tv":50000,
"richman":12000, "polo":11000, "zara":10000, "louisVuitton":9000, "gucci":8000, "nike":7000, "armani":6000, "D&G":5000, "nike":12000, "adidas":12000, "allStar":11000, "northStar":11000, "vans":10000, "puma":9000, "reebok":8000, "newBalance":10000}

li_ark1_room1 = ["dummy", "dummy", "dummy"]
li_ark1_room2 = ["dummy", "dummy", "dummy"]
li_ark2_room1 = ["dummy", "dummy", "dummy"]
li_ark2_room2 = ["dummy", "dummy", "dummy"]

def showList(flat):
	if flat == 1:
		for i in range(3):
			rand_i = random.randint(0, 7)
			li_ark1_room1[i] = Ark1_room1[rand_i]
		for i in range(3):
			rand_i = random.randint(0, 7)
			li_ark1_room2[i] = Ark1_room2[rand_i]
	else:
		for i in range(3):
			rand_i = random.randint(0, 7)
			li_ark2_room1[i] = Ark2_room1[rand_i]
		for i in range(3):
			rand_i = random.randint(0, 7)
			li_ark2_room2[i] = Ark2_room2[rand_i]

def showEarnVal(thing1, thing2):
	earn_val1 = things_info[thing1]
	earn_val2 = things_info[thing2]
	total_earn_val = earn_val1 + earn_val2

	print("You have picked two things from two room. Here is the earning value of your: $", total_earn_val)
	
	if total_earn_val in range(1, 20000):
		print("Poor earning! May be not your day. Pick things wisely. Better luck next time.")
	elif total_earn_val in range(20000, 50000):
		print("Good! Try to earn more.")
	else:
		print("Awesome! You have earned big bucks. Keep it up. See you again.")
	

print("Welcome to Pick N Earn! It's time to pick and earn :)")
print("There are two flats. 'The Ark-1' and 'The Ark-2'")

program_status = True
sub_program_status = True

while program_status:
	flat = int(input("Enter a choice. For 'The Ark-1' type 1 and for 'The Ark-2' type 2. "))
	
	if flat == 1:
		print("You have entered", Ark1[0], "! Pick only a one thing from the following list:")
		showList(flat)

		while sub_program_status:
			print("Wow! Fruits found! Good for health.", li_ark1_room1)
			thing1 = input("Type the name of thing that you wanna pick (pick wisely): ")
			thing1 = thing1.lower()
			
			if thing1 not in li_ark1_room1:
				print("Only allow one thing from the above list!")
				continue
			else:
				print("You have entered", Ark1[1], "! Pick only a one thing from the following list:")
				
				while True:
					print("Wow! Gadgets found!", li_ark1_room2)
					thing2 = input("Type the name of thing that you wanna pick (pick wisely): ")
					thing2 = thing2.lower()
					
					if thing2 not in li_ark1_room2:
						print("Only allow one thing from the above list!")
						continue
					else:
						showEarnVal(thing1, thing2)
						sub_program_status = False
						program_status = False
						break
	elif flat == 2:
		print("You have entered", Ark2[0], "! Pick only a one thing from the following list:")
		showList(flat)
		
		while sub_program_status:
			print("Wow! T-shirts found!", li_ark2_room1)
			thing1 = input("Type the name of thing that you wanna pick (pick wisely): ")
			
			if thing1 not in li_ark2_room1:
				print("Only allow one thing from the above list!")
				continue
			else:
				print("You have entered", Ark2[1], "! Pick only a one thing from the following list:")
				
				while True:
					print("Wow! shoes found!", li_ark2_room2)
					thing2 = input("Type the name of thing that you wanna pick (pick wisely): ")
					
					if thing2 not in li_ark2_room2:
						print("Only allow one thing from the above list!")
						continue
					else:
						showEarnVal(thing1, thing2)
						sub_program_status = False
						program_status = False
						break
	else:
		print("Please type a valid choice! Type 1 or 2.")
		continue