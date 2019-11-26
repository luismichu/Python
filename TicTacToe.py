import random

def getWinner(game):
  getWinner.winner = ' '
  win = [[1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1],
     [1, 0, 0, 1, 0, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 0, 0, 1, 0],
     [0, 0, 1, 0, 0, 1, 0, 0, 1],
     [1, 0, 0, 0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 1, 0, 1, 0, 0]
    ]
  for i in range(len(win)):
    ia = [game[j] * win[i][j] for j in range(len(game))]
    player = [-game[j] * win[i][j] for j in range(len(game))]
    if ia == win[i] or player == win[i]:
      if ia == win[i]:
        getWinner.winner = 'ia'
      else:
        getWinner.winner = 'player'
      return True

  return False


def seeTheFuture(game, turn):
  zeros(game)
  print(zeros.pos)
  for pos in zeros.pos:
    gameCopy = game.copy()
    gameCopy[pos] = turn
    if getWinner(gameCopy):
      if getWinner.winner == 'ia':
        value = 10

      elif getWinner.winner == 'player':
        value = -10

    elif not zeros(game):
      value = 0

    else:
      value = seeTheFuture(gameCopy, turn * -1)

    return [value, pos]



def getBestMove(game, turn, i):
  moves = []
  if zeros(game):
    value = seeTheFuture(game, turn * -1)
    value[0] *= zeros.num
    moves.append([value])
             
    gameCopy = game.copy()
    moves.sort()
    moves.reverse()
    print(moves)
    gameCopy[moves[0][1]] = turn
    return gameCopy
                
  else:
    return game


def zeros(game):
  zeros.num = game.count(0)
  zeros.pos = [i for i in range(len(game)) if game[i] == 0]
  return True if game.count(0) > 0 else False

def printGame(game):
  view = ['X' if ficha==-1 else '-' if ficha==0 else 'O' for ficha in game]
  for i in range(0, 9, 3):
    print(view[i], ' | ', view[i+1], ' | ', view[i+2])
  print('')


game = [1, -1, 1, 0, -1, 1, 0, 0, 0]

game = getBestMove(game, 1, 0)
printGame(game)


game = [0,0,0,0,0,0,0,0,0]

"""while zeros(game) and not getWinner(game):
  jugador = int(input('Pos: '))
  while game[jugador] != 0:
    print('Posicion no valida')
    jugador = int(input('Pos: '))

  game[jugador] = -1

  printGame(game)
  if getWinner(game):
    print(getWinner.winner)
  else:
    game = getBestMove(game, 1, 0)

    printGame(game)
    print(game)
    if getWinner(game):
      print('WINNER:', getWinner.winner)
"""