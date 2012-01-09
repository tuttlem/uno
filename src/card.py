
class Card(object):
    '''Defines a single card'''

    COLOURS = {	
        0: 'Omni', 
        1: 'Red', 
        2: 'Green', 
        3: 'Blue', 
        4: 'Yellow'
    }

    VALUES = { 
        0: 'Naught',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Skip',
        11: 'Reverse',
        12: 'Draw Two',
        13: 'Wild',
        14: 'Wild Draw Four' 
    }

    def __init__(self, value, colour):
        self.value = value
        self.colour = colour

    def is_draw_two(self):
        return self.value == 12

    def is_skip(self):
        return self.value == 10

    def is_reverse(self):
        return self.value == 11

    def is_wild(self):
        return self.value == 13 or self.value == 14

    def is_draw_four(self):
        return self.value == 14

    def __str__(self):
        if self.is_wild():
            return Card.VALUES[self.value]

        return '{0} {1}'.format(Card.COLOURS[self.colour], Card.VALUES[self.value])
