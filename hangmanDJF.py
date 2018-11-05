import random

#lines 4 & 5 read in the file and assign it to the list of possible words to be chosen
wordBank = open("nbateams.txt", "r")
gameBank = wordBank.readlines()

#lines 8-9 randomly pick a word to guess
choice = input("Would you like to play hangman? Y/N ").upper()

while choice[0] == "Y": #If player inputs "y" or "Y", the game begins
	#Lines 12-22 are for aesthetic purposes; 23 & 24 are just opening credits
	title = """
*************************************************************************************************
*███╗   ██╗██████╗  █████╗          ██╗██╗   ██╗███╗   ███╗██████╗ ███╗   ███╗ █████╗ ███╗   ██╗*
*████╗  ██║██╔══██╗██╔══██╗         ██║██║   ██║████╗ ████║██╔══██╗████╗ ████║██╔══██╗████╗  ██║*
*██╔██╗ ██║██████╔╝███████║         ██║██║   ██║██╔████╔██║██████╔╝██╔████╔██║███████║██╔██╗ ██║*
*██║╚██╗██║██╔══██╗██╔══██║    ██   ██║██║   ██║██║╚██╔╝██║██╔═══╝ ██║╚██╔╝██║██╔══██║██║╚██╗██║*
*██║ ╚████║██████╔╝██║  ██║    ╚█████╔╝╚██████╔╝██║ ╚═╝ ██║██║     ██║ ╚═╝ ██║██║  ██║██║ ╚████║*
*╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝     ╚════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝*
*************************************************************************************************                                                                                             
																						  
	"""
	print(title)
	print("A NBA themed Hangman Game designed by Darius Faison!")
	
	print("\n")
	username = input("Enter your name! ")
	#Lines 29-31 are for a special case easter egg"
	if username == "Jordan" or username == "LeBron":
		username = "GOAT"
		print("You are a legend!")
	print(f"{username}, can you guess the NBA team? Let's find out!")
	counter = 0 #Counter of how many incorrect guesses have been made
	#Lines 25 & 26 generate a random number between 0 and the length of the list + 1 in order to get all values in the list, that number is used as the index of the list 
	index = random.randint(0, len(gameBank)-1)
	word = gameBank[index].upper()
	
	#Lines 31-33 initialize the guessLetters list, which contains all of the letters that the player has guessed
	#" " and "\n" are included in the initialization so that those characters do not appear as underscores
	#guessLetters and word are being compared in line 32
	guessLetters = [" ", "\n"]
	guess = "".join("_ " if x not in guessLetters else x for x in word) #If x is not found in guessLetters, then join "_ " to the string guess; else join x to the string
	print(guess)
	
	while counter < 7 and guess != word: #The conditions for which the game will continue running
		letter = input("Guess a letter! (or type 'quit' to end the game) ").upper()
		if letter == "QUIT":
			break
		guessLetters.append(letter) #Append the currently guessed letter to the guessLetters list
		if letter in word:
			print("Correct!")
		#If the letter is not found in word, then counter will increase and a piece of the Jordan ASCII Symbol will be printed out
		else:
			counter += 1
			if letter not in word and counter == 1:
				symbol = """
       ___|
 O     \_/|
          |
          |
__________|
				"""
				print(symbol)
				print("Nah fam. Try again.")
			elif letter not in word and counter == 2:
				symbol = """
       ___|
 O     \_/|
 |        |
          |
__________|
				"""
				print(symbol)
				print("Nah fam. Try again.")
			elif letter not in word and counter == 3:
				symbol = """
       ___|
 O     \_/|
 |        |
/         |
__________|
				"""
				print(symbol)
				print("Nah fam. Try again.")
			elif letter not in word and counter == 4:
				symbol = """
       ___|
 O     \_/|
 |        |
/ \       |
__________|                                            

				"""
				print(symbol)
				print("Nah fam. Try again.")
			elif letter not in word and counter == 5:
				symbol = """
       ___|
 O     \_/|
/|        |
/ \       |
__________|
				"""
				print(symbol)
				print("Nah fam. Try again.")
			elif letter not in word and counter == 6:
				symbol = """
       ___|
 O/    \_/|
/|        |
/ \       |
__________|
				"""
				print(symbol)
				print("Nah fam. Try again.")
			elif letter not in word and counter == 7:
				symbol = """
   o   ___|
 O/    \_/|
/|        |
/ \       |
__________|
				"""
				print(symbol)
				print("Nah fam. Try again.")
		print("\n" *5)
		guess = "".join("_ " if x not in guessLetters else x for x in word)
		print(guess)
		print(guessLetters)
		print("\n" *2)
	if guess == word:
		winTitle = '''
		
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗██╗██╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║██║██║██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║██║██║██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚═╝╚═╝╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║██╗██╗██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝╚═╝╚═╝
                                                               
'''
		print(winTitle)
	elif letter == "quit".upper():
		quitTitle = '''
		
████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗███████╗    ███████╗ ██████╗ ██████╗     ██████╗ ██╗      █████╗ ██╗   ██╗██╗███╗   ██╗ ██████╗ ██╗██╗██╗
╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██║████╗  ██║██╔════╝ ██║██║██║
   ██║   ███████║███████║██╔██╗ ██║█████╔╝ ███████╗    █████╗  ██║   ██║██████╔╝    ██████╔╝██║     ███████║ ╚████╔╝ ██║██╔██╗ ██║██║  ███╗██║██║██║
   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║    ██╔══╝  ██║   ██║██╔══██╗    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██║██║╚██╗██║██║   ██║╚═╝╚═╝╚═╝
   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗███████║    ██║     ╚██████╔╝██║  ██║    ██║     ███████╗██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝██╗██╗██╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝
                                                                                                                                                    
'''
		print(quitTitle)
	else:
		print("The team was the " + word +"!")
		lossTitle = '''
		
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗██╗██╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝██║██║██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  ██║██║██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  ╚═╝╚═╝╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗██╗██╗██╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝╚═╝╚═╝
                                                                         
'''
		print(lossTitle)
	choice = input("Play again? Y/N ").upper() #Allows the user to decide if they would like to play again, should run indefinitely