
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


###############################################################################
# Functions                                                                   #
###############################################################################


def change_card_array_ids_to_names(card_list):
    new_card_list = []
    card_df = pd.read_csv("data/cards.csv")
    for i in card_list:
        card = card_df.loc[(card_df['card_id'] == i)]['card_title'].item()
        new_card_list.append(card)
    return(new_card_list)


def add_house_columns(deck_df):
    if 'Brobnar' in deck_df['houses'].values:
        deck_df['house_brobnar'] = True
    else:
        deck_df['house_brobnar'] = False
    if 'Dis' in deck_df['houses'].values:
        deck_df['house_dis'] = True
    else:
        deck_df['house_dis'] = False
    if 'Sanctum' in deck_df['houses'].values:
        deck_df['house_sanctum'] = True
    else:
        deck_df['house_sanctum'] = False
    if 'Mars' in deck_df['houses'].values:
        deck_df['house_mars'] = True
    else:
        deck_df['house_mars'] = False
    if 'Untamed' in deck_df['houses'].values:
        deck_df['house_untamed'] = True
    else:
        deck_df['house_untamed'] = False
    if 'Shadows' in deck_df['houses'].values:
        deck_df['house_shadows'] = True
    else:
        deck_df['house_shadows'] = False
    if 'Logos' in deck_df['houses'].values:
        deck_df['house_logos'] = True
    else:
        deck_df['house_logos'] = False
    deck_df = deck_df.drop("houses", axis=1)
    return deck_df


def prepare_deck(deck):
    deck_code = deck[-36:]  # strip out the deck code at the end of the url
    # load the deck
    deck_data = load_single_deck(deck_code)
    deck_df = decode_single_deck(deck_data)
    deck_df = add_house_columns(deck_df)
    # load the list of all cards to change the card_ids to names
    card_df = pd.read_csv("data/cards.csv")
    series_of_cards = card_df['card_title']
    list_of_cards = list(dict.fromkeys(series_of_cards))
    list_of_cards.sort()
    list_of_cards[568] = "REDACTED"
    deck_df['card_name_list'] = \
        deck_df['deck_list'].apply(change_card_array_ids_to_names)
    for n in list_of_cards:
        deck_df[n] = deck_df['card_name_list'].astype(str).str.count(n)
    # Add some expansion columns
    # CoA = Call of the Archons which was set number 1
    # AoA = Age of Ascension which was set number 2
    deck_df.loc[deck_df.deck_expansion == 435, 'expansion_coa'] = True
    deck_df.loc[deck_df.deck_expansion == 341, 'expansion_coa'] = False
    deck_df.loc[deck_df.deck_expansion == 435, 'expansion_aoa'] = True
    deck_df.loc[deck_df.deck_expansion == 341, 'expansion_aoa'] = False
    return deck_df


###############################################################################
# Code for when file is run from command line                                 #
###############################################################################

if __name__ == '__main__':
    # Start with a prompt for the decklist
    print("Please enter the link to your KeyForge deck")
    deck = str(input("Deck Link: "))
    deck_df = prepare_deck(deck)
    # Prepare the df for the model
    X = deck_df
    X = X.drop(['deck_id', 'deck_name', 'deck_wins', 'deck_losses',
                'house_shadows', 'house_mars', 'house_untamed', 'house_logos',
                'house_dis', 'house_sanctum', 'house_brobnar',
                'deck_expansion', 'expansion_coa', 'expansion_aoa',
                'deck_list', 'card_name_list'], axis=1)
    # load the model and get the prediction
    lm = pickle.load(open('finalized_linear_model.sav', 'rb'))
    predictions = lm.predict(X)
    # format and output
    deck_name = str(deck_df['deck_name'][0])
    deck_score = str(round(predictions[0][0], 2))
    print("The deck " + deck_name + " has a score of " + deck_score)
