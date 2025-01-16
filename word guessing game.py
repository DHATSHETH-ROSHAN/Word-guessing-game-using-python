try:
    import random
    import math
    
    name = input("Enter your name: ")
    while True:
        print(f'good luck!,{name}')
        
        # listing words and choosing any random worrd from the listed words
        words = ['rainbow','computer','science', 'programming','bios','microprocessor','ironman','intel','amd','nvidia','snapdragon','desktop']
        word = random.choice(words)
        print('guess the characters: ')
        guesses = ''
    
        r = len(word)
        print(r)
        
        def chance(lb,ub):                  # calculating the correct number of chances for the given lowerr bound  to upper bound
            range_size = ub - lb + 1
            ch = math.ceil(math.log2(range_size))
            return ch
        
        turns = chance(1, r)
        
        while turns > 0:
            failed = 0
            for char in word:
                if char in guesses:
                    print(char,end=' ')
                else:
                    print("_",end=' ')
                    failed +=1
            print()
            
            if failed ==0:
                print("you win👌")
                print(f'the word is: {word}')
                break
            
            #print()
            guess = input("guess a characterr: ").lower()
            if len(guess) == 1 and guess.isalpha():    
                guesses += guess
            else:
                print("Please enter a single character")
            
            if guess not in word:
                turns -=1
                print("wrong")
                print(f'you have {turns} more guesses')
                
                if turns == 0:
                    print("you loose!🪦")
                    print(f'the word is: {word}')
                    break
                    
        replay = input("Do you want to play again? (yes/no): ").strip().lower()   # getting know that the user wants to play or not
        if replay != "yes":     # if the user enters anything other than yes then the game ends
            print("Thanks for playing! Goodbye!")
            break
            
except Exception as e :
    print(f'Failed to import module.😢 {e}')
    