import random

def guess_the_number(x):
  print('Lets guess the number')
  
  random_number=random.randint(0,x)
  num_guess=0
  while True:
    guess=int(input(f'Guess a number between 0 and {x}: '))
    num_guess+=1

    if guess== random_number:
      print('u won')
      break
    elif guess<random_number:
      print('Too Low')
    else:
      print('Too large')
    