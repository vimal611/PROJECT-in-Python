import random
import time
import GDM #importing module which have music 
from GDM import music


#Define a function welcome and taking name and showing basic info 
def welcome():
    name = input(">>Please Player- Enter your preferred game name: ").capitalize() #taking name of player
    if name.isalpha() == True:
        print()
        #giving intro and delay each line to print by 2 sec
        print("->> Hi!", name,"Glad to have you here!")
        time.sleep(2)
        print("->>You will be playing against the computer 🖥️")
        time.sleep(2)
        print("->>The computer will randomly choose a word and you will try to guess what the word is.")
        time.sleep(2)
        print("->>You can always invite your friends🧑‍🤝‍🧑 for a fun time together \nGood Luck👍!\nHave fun playing")
        time.sleep(2)
    else:
        print("Please enter your name using letter only")
        name = input("Enter a game name here: ")
        print("'Hi!'",name,"Lets begins!")

#Define another function get word for generating random words for the user to guess.
def get_word():
    #computer select random word from the list given below
    words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot','lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'litchi', 'muskmelon']
    return random.choice (words).lower()

def game_run():
    welcome()
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    word = get_word()
    letters_guessed= []
    tries = 12
    guessed= False
    print()
    #giving user a hint that word cintain how many letters it have
    print("HINT:- The word contains ",len (word)," letters.")
    print(len(word) *"  _ ")

    while guessed == False and tries>0:
        print("You have "+str(tries)+" tries")
        guess=input("Guess a letter in the word or enter the full word.").lower()
        #user input a letter
        if len(guess)==1:
            if guess not in alphabet: #checking if the enterd chracter is to be alphabet
                print("You are yet to enter  a letter. Check your entry ,make sure you enter an alphabet not a number")
            elif guess in letters_guessed:#check that if player entered a character which he already guessed or not
                print("You have already guessed that letter before.\nTry again🤨!")
            elif guess not in word: #if he entered a chracter which is not a part of the word
                print("Sorry😑 that letter is not part of the word :(")
                letters_guessed.append(guess)
                tries-=1
            elif guess in word:#if entered chracter is in word
                print("Great! That letter exist in the word!")
                letters_guessed.append(guess)
            else:
                print("Check your entry ! You night have entered the wrong entry🚫")

        elif len(guess)==len(word):
            if guess==word:#if he/she guessed right word
                print("Great Job! You guessed the word correctly!")
                guessed = True
            else:#if he/she fails to do so
                print("Sorry😑 that was not the word we were looking for :(")
                tries-=1

        else:
            print("The length of your guess is not the same as the of the correct word.")
            tries-=1
         #here we are updating the status of blank " _ ",when guessed the correct character of word
         #we remove one " _ " and replace it with correct character
        status=""
        if guessed==False:
            for letter in word:
                if letter in letters_guessed:
                    status+=letter
                else:
                    status+="_"
            print(status)

        if status==word:
            #when you are out of all available chances
            print("Great Job😄!\nYou guessed the word correctly!")
            guessed=True
        elif tries==0:
            print("Opps 😵!\nYou are ran out of guesses and you couldn'gt guesses the word.")
def display():
    music()#calling music function from GDM module
    print()
    print("----------------------------------------------------------------------------")
    print()
    print("💥🐼 🐍♡ 【G】【U】【E】【S】【S】 【T】【H】【E】 【W】【O】【R】【D】 😳😳 ♪🎯")
    print()
    print()
    print("     🍇🍊🍓🍑🍏🍋🥭🥥🍈🍉🍒🍐🍍🍌🥝")
    print("     🍉                          🍉")
    print("     🍉  🍒ʄʀʊɨȶ 🍏 ʋҽɾʂι🌺ɳ🍒   🍉")
    print("     🍉                          🍉")
    print("     🍇🍊🍓🍑🍏🍋🥭🥥🍈🍉🍒🍐🍍🍌🥝")
    print()
    print()
    #asking for paly or not
    print("TO play? (yes/no)")
    response = input ("Enter 'y' for Yes or 'N' for No :- ").lower()
    if response == 'y':
        game_run()
    else:
        print("Hope you had fun playing the game.\nSee you next time!\n   😕😕😕") 
        
#main function        
def main():
    display()
    
if __name__=="__main__":
    main()
            
