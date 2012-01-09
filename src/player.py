
class Player(object):

    '''Defines a player in a game of uno'''

    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self, table_card, colour):
        pass

    def colour_decision(self):
        pass

    def has_cards(self):
        return len(self.hand) > 0

    def take_card(self, card):
        self.hand.append(card)
        
    def __str__(self):
        return self.name

class CpuPlayer(Player):

    def __init__(self, name):
        Player.__init__(self, name)

    def play_card(self, table_card, colour):
        wilds         = [c for c in self.hand if c.is_wild()]
        colours       = [c for c in self.hand if c.colour == colour]
        colours_table = [c for c in self.hand if c.colour == table_card.colour]
        values        = [c for c in self.hand if c.value == table_card.value]

        if table_card.is_wild():
            if len(colours) > 0:
                candidate = colours[0]
                self.hand.remove(candidate)
                return candidate
            elif len(wilds) > 0:
                candidate = wilds[0]
                self.hand.remove(candidate)
                return candidate

            return None
        else:
            if len(colours_table) > 0:
                candidate = colours_table[0]
                self.hand.remove(candidate)
                return candidate
            elif len(values) > 0:
                candidate = values[0]
                self.hand.remove(candidate)
                return candidate
            elif len(wilds) > 0:
                candidate = wilds[0]
                self.hand.remove(candidate)
                return candidate

            return None

    def colour_decision(self):
        reds    = [c for c in self.hand if c.colour == 1]
        greens  = [c for c in self.hand if c.colour == 2]
        blues   = [c for c in self.hand if c.colour == 3]
        yellows = [c for c in self.hand if c.colour == 4]

        colour = 1
        max_count = len(reds)

        if len(greens) > max_count:
            max_count = len(greens)
            colour = 2

        if len(blues) > max_count:
            max_count = len(blues)
            colour = 3

        if len(yellows) > max_count:
            max_count = len(yellows)
            colour = 4

        return colour
