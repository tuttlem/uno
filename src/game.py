
from deck import Deck
from card import Card

class Game(object):
    '''Game object manages players, the table and the deck'''

    def __init__(self):
        self.deck = Deck()
        self.players = list()

    def new_game(self):
        print('Starting a new game\n')

        self.deck.prepare(2)
        self.players = list()
        self.player_index = 0
        self.direction = 1
        self.table_cards = list()
        self.colour_decision = -1

    def start_game(self):
        for i in range(7):
            for p in self.players:
                p.take_card(self.draw_card())

        self.table_cards.insert(0, self.draw_card())
        self.action_handled = True

    def add_player(self, player):
        self.players.append(player);

    def table_card(self):
        return self.table_cards[0]

    def current_player(self):
        return self.players[self.player_index]

    def previous_player(self):
        index = self.player_index + (self.direction * -1)
        
        if index < 0: index = len(self.players) - 1
        if index == len(self.players): index = 0        
        
        return self.players[index]

    def validate(self, candidate):

        if candidate.is_wild():
            return True

        if self.table_card().is_wild():
            return candidate.colour == self.colour_decision
        else:
            return (candidate.colour == self.table_card().colour) or (candidate.value == self.table_card().value)

    def draw_card(self):
        if not self.deck.has_cards():
            print('--- deck needs to be refilled ---')
            top_card = self.table_cards.pop()
            self.deck.refill(self.table_cards)
            table_cards = list()

        return self.deck.next_card()

    def move_to_next_player(self):
        self.player_index += self.direction

        if self.player_index < 0: self.player_index = len(self.players) - 1
        if self.player_index == len(self.players): self.player_index = 0

    def next(self):
        if not self.action_handled:
            if self.table_card().is_reverse():
                self.direction *= -1
                self.move_to_next_player()
                self.move_to_next_player()
                self.action_handled = True

            elif self.table_card().is_skip():
                self.move_to_next_player()
                self.action_handled = True

            elif self.table_card().is_draw_two():
                print('[{0}] {1} is now drawing 2 cards'.format(self.player_index, self.current_player()))
                self.current_player().take_card(self.draw_card())
                self.current_player().take_card(self.draw_card())
                self.move_to_next_player()
                self.action_handled = True

            elif self.table_card().is_wild():
                self.colour_decision = self.previous_player().colour_decision()
                self.action_handled = True
                print('    {1} chose the new colour to be {2}'.format(self.player_index, self.previous_player(), Card.COLOURS[self.colour_decision]))
            
            if self.table_card().is_draw_four():
                print('[{0}] {1} is now drawing 4 cards'.format(self.player_index, self.current_player()))
                self.current_player().take_card(self.draw_card())
                self.current_player().take_card(self.draw_card())
                self.current_player().take_card(self.draw_card())
                self.current_player().take_card(self.draw_card())
                self.move_to_next_player()
                self.action_handled = True

        self.player_move()
        self.move_to_next_player()

    def player_move(self):
        candidate = self.current_player().play_card(self.table_card(), self.colour_decision)

        if candidate == None:
            print('[{0}] {1} can not play a card'.format(self.player_index, self.current_player()))
            self.current_player().take_card(self.draw_card())
        elif not self.validate(candidate):
            print('[{0}] {1} tried to play an invalid card'.format(self.player_index, self.current_player()))
            self.current_player().take_card(candidate)
            self.current_player().take_card(self.draw_card())
        else:
            print('[{0}] {1} played a {2}'.format(self.player_index, self.current_player(), candidate))
            self.action_handled = False
            self.table_cards.insert(0, candidate)

    def winner(self):    
        for player in self.players:
            if not player.has_cards():
                return player

        return None

