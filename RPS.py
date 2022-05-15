import random

def rock_paper_scissors():
  print("Let's play Rock Paper and Scissors")

  r ="rock"
  p="paper"
  s="scissors"

  all_choices=[r,p,s]

  user=input(f'Enter a choice ({r},{p} and {s}): ')

  if user not in all_choices:
    print("Invalid choice")
    return

  computer=random.choices(all_choices)
  print(f'User Choice {user},computer chose {computer}')

  if user == computer:
    print('DRAW')
  elif (user==r and computer==p) or (user==p and computer==s) or (user==s and  computer==r):
    print('Computer Wins')
  else:
    print('You won')
        