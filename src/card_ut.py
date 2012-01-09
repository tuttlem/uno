
import unittest
import card

class CardTests(unittest.TestCase):

    def value_by_name(self, name):
        return [v[0] for v in card.Card.VALUES.items() if v[1] == name][0]

    def setUp(self):
        self.skip_card = card.Card(self.value_by_name('Skip'), 1)
        self.reverse_card = card.Card(self.value_by_name('Reverse'), 1)
        self.draw_two_card = card.Card(self.value_by_name('Draw Two'), 1)
        self.wild_card = card.Card(self.value_by_name('Wild'), 0)
        self.draw_four_card = card.Card(self.value_by_name('Wild Draw Four'), 0)

    def test_is_skip(self):
        self.assertTrue(self.skip_card.is_skip())
        self.assertFalse(self.skip_card.is_draw_two())
        self.assertFalse(self.skip_card.is_reverse())
        self.assertFalse(self.skip_card.is_wild())
        self.assertFalse(self.skip_card.is_draw_four())

    def test_is_draw_two(self):
        self.assertTrue(self.draw_two_card.is_draw_two())
        self.assertFalse(self.draw_two_card.is_skip())
        self.assertFalse(self.draw_two_card.is_reverse())
        self.assertFalse(self.draw_two_card.is_wild())
        self.assertFalse(self.draw_two_card.is_draw_four())

    def test_is_reverse(self):
        self.assertTrue(self.reverse_card.is_reverse())
        self.assertFalse(self.reverse_card.is_draw_two())
        self.assertFalse(self.reverse_card.is_skip())
        self.assertFalse(self.reverse_card.is_wild())
        self.assertFalse(self.reverse_card.is_draw_four())

    def test_is_wild(self):
        self.assertTrue(self.wild_card.is_wild())
        self.assertFalse(self.wild_card.is_draw_two())
        self.assertFalse(self.wild_card.is_skip())
        self.assertFalse(self.wild_card.is_reverse())
        self.assertFalse(self.wild_card.is_draw_four())

        self.assertTrue(self.draw_four_card.is_wild())
        self.assertFalse(self.draw_four_card.is_draw_two())
        self.assertFalse(self.draw_four_card.is_skip())
        self.assertFalse(self.draw_four_card.is_reverse())

    def test_is_draw_four(self):
        self.assertTrue(self.draw_four_card.is_draw_four())
        self.assertFalse(self.draw_four_card.is_draw_two())
        self.assertFalse(self.draw_four_card.is_skip())
        self.assertFalse(self.draw_four_card.is_reverse())


if __name__ == '__main__':
    unittest.main()
