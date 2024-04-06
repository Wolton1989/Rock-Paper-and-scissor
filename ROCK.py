import random 


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_picture = [rock, paper, scissors] 

user_choices = int(input("what do you chose ? Type 0 for rock 1 for paper 2 for scissors?\n"))
#1print(game_picture[user_choices]) 

if user_choices >= 3 or user_choices == 0:
    print("you typed invalid number ")
else:
    print(game_picture[user_choices] )
    
    computer_choice = random.randint(0, 2)
    print("computer chose ")
    print(game_picture[computer_choice]) 

    if user_choices == 0 and computer_choice == 2:
        print("you win ")
    elif computer_choice == 2 and user_choices == 0:
        print("you lose ")
    elif computer_choice > user_choices:
        print("you lose ")
    elif user_choices > computer_choice:
        print("you win ")
    elif computer_choice == user_choices:
        print(" DRAW ")

