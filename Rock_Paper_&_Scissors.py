import random
scissors='''
    __________
---'     _____)_____
             _______)
          ___________)
          (_____)
---.___ (______)

'''
paper='''
    ___________
---'     ______)___
             _______)
          __________)
          (_________)
---.____(______)

'''
rock='''

    ___________
---'     ______)
          (_____)
          (______)
          (_____)
---.____ (_____)


'''
game_images=[rock,paper,scissors]
user_choice= int(input("What do you choose? Type for Rock 0, 1 for paper or 2 for scissors "))

computers_choice=random.randint(0,2)
    

if user_choice>=3 or user_choice<0:
    print("Game over. You didn´t write a correct number")
else:
    print(game_images[user_choice])
    print("Computer chose: ")
    print(game_images[computers_choice])

    if user_choice == computers_choice:
        print("It is a draw")

    elif user_choice==0 and computers_choice==2:
        print("You win!")
    elif computers_choice==0 and user_choice==2:
        print("Computer win!")
    elif computers_choice < user_choice:
        print("You win!")
    elif user_choice<computers_choice:
        print("You lose")