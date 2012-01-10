
import time

from card import Card
from game import Game
from player import CpuPlayer

def game_event(what):
   if what == Game.GE_GAME_STARTING:
      print 'The game is about to begin'
   elif what == Game.GE_DEALING_CARDS:
      print 'Cards are being dealt to players'
   elif what == Game.GE_DECK_REFILL:
      print 'Deck has been exhausted, need to refill from table cards'
   else:
      print "Unsure what the game state {0} is".format(what)

def player_added(who):
   print "{0} has been added to the game".format(who)

def cards_taken(who, count):
   print "{0} has taken {1} card(s)".format(who, count)

def colour_decision(who, colour):
   print "{0} chose the new colour to be {1}".format(who, Card.COLOURS[colour])

def cant_play(who):
   print "{0} is unable to play a card".format(who)

def card_played(who, card):
   print "{0} played a {1}".format(who, card)

game = Game()
game.game_event += game_event
game.player_added += player_added
game.cards_taken += cards_taken
game.colour_decision_made += colour_decision
game.cant_play += cant_play
game.card_played += card_played;

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

