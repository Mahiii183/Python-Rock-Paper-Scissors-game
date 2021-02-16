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

choices_str = 'Rock,Paper,Scissors'
choice_lst = choices_str.split(',')
again = 'Y'.lower()

while (again == 'y'):
# Player 1
  player_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 scissors :"))
  player_selection = choice_lst[player_choice]
  if player_choice == 0:
    print(rock)
    print(f'Player 1 chose: {player_selection}')
  elif player_choice == 1:
    print(paper)
    print(f'Player 1 chose: {player_selection}')
  elif player_choice == 2:
    print(scissors)
    print(f'Player 1 chose: {player_selection}')
  else:
    print("Invalid credentials")

  # Computer
  computer_ind = int(random.randint(0, 2))
  computer_selection = choice_lst[computer_ind]
  if computer_ind == 0:
    print(rock)
    print(f'Computer chose: {computer_selection}')
  elif computer_ind == 1:
    print(paper)
    print(f'Computer chose: {computer_selection}')
  elif computer_ind == 2:
    print(scissors)
    print(f'Computer chose: {computer_selection}')

  # Functionality
  if player_choice == computer_ind:
    print("It\'s a Tie!")
  elif player_choice > computer_ind:
    if computer_ind == 0 and player_choice == 2:
      print("You Lose!")
    else:
      print("You Win!")
  elif player_choice < computer_ind:
    if player_choice == 0 and computer_ind == 2:
      print("You Win!")
    else:
      print("You lose!")
  
  # Play again
  again = input("Would you like to play again? Y/N: ").lower()
  
  if again == "N".lower():
    print("Thanks for playing!")
