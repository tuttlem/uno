
import time

from game import Game
from player import CpuPlayer

game = Game()

game.new_game()

game.add_player(CpuPlayer('Jack'))
game.add_player(CpuPlayer('John'))
game.add_player(CpuPlayer('Mary'))
game.add_player(CpuPlayer('Anne'))

game.start_game()

while game.winner() == None:
    game.next()
    time.sleep(1)
    


print 'Winner was {0}'.format(game.winner())

