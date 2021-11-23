import random
import pygame
from pygame import *

#background music of game
pygame.mixer.init()
mixer.music.load(r'C:\Users\vimal\Desktop\sps-music\background.wav')
mixer.music.play(-1)

#music for win and loose
pygame.mixer.init()
loose = pygame.mixer.Sound(r'C:\Users\vimal\Desktop\sps-music\lose.wav')
win = pygame.mixer.Sound(r'C:\Users\vimal\Desktop\sps-music\win.wav')

def stone_paper_scissor():
    while True:
        print()
        print("*************************************************************************")
        print()
        print("- ＳＴ♢ＮΞ ░ ＰΛＰΞＲ ░ ＳＣＩＳＳ♢ＲＳ -\n")
        print()
        print("🧨🎇🎆💰🧨🎇🎆💰🧨🎇🎆💰🧨🎇🎆💰🧨🎇🎆")
        print()
        print("\n💎Stone \n📃Paper \n✂️Scissors")
        print()
        print("*************************************************************************")
        user_action = input("\nYou Choose:- ")
        
        possible_actions = ["Stone", "Paper", "Scissors","stone","paper", "scissors"]
        computer_action = random.choice(possible_actions)#computer randomaly choose one of the given option
        
        print(f"\nYou choose 🦸: {user_action},\nComputer chose 🖥️:{computer_action}.\n")

        #if both user and computer choose same 
        if user_action == computer_action:
            print(f"Both players selected {user_action}.\nIt's a tie!")
            
        elif user_action == "Stone" or user_action == "stone" :
            if computer_action == "Scissors" or computer_action == "scissors":
                print("Rock smashes scissors!\n🏆YOᑌ ᗯIᑎ!")
                win.play()
            else:
                print("Paper covers stone!\n😵ү𝔬𝐔 𝐥Øⓢ𝒆\n!Game Over!")
                loose.play()
                                
        elif user_action == "Paper" or user_action == "paper":
            if computer_action == "Stone" or computer_action == "stone":
                print("Paper covers rock!\n🏆YOᑌ ᗯIᑎ!")
                win.play()
            else:
                print("Scissors cuts paper!\n😵ү𝔬𝐔 𝐥Øⓢ𝒆\n!Game Over!")
                loose.play()
		                
        elif user_action == "Scissors" or user_action == "scissors":
            if computer_action == "Paper":
                print("Scissors cuts paper!\n🏆YOᑌ ᗯIᑎ!")
                win.play()
            else:
                print("Rock smashes scissors!\n😵ү𝔬𝐔 𝐥Øⓢ𝒆\n!Game Over!")
                loose.play()

        print("*************************************************************************\n")
        play_again= input("Play again? (y/n): ")
        print("------------------NEW GAME------------------")
        if play_again.lower() != "y":
            break

#main function
def main():
    print(stone_paper_scissor())
main()
    

