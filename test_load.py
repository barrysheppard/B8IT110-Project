
###############################################################################
# Title: Keyforge Project                                                     #
# Student: Barry Sheppard ID: 10387786                                        #
# Task: Load keyforge decks from https://www.keyforgegame.com                 #
###############################################################################


###############################################################################
# Import                                                                      #
###############################################################################
import unittest
import pandas as pd
from load import load_decks
from load import total_decks
from load import decode_cards
from load import decode_decks
from load import load_bulk_decks
from load import create_blank_csv


###############################################################################
# Functions                                                                   #
###############################################################################


# test the load functionality
class TestLoad(unittest.TestCase):

    def test_create_blank_csv(self):
        # Need more checks here
        True

    def test_decode_cards(self):
        decks = load_decks(1, 1)
        cards_df = decode_cards(decks)
        # Need more checks here
        True

    def test_decode_decks(self):
        decks = load_decks(1, 1)
        decks_df = decode_decks(decks)
        # self.assertIsInstance(pd.DataFrame, type(decks_df))
        # Need more checks here
        True

    def test_load_bulk_decks(self):
        # Need more checks here
        True

    def test_load_decks(self):
        # Starting with deck 1, load 4 decks
        decks = load_decks(1, 4)
        # each load has 3 elements: 'data', 'count', '_linked'
        self.assertEqual(3, len(decks))
        # count the 4 decks
        self.assertEqual(4, len(decks['data']))

    def test_total_decks(self):
        count = int(total_decks())
        self.assertTrue(count > 120000)


###############################################################################
# Code for when file is run from command line                                 #
###############################################################################


if __name__ == '__main__':
    unittest.main()
