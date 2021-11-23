#SUBMITTED BY-

#Name:- VIMAL PRAKASH MEENA                        AND         Name:- KUSHAGRA SINGH PARIHAR
#Collage Roll No. :- CSC/20/5                                  Collage Roll No. :- CSC/20/34
#University Roll No. :- 20059570004                            University Roll No. :- 20059570027

#X----------------------------------------------------------------------------------------X

#function to acceptthe choice between three games by the player
def choice():
    print("↫↫↫↫↫↬↬↬↬↬♞↫↫↫↫↫↬↬↬↬↬♞↫↫↫↫↫↬↬↬↬↬♞↫↫↫↫↫↬↬↬↬↬♞↫↫↫↫↫↬↬↬↬↬♞↫↫↫↫↫↬↬↬↬↬")
    print("↫↫    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ")             
    print("↫↫          🎮🎮 GAME 🕹️ BOX 🎮🎮                          ")          
    print("↫↫                                                        ")             
    print("↫↫             𝟙.𝕊𝕋𝕆ℕ𝔼 ℙ𝔸ℙ𝔼ℝ 𝕊ℂ𝕀𝕊𝕊𝕆ℝ                         ")              
    print("↫↫             𝟚.𝔸𝔻𝕍𝔼ℕ𝕋𝕌ℝ𝔼 ℚ𝕌𝔼𝕊𝕋                            ")           
    print("↫↫             𝟛.𝔾𝕌𝔼𝕊𝕊 𝕋ℍ𝔼 𝕎𝕆ℝ𝔻                               ")         
    print("↫↫    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ")
    print("↫↫↫↫↫↬↬↬↬↬♞↫↫↫↫↫↬↬↬↬↬♞↫↫↫↫↫↬↬↬↬↬♞↫↫↫↫↫↬↬↬↬↬♞↫↫↫↫↫↬↬↬↬↬♞↫↫↫↫↫↬↬↬↬↬")  
    print()
    #taking input and giving exception if he/she choose option other than given above  
    while True: 
        try:
            n=int(input("Select your game:- "))
            
            if n==1:
                import StonePaperScissor #if player choose "stone-paper-scissors", importing that module of game
                from StonePaperScissor import stone_paper_scissor
                stone_paper_scissor()
                
            elif n==2:
                import AdventureQuest   #if player choose "adventure-quest", importing that module of game
                from AdventureQuest import intro
                intro()
                
            elif n==3:
                import GuessTheWord    #if player choose "guess-the-word", importing that module of game
                from GuessTheWord import display
                display()
            else:
                print("😑😑😑😑😑😑")
        except ValueError:
            print("You have to choose between (1 , 2, 3)?.\nTry again!\n")

#main function        
def main():
    choice()
    
if __name__=="__main__":
    main()
