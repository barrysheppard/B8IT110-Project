
###############################################################################
# Title: Keyforge Project                                                     #
# Student: Barry Sheppard ID: 10387786                                        #
# Task: Load keyforge decks from https://www.keyforgegame.com                 #
###############################################################################


###############################################################################
# Import                                                                      #
###############################################################################
import unittest
from load import load_deck
from load import total_decks

###############################################################################
# Code for when file is run from command line                                 #
###############################################################################


# test the load functionality
class TestLoad(unittest.TestCase):

    def test_load_deck(self):
        deck = load_deck("1")
        self.assertEqual('Dr. "The Old" Jeffries', deck[0])
        self.assertEqual(0, deck[1])
        self.assertEqual(0, deck[2])
        self.assertEqual(341, deck[3])
        # This test will also check extract_detail function
        self.assertEqual('Research Smoko', deck[4][0])
        self.assertEqual('Logos', deck[5][0])
        self.assertEqual('Creature', deck[6][0])
        self.assertEqual(0, deck[7][0])
        self.assertEqual('2', deck[8][0])
        self.assertEqual('0', deck[9][0])
        # There should be 30 cards in total in each deck
        self.assertEqual(30, len(deck[5]))

    def test_total_decks(self):
        count = int(total_decks())
        self.assertTrue(count > 120000)


if __name__ == '__main__':
    unittest.main()
