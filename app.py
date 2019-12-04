
###############################################################################
# Title: Keyforge Project                                                     #
# Student: Barry Sheppard ID: 10387786                                        #
# Task: Application to rate decks using model previously generated            #
###############################################################################


###############################################################################
# Import                                                                      #
###############################################################################
import pandas as pd
import pickle
from load import load_single_deck
from load import decode_single_deck
from clean import prepare_deck


###############################################################################
# Functions                                                                   #
###############################################################################

def prepare_deck_for_model(deck_df):
    '''returns deck_df with columns not needed by the model removed'''
    X = deck_df.drop(['deck_id', 'deck_name', 'deck_wins', 'deck_losses',
                      'house_shadows', 'house_mars', 'house_untamed',
                      'house_logos', 'house_dis', 'house_sanctum',
                      'house_brobnar', 'deck_expansion', 'expansion_coa',
                      'expansion_aoa', 'deck_list', 'card_name_list'], axis=1)
    return X


###############################################################################
# Code for when file is run from command line                                 #
###############################################################################

if __name__ == '__main__':
    # Start with a prompt for the decklist
    print("Please enter the link to your KeyForge deck")
    deck = str(input("Deck Link: "))
    deck_code = deck[-36:]  # strip out the deck code at the end of the url
    # load the deck
    deck_data = load_single_deck(deck_code)
    deck_df = decode_single_deck(deck_data)
    deck_df = prepare_deck(deck_df)
    card_df = pd.read_csv("data/cards.csv")
    X = prepare_deck_for_model(deck_df)
    # load the model and get the prediction
    lm = pickle.load(open('finalized_linear_model.sav', 'rb'))
    predictions = lm.predict(X)
    # format and output
    deck_name = str(deck_df['deck_name'][0])
    deck_score = str(round(predictions[0][0], 2))
    print("The deck " + deck_name + " has a score of " + deck_score)
