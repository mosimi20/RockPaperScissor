import random

while True:

    userSelection = input("Enter your choice (rock, paper, scissors): ")

    print('You have chosen:', userSelection)

    possibleActions = ['rock', 'paper', 'scissors']
    computerPlay = random.choice(possibleActions)

    print('Computer chose:', computerPlay)

    if userSelection == computerPlay:
        print("You both selected:", userSelection, 'Its a tie!')

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