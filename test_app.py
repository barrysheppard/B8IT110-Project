
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
from app import prepare_deck_for_model


###############################################################################
# Functions                                                                   #
###############################################################################

# test the load functionality
class TestLoad(unittest.TestCase):

    def test_prepare_deck_for_model(self):
        # Need more checks here
        True


###############################################################################
# Code for when file is run from command line                                 #
###############################################################################


if __name__ == '__main__':
    unittest.main()
