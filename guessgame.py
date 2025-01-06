from random import randint
import random
import string

def check(guessed,guess,word,word_so_far,attempts):
    inFlag = False
    guessed.add(guess) 
    #go through word and check if the guessed letter is in the word
    for i in range(len(word)):
        if guess==word[i].lower(): 
            #if the guessed letter is in the word
            word_so_far[i] = word[i]     
            inFlag = True

    print("".join(word_so_far))

    #if letter is not in the word, print:
    if not inFlag:
        attempts = attempts-1
        print( "Sorry, incorrect letter. attempts left: " + str(attempts))
    else:
        print("Nice guess! Attempts remaining: " + str(attempts))
    return attempts

#initialize variables
alphabet = set(string.printable)
done = False
wordbase = ["apple",
            "coconut",
            "banana",
            "mango",
            "white",
            "yellow",
            "black",
            "CSGO",
            "AK case hardened pattern 661 FN Staktrak",
            "Raytracing is overrated",
            "toilet",
            "ohio",
            "rizz",
            "rizzler",
            "people",
            "LTT",
            "Billet Labs",
            "Gamers Nexus", 
            "Grrtt",
            "Hello, world!",
            "Python is fun",
            "Data science rocks",
            "Artificial intelligence",
            "Machine learning",
            "Coding is life",
            "Keep calm and code on",
            "The quick brown fox Jumps over the lazy dog",
            "Innovate and inspire",
            "Think outside the box",
            "Stay curious",
            "Success is a journey",
            "Learn, build, repeat",
            "Code, test, debug, repeat",
            "Embrace the grind",
            "Knowledge is power",
            "Never stop learning",
            "The sky is the limit",
            "Keep pushing forward"]
guessed = set(" ")
attempts = 10
word_so_far = []
word = random.choice(wordbase) 
print("GUESSING GAME")


#set the blank version of the word
for i in range(len(word)):
    if word[i]!=" ":
        word_so_far.append("_")
    else:
        word_so_far.append(word[i])

#game:
while True: 
    #provide input
    guess = input("Please guess a letter: ")
    #conditions for inputs:
    if len(guess)>1:
        guess = input("Sorry, pick ONE letter: ")
    elif guess not in alphabet:
        guess = input("Character not accepted, pick other character: " + str(alphabet))
    #make input lowercase 
    guess = guess.lower()


    #if the letter has been guessed before:
    if guess in guessed:
        while guess in guessed:
            guess = input("Letter already guessed, please pick another: ")
        attempts = check(guessed,guess,word,word_so_far,attempts)
    #if letter has not been guessed yet:
    else:
        attempts = check(guessed,guess,word,word_so_far,attempts)
        
    
   
    
    if "".join(word_so_far) == word:
        print("\n")
        print("DONE!")
        print("correct word: " + word)
        done = True

    if attempts == 0:  
        print("\n")
        print("FAILED :(")
        print("correct word: " + word)
        done = True

    print("\n")

    if done:
        again = input("Play again? (Y/N): ").upper()
        while again!="Y" and again!="N":
            print(again)
            again = input("Please choose between Y/N: ").upper()
        if again=="Y":
            
            wordbase.remove(word)
            if not wordbase:
                print("Sorry, no words left :(")
                break
            print("\n")
            alphabet = set(string.printable)
            done = False
            guessed = set(" ")
            attempts = 10
            word_so_far = []
            word = random.choice(wordbase) 
            #set the blank version of the word
            for i in range(len(word)):
                if word[i]!=" ":
                    word_so_far.append("_")
                else:
                    word_so_far.append(word[i])
            print("GUESSING GAME")
            pass
        elif again=="N":
            break


