# a program that will tell a story by taking some inputs such as noun, adjective and verb from the user.

print("..Story Teller..")

# list of noun
person = ["Rashed", "Rakib", "Rahat", "Messi", "Ronaldo", "Shakib", "Mustafiz", "Tendulkar", "Virat", "Rashid"]
sports = ["Cricket", "Football", "Rugby", "Tennis"]
countries = ["Bangladesh", "America"]
places = ["Paris", "Dubai", "Kashmir"]

program_status = False

while not program_status:
	print("Before telling a story we would like to take some words from you.")
	while True:
		noun = input("Enter a noun e.g. Rashed, Cricket, America, Paris, etc. ")
		noun = noun.capitalize()
		adj = input("Enter a adjective e.g. Good, Clumsy, etc. ")
		adj = adj.lower()
		verb = input("Enter a verb e.g. Play, Dance, etc. ")
		verb = verb.lower()

		if len(noun) > 0 and len(adj) > 0 and len(verb) > 0:
			if len(noun) >= 2 and len(adj) >= 2 and len(verb) >= 2:
				if len(noun) >= 3 and len(adj) >= 3:
					# pre-made stories
					story = "Two freinds are going home after finishing the class. One of them says let's learn some grammer. There are too many things to learn in English Grammer. In Grammer parts of speech is eight types. They are noun, pronoun, adjective, verb, adverb, prepositon, conjunction and interjection. Now think about three words whatever comes to your mind. Second freind thinking randomly and says that ok i thought and here are the words " + noun + ", " + adj + ", " + verb + " respectively. Hmm, ok, now First of all, noun is: '" + noun + "'. Secondly, pronoun is: 'They/You'. Thirdly, adjective is: '" + adj + "'. Then, verb is: '"+ verb + "'. Next, adverb is: 'too' that i used earlier in our conversation. Then.. Hey, wait. Let me explain myself the rest. So, then preposition is: 'in/to'. Then, conjunction is: and type sentence we used in our chat. Finally, interjection is: 'Hey' that i said to stop you."
					story1 = noun + " is a " + adj + " reader. He loves to " + verb + ". He " + verb + "s not only on online but also on offline."
					story2 = noun + " is a " + adj + " player. He is one of the finest players in the world. Football lovers " + verb + " him."
					story3 = noun + " is a " + adj + " player. He is one of the finest bowlers in the world. Cricket lovers " + verb + " him."
					story4 = noun + " is a " + adj + " player. He is one of the finest players in the world. Cricket lovers " + verb + " him."
					story5 = noun + " is a " + adj + " game. It's one of the most popular games in the world. Cricket is a bat-and-ball game played between two teams of eleven players on a field at the centre of which is a 20-metre (22-yard) pitch with a wicket at each end, each comprising two bails balanced on three stumps. Last but not least, many people" + verb + noun + "."
					story6 = noun + " is a " + adj + " game. Football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal. It's provabely the most popular game in the world. Last but not least, many people" + verb + noun + "."
					story7 = noun + "refers to the team sports rugby league and rugby union. Legend claims that rugby football was started circa 1845 in Rugby School, Rugby, Warwickshire, England, although forms of football in which the ball was carried and tossed date to medieval times. Rugby eventually split into two sports in 1895 when twenty-one clubs split from the original Rugby Football Union, to form the Northern Union (later to be named rugby league in 1922) in the George Hotel, Huddersfield, Northern England over the issue of payment to players, thus making rugby league the first code to turn professional and pay its players, rugby union turned fully professional in 1995. Both sports are run by their respective world governing bodies World Rugby (rugby union) and the Rugby League International Federation (rugby league). Rugby football was one of many versions of football played at English public schools in the 19th century. Although rugby league initially used rugby union rules, they are now wholly separate sports. In addition to these two codes, both American and Canadian football evolved from rugby football. Last but not least, many people " + verb + noun + "."
					story8 = noun + " is a " + adj + " game. It's one of the most popular games in the world. Last but not least, many people" + verb + noun + "."
					story9 = noun + "is a sovereign state of South Asia. The constitutional name of Bangladesh is the People's Republic of Bangladesh. " + noun + " is a " + adj + "country. People " + verb + " this country."
					story10 = noun + ", the United States is a federal constitutional republic consisting of a single state and a federal district in North America. This country is also known as the United States. " + noun + " is a " + adj + "country. People " + verb + " this country."
					story11 = noun + ", is a " + adj + " place. People " + verb + " to visit here. It's a heaven on earth to some people."

					if noun in person:
						if noun in ["Rashed", "Rakib", "Rahat"]:
							print(story1)
							program_status = True
							break
						elif noun in ["Messi", "Ronaldo"]:
							print(story2)
							program_status = True
							break
						elif noun in ["Shakib", "Mustafiz", "Tendulkar", "Virat", "Rashid"]:
							if noun in ["Mustafiz", "Rashid"]:
								print(story3)
								program_status = True
								break
							else:
								print(story4)
								program_status = True
								break

					elif noun in sports:
						if noun == Cricket:
							print(story5)
							program_status = True
							break
						elif noun == Football:
							print(story6)
							program_status = True
							break
						elif noun == Rugby:
							program_status = True
							print(story7)
							break
						else:
							print(story8)
							program_status = True
							break

					elif noun in countries:
						if noun == Bangladesh:
							print(story9)
							program_status = True
							break
						else:
							print(story10)
							program_status = True
							break

					elif noun in places:
						print(story11)
						program_status = True
						break
					else:
						print(story)
						program_status = True
						break
				else:
					print("Please type valid noun and adjective.")
					continue
			else:
				print("Please type valid noun, adjective and verb.")
				continue
		else:
			print("Empty field(s) not allowed! Please enter noun, adjective and verb.")
			continue
