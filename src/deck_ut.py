
import unittest
import deck

class DeckTests(unittest.TestCase):
    
    def setUp(self):
        self.deck1 = deck.Deck()
        self.deck1.prepare(1)
        
        self.deck2 = deck.Deck()
        self.deck2.prepare(2)
        
        self.deck3 = deck.Deck()
        self.deck3.prepare(3)
        
        self.empty_deck = deck.Deck()
    
    def test_card_count(self):
        card_count = 0
        
        while self.deck1.has_cards():
            self.deck1.next_card()
            card_count += 1
            
        self.assertTrue(card_count == 54)
        
    def test_empty_deck(self):
        self.assertFalse(self.empty_deck.has_cards())
    

if __name__ == '__main__':
    unittest.main()
