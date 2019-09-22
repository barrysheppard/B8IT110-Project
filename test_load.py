
#####################################################################
# Title: Keyforge Project                                           #
# Student: Barry Sheppard ID: 10387786                              #
# Task: Load keyforge decks from https://www.keyforgegame.com       #
#####################################################################


#####################################################################
# Import                                                            #
#####################################################################
import unittest
from load import load_deck
from load import total_decks

#####################################################################
# Code                                                              #
#####################################################################


# test the load functionality
class TestLoad(unittest.TestCase):

    def test_load_deck(self):
        deck = load_deck("1")
        self.assertEqual('Dr. "The Old" Jeffries', deck[0])
        self.assertEqual('Logos', deck[1])
        self.assertEqual('Dis', deck[2])
        self.assertEqual('Brobnar', deck[3])
        self.assertEqual(0, deck[4])
        self.assertEqual(0, deck[5])
        self.assertEqual(341, deck[6])
        self.assertEqual('d438faa9-7920-437a-8d1c-682fade5d350', deck[7][0])

    def test_total_decks(self):
        count = int(total_decks())
        self.assertTrue(count > 120000)


if __name__ == '__main__':
    unittest.main()
