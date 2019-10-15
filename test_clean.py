
###############################################################################
# Title: Keyforge Project                                                     #
# Student: Barry Sheppard ID: 10387786                                        #
# Task: clean keyforge decks from https://www.keyforgegame.com                #
###############################################################################


###############################################################################
# Import                                                                      #
###############################################################################
import unittest
import pandas as pd
from clean import create_card_df
from clean import create_deck_df

###############################################################################
# Functions                                                                   #
###############################################################################


# test the load functionality
class TestLoad(unittest.TestCase):

    def test_create_card_df(self):
        # Need more checks here
        True

    def test_create_deck_df(self):
        # Need more checks here
        True


###############################################################################
# Code for when file is run from command line                                 #
###############################################################################


if __name__ == '__main__':
    unittest.main()
