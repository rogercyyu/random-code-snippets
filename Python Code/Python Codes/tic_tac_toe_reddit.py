#!/usr/bin/python
"""Noughts and Crosses."""

import sys

def Input(*args):
  """Kludge to handle python 2 and 3."""
  if sys.version_info.major >= 3:
    return input(*args)
  return raw_input(*args)

bye = r"""
             *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                  MMM88&&&&&&
                    MMM8&&&      *
          |\___/|
          )     (             .
         =\     /=
           )===(            Thanks for playing   *
          /     \
          |     |
         /       \
         \       /
  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  By Me yay  |  |  |  |  |  |  |  |  |
"""


def Play():
  """Play one round of noughts and crosses."""
  position = [' ' for _ in range(9)]

  print ("What is player 1's name?")
  name1 = Input()
  print ("Thanks %s, What's player 2's name?" % name1)
  name2 = Input()
  print ('So %s is X and %s is O.' % (name1, name2))
  Input('Press Enter to continue...')

  PrintBoard(position)

  players = [(name1, 'X'), (name2, 'O')]
  for movecount in range(9):
    player = players[movecount % 2]
    while True:
      print ("%s's ( %s ) turn, please choose placement [1-9]?" % player)
      try:
        move = int(Input())
      except ValueError:
        print ('Invalid input, please choose placement [1-9]?')
        continue
      if move < 1 or move > 9:
        print ('That is not a valid move! Try again.')
        continue
      if position[move-1] != ' ':
        print ('That move is taken!, Try again.')
        continue
      break

    position[move-1] = player[1]
    PrintBoard(position)
    if PlayerWin(position, player):
      print ('%s wins as %s.' % player)
      break
  else:
    print ('Its a tie BOI!')


def PrintBoard(position):
  print ("""
  %s | %s | %s          1 | 2 | 3
  -----------        -----------
  %s | %s | %s          4 | 5 | 6
  -----------        -----------
  %s | %s | %s          7 | 8 | 9
  """ % tuple(p for p in position))


def PlayerWin(position, player):

  def Marks(m1, m2, m3):
    return tuple(position[i-1] for i in (m1, m2, m3))

  mark = player[1]
  win = (mark, mark, mark)
  return (
      Marks(4, 5, 6) == win or
      Marks(7, 8, 9) == win or
      Marks(1, 4, 7) == win or
      Marks(2, 5, 8) == win or
      Marks(3, 6, 9) == win or
      Marks(1, 5, 9) == win or
      Marks(3, 5, 7) == win
  )


# Now let's get down to business.
print ('Welcome to Noughts & Crosses.')

while True:
  Play()
  while True:
    print ('Would you like to play again (y/n)?')
    answer = Input()
    if answer in ('y', 'n'):
      break
  if answer == 'n':
    break
  print ('Aight, resetting...')

print ('Aight, cya.')
print (bye)
