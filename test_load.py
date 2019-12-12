
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
import os
from load import load_decks
from load import total_decks
from load import decode_cards
from load import decode_decks
from load import load_bulk_decks
from load import create_blank_csv
from load import load_single_deck
from load import decode_single_deck


###############################################################################
# Functions                                                                   #
###############################################################################


# test the load functionality
class TestLoad(unittest.TestCase):

    def test_create_blank_csv(self):
        # Need more checks here
        card_file_name = "card_test1_test2.csv"
        deck_file_name = "deck_test1_test2.csv"
        create_blank_csv("test1", 'test2')
        deck_df = pd.read_csv(deck_file_name)
        card_df = pd.read_csv(card_file_name)
        self.assertEqual('deck_id', deck_df.columns.values[0])
        self.assertEqual('card_id', card_df.columns.values[0])
        True

    def test_decode_cards(self):
        decks = load_decks(1, 1)
        cards_df = decode_cards(decks)
        self.assertEqual('Research Smoko', cards_df['card_title'][0])

    def test_decode_decks(self):
        decks = load_decks(1, 1)
        decks_df = decode_decks(decks)
        print(decks_df)
        # self.assertEqual('Research Smoko', cards_df['card_title'][0])
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

    def test_total_load_bulk_decks(self):
        True

    def test_load_single_deck(self):
        True

    def test_decode_single_deck(self):
        True

    def tearDown(self):
        card_file_name = "card_test1_test2.csv"
        deck_file_name = "deck_test1_test2.csv"
        os.remove(card_file_name)
        os.remove(deck_file_name)

###############################################################################
# Code for when file is run from command line                                 #
###############################################################################


if __name__ == '__main__':
    unittest.main()
