import random

#lines 4 & 5 read in the file and assign it to the list of possible words to be chosen
wordBank = open("nbateams.txt", "r")
gameBank = wordBank.readlines()

#lines 8-9 randomly pick a word to guess
choice = input("Would you like to play hangman? Y/N ").upper()

while choice == "Y": #If player inputs "y" or "Y", the game begins
	#Lines 12-21 are for aesthetic purposes
	title = """
	 *  ███╗   ██╗██████╗  █████╗     ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗    *
	*   ████╗  ██║██╔══██╗██╔══██╗    ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║     *
	 *  ██╔██╗ ██║██████╔╝███████║    ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║    *
	  * ██║╚██╗██║██╔══██╗██╔══██║    ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║   *
	 *  ██║ ╚████║██████╔╝██║  ██║    ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║    *
	*   ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝     *
																								  
	"""
	print(title)
	
	counter = 0 #Counter of how many incorrect guesses have been made
	#Lines 25 & 26 generate a random number between 0 and the length of the list + 1 in order to get all values in the list, that number is used as the index of the list 
	index = random.randint(0, len(gameBank)+1)
	word = gameBank[index]
	
	#Lines 31-33 initialize the guessLetters list, which contains all of the letters that the player has guessed
	#" " and "\n" are included in the initialization so that those characters do not appear as underscores
	#guessLetters and word are being compared in line 32
	guessLetters = [" ", "\n"]
	guess = "".join("_ " if x not in guessLetters else x for x in word) #If x is not found in guessLetters, then join "_ " to the string guess; else join x to the string
	print(guess)
	
	while counter < 7 and guess != word: #The conditions for which the game will continue running
		letter = input("Guess a letter! ")
		guessLetters.append(letter) #Append the currently guessed letter to the guessLetters list
		if letter in word:
			print("Correct!")
		#If the letter is not found in word, then counter will increase and a piece of the Jordan ASCII Symbol will be printed out
		else:
			counter += 1
			if letter not in word and counter == 1:
				print("Nah fam. Try again.")
				symbol = """

                       
            ,----..    
           /   /   \   
          /   .     :  
         .   /   ;.  \ 
        .   ;   /  ` ; 
        ;   |  ; \ ; | 
        |   :  | ; | ' 
        .   |  ' ' ' : 
        '   ;  \; /  | 
         \   \  ',  /  
          ;   :    /   
           \   \ .'    
            `---`      
                       
                       

				"""
				print(symbol)
			elif letter not in word and counter == 2:
				print("Nah fam. Try again.")
				symbol = """

                       
            ,----..    
           /   /   \   
          /   .     :  
         .   /   ;.  \ 
        .   ;   /  ` ; 
        ;   |  ; \ ; | 
        |   :  | ; | ' 
        .   |  ' ' ' : 
        '   ;  \; /  | 
         \   \  ',  /  
          ;   :    /   
           \   \ .'    
            `---`      
                       
                       
                       
          ,---,        
        ,---.'|        
        |   | :        
        '   : '        
        :   | |        
        |   ' :        
        ;   ; |        
        '   | '        
        |   | :        
        '   : '        
        |   | |        
        ;   : ;        
        |   ,/         
        '---'          
                       
  
				"""
				print(symbol)
			elif letter not in word and counter == 3:
				print("Nah fam. Try again.")
				symbol = """

                       
            ,----..    
           /   /   \   
          /   .     :  
         .   /   ;.  \ 
        .   ;   /  ` ; 
        ;   |  ; \ ; | 
        |   :  | ; | ' 
        .   |  ' ' ' : 
        '   ;  \; /  | 
         \   \  ',  /  
          ;   :    /   
           \   \ .'    
            `---`      
                       
                       
                       
                ,---,  
          ,--,,---.'|  
         / .`||   | :  
        /' / ;'   : '  
       /  / .':   | |  
      /  / ./ |   ' :  
     / ./  /  ;   ; |  
    /  /  /   '   | '  
   /  /  /    |   | :  
  ;  /  /     '   : '  
./__;  /      |   | |  
|   : /       ;   : ;  
;   |/        |   ,/   
`---'         '---'    
                       

				"""
				print(symbol)
			elif letter not in word and counter == 4:
				print("Nah fam. Try again.")
				symbol = """

                                             
            ,----..                          
           /   /   \                    ,--, 
          /   .     :                  / .`| 
         .   /   ;.  \                /' / ; 
        .   ;   /  ` ;               /  / .' 
        ;   |  ; \ ; |              /  / ./  
        |   :  | ; | '             / ./  /   
        .   |  ' ' ' :            /  /  /    
        '   ;  \; /  |           /  /  /     
         \   \  ',  /           ;  /  /      
          ;   :    /          ./__;  /       
           \   \ .'           |   : /        
            `---`             ;   |/         
                              `---'          
                                             
                                             
                ,---,                        
          ,--,,---.'|                        
         / .`||   | :                        
        /' / ;'   : '                        
       /  / .':   | |                        
      /  / ./ |   ' :                        
     / ./  /  ;   ; |                        
    /  /  /   '   | '                        
   /  /  /    |   | :                        
  ;  /  /     '   : '                        
./__;  /      |   | |                        
|   : /       ;   : ;                        
;   |/        |   ,/                         
`---'         '---'                          
                                             

				"""
				print(symbol)
			elif letter not in word and counter == 5:
				print("Nah fam. Try again.")
				symbol = """

                                             
            ,----..                          
           /   /   \                    ,--, 
          /   .     :                  / .`| 
         .   /   ;.  \                /' / ; 
        .   ;   /  ` ;               /  / .' 
        ;   |  ; \ ; |              /  / ./  
        |   :  | ; | '             / ./  /   
        .   |  ' ' ' :            /  /  /    
        '   ;  \; /  |           /  /  /     
         \   \  ',  /           ;  /  /      
          ;   :    /          ./__;  /       
           \   \ .'           |   : /        
            `---`             ;   |/         
                              `---'          
                                             
                                             
                ,---,                        
          ,--,,---.'|                        
         / .`||   | :                        
        /' / ;'   : '                        
       /  / .':   | |                        
      /  / ./ |   ' :                        
     / ./  /  ;   ; |                        
    /  /  /   '   | '                        
   /  /  /    |   | :                        
  ;  /  /     '   : '                        
./__;  /      |   | |                        
|   : /       ;   : ;                        
;   |/        |   ,/                         
`---'         '---'                          
                                             
                                             
                                             
          ,--,                               
         / .`|                               
        /' / ;                               
       /  / .'                               
      /  / ./                                
     / ./  /                                 
    /  /  /                                  
   /  /  /                                   
  ;  /  /                                    
./__;  /                                     
|   : /                                      
;   |/                                       
`---'                                        
                                             

				"""
				print(symbol)
			elif letter not in word and counter == 6:
				print("Nah fam. Try again.")
				symbol = """

                                             
            ,----..                          
           /   /   \                    ,--, 
          /   .     :                  / .`| 
         .   /   ;.  \                /' / ; 
        .   ;   /  ` ;               /  / .' 
        ;   |  ; \ ; |              /  / ./  
        |   :  | ; | '             / ./  /   
        .   |  ' ' ' :            /  /  /    
        '   ;  \; /  |           /  /  /     
         \   \  ',  /           ;  /  /      
          ;   :    /          ./__;  /       
           \   \ .'           |   : /        
            `---`             ;   |/         
                              `---'          
                                             
                                             
                ,---,                        
          ,--,,---.'|                        
         / .`||   | :                        
        /' / ;'   : '                        
       /  / .':   | |                        
      /  / ./ |   ' :                        
     / ./  /  ;   ; |                        
    /  /  /   '   | '                        
   /  /  /    |   | :                        
  ;  /  /     '   : '                        
./__;  /      |   | |                        
|   : /       ;   : ;                        
;   |/        |   ,/                         
`---'         '---'                          
                                             
                                             
                                             
          ,--,        ,--,                   
         / .`|        |'. \                  
        /' / ;        ; \ `\                 
       /  / .'        `. \  \                
      /  / ./          \  \  \               
     / ./  /            \  \ '\              
    /  /  /              \  ;  ;             
   /  /  /                \  \  \            
  ;  /  /                  \  ;  \           
./__;  /                    \  \__;,         
|   : /                      \ |   :         
;   |/                        \;   |         
`---'                          `---'         
                                             

				"""
				print(symbol)
			elif letter not in word and counter == 7:
				print("Nah fam. Try again.")
				symbol = """

                                               
                                               
                                    ,----..    
                                   /   /   \   
                                  /   .     :  
                                 .   /   ;.  \ 
                                .   ;   /  ` ; 
                                ;   |  ; \ ; | 
                                |   :  | ; | ' 
                                .   |  ' ' ' : 
                                '   ;  \; /  | 
                                 \   \  ',  /  
                                  ;   :    /   
                                   \   \ .'    
                                    `---`                                                  
            ,----..                            
           /   /   \          ,--,             
          /   .     :        / .`|             
         .   /   ;.  \      /' / ;             
        .   ;   /  ` ;     /  / .'             
        ;   |  ; \ ; |    /  / ./              
        |   :  | ; | '   / ./  /               
        .   |  ' ' ' :  /  /  /                
        '   ;  \; /  | /  /  /                 
         \   \  ',  / ;  /  /                  
          ;   :    /./__;  /                   
           \   \ .' |   : /                    
            `---`   ;   |/                     
                    `---'                      
                                               
                                               
                ,---,                          
          ,--,,---.'|                          
         / .`||   | :                          
        /' / ;'   : '                          
       /  / .':   | |                          
      /  / ./ |   ' :                          
     / ./  /  ;   ; |                          
    /  /  /   '   | '                          
   /  /  /    |   | :                          
  ;  /  /     '   : '                          
./__;  /      |   | |                          
|   : /       ;   : ;                          
;   |/        |   ,/                           
`---'         '---'                            
                                               
                                               
                                               
          ,--,        ,--,                     
         / .`|        |'. \                    
        /' / ;        ; \ `\                   
       /  / .'        `. \  \                  
      /  / ./          \  \  \                 
     / ./  /            \  \ '\                
    /  /  /              \  ;  ;               
   /  /  /                \  \  \              
  ;  /  /                  \  ;  \             
./__;  /                    \  \__;,           
|   : /                      \ |   :           
;   |/                        \;   |           
`---'                          `---'           
                                               

				"""
				print(symbol)
		guess = "".join("_ " if x not in guessLetters else x for x in word)
		print(guess)
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
	else:
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