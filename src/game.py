
from deck import Deck
from card import Card
from event import Event

class Game(object):
    '''Game object manages players, the table and the deck'''

    GE_GAME_STARTING = 1
    GE_DEALING_CARDS = 2
    GE_DECK_REFILL = 3

    def __init__(self):
        self.deck = Deck()
        self.players = list()

        self.game_event = Event()
        self.card_played = Event()
        self.cards_taken = Event()
        self.player_added = Event()
        self.colour_decision_made = Event()
        self.cant_play = Event()

    def new_game(self):
        self.game_event(self.GE_GAME_STARTING)

        self.deck.prepare(2)
        self.players = list()
        self.player_index = 0
        self.direction = 1
        self.table_cards = list()
        self.colour_decision = -1

    def start_game(self):
        self.game_event(self.GE_DEALING_CARDS)

        for i in range(7):
            for p in self.players:
                p.take_card(self.draw_card())
                self.cards_taken(p, 1)

        self.table_cards.insert(0, self.draw_card())
        self.action_handled = True

    def add_player(self, player):
        self.players.append(player)

        self.player_added(player)

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
            self.game_event(self.GE_DECK_REFILL)

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
                self.current_player().take_card(self.draw_card())
                self.current_player().take_card(self.draw_card())

                self.cards_taken(self.current_player(), 2)

                self.move_to_next_player()
                self.action_handled = True

            elif self.table_card().is_wild():
                self.colour_decision = self.previous_player().colour_decision()
                self.action_handled = True

                self.colour_decision_made(self.previous_player(), self.colour_decision)

            if self.table_card().is_draw_four():
                self.current_player().take_card(self.draw_card())
                self.current_player().take_card(self.draw_card())
                self.current_player().take_card(self.draw_card())
                self.current_player().take_card(self.draw_card())

                self.cards_taken(self.current_player(), 4)

                self.move_to_next_player()
                self.action_handled = True

        self.player_move()
        self.move_to_next_player()

    def player_move(self):
        candidate = self.current_player().play_card(self.table_card(), self.colour_decision)

        if candidate == None:
            self.cant_play(self.current_player())
            self.current_player().take_card(self.draw_card())
            self.cards_taken(self.current_player(), 1)
        elif not self.validate(candidate):
            self.current_player().take_card(candidate)
            self.cant_play(self.current_player())
            self.current_player().take_card(self.draw_card())
            self.cards_taken(self.current_player(), 1)
        else:
            self.action_handled = False
            self.table_cards.insert(0, candidate)
            self.card_played(self.current_player(), candidate)

    def winner(self):
        for player in self.players:
            if not player.has_cards():
                return player

        return None

