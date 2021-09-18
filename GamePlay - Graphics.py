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

import random

while True:

    userSelection = input("Enter your choice (rock, paper, scissors): ")

    if userSelection == "rock":
      print(f"You chose \n{rock}")

    elif userSelection == "paper":
      print(f"You chose \n{paper}")

    else:
      print(f"You chose \n{scissors}")

    # print('You have chosen:', userSelection)

    possibleActions = ['rock', 'paper', 'scissors']
    computerPlay = random.choice(possibleActions)

    if computerPlay == "rock":
      print(f"Computer chose \n{rock}")

    elif computerPlay == "paper":
      print(f"Computer chose \n{paper}")

    else:
      print(f"Computer chose \n{scissors}")

    if userSelection == computerPlay:
        print(f"You both selected {userSelection}. Its a tie!")

    elif userSelection == 'rock' and computerPlay == 'scissors':
        print('Rock beats scissors! You win!')

    elif userSelection == 'rock' and computerPlay == 'papper':
        print('Paper beats rock! Computer Wins')

    elif userSelection == 'paper' and computerPlay == 'rock':
        print('Paper beats rock! You win!')
    
    elif userSelection == 'paper' and computerPlay == 'scissors':
        print('Scissors beats paper! Computer Wins')

    elif userSelection == 'scissors' and computerPlay == 'paper':
        print('Scissors beats paper! You win!')

    else:
        print('Rock beats scissors! Computer Wins!')

    playAgain = input('Wanna play again? (y/n): ')

    if playAgain.lower() != 'y':
        exit()