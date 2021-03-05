from random import randint
def main():

		guesses = 0
		secret = randint(1, 100)
		gameover = False
		lastguess = 0

		print("I'm thinking of a number between 1 and 100 ...\n")
	
		while (not gameover):
		
	
			guesses += 1
		
			response = input("Please guess a number: ")
			lastguess = int(response)

			if (lastguess < secret):
		
				print(str(lastguess) + " is too low.")
		
			elif (lastguess > secret):
		
				print(str(lastguess) + " is too high.")
		
			else:

				print("Congratulations!  You guessed the number in " + str(guesses) + " guess(es)!")
				gameover = True

				input("\nPress the ENTER key to exit.")
				
main()
