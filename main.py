from GNT import guess_the_number
from RPS import rock_paper_scissors
from ttt import TicTacToe


while True:
  txt="""MINI GAMES!!!
  - Guess The Number     (1)
  - Rock,Paper,Scissors  (2)
  - Tic Tac Toe          (3)
 
       Select a game (press a number or 'q' to quit):"""

  value=input(txt)
  if value =='1':
    guess_the_number(100)
  if value =='2':
    rock_paper_scissors()
  if value =='3':
    game=TicTacToe()
    game.play()

  if value=='q':
    break