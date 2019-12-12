
###############################################################################
# Title: Keyforge Project                                                     #
# Student: Barry Sheppard ID: 10387786                                        #
# Task: Prep data of keyforge decks                                           #
###############################################################################

# csv files are saved in the data/decks and data/cards folders. These will
# start with cards_ or decks_ then having the starting page number _ and
# the ending page number.
# Each deck page has 25 decks, each card page has details of each card from
# 25 decks. That number will vary as decks can have multiple copies of the same
# card but it will only appear once on the cards listing.
# data was in a pandas table before export. This means the table starts with
# an index. However, as multiple tables were appended to each csv this means
# the index repeats. E.g. 1 to 25 and then 1 to 25 again.

###############################################################################
# Import                                                                      #
###############################################################################
import pandas as pd
import os


###############################################################################
# Functions                                                                   #
###############################################################################

def add_house_columns(deck_df):
    ''' returns deck_df with new columns for house removing house column'''
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


def change_card_ids_array_to_names(card_list, card_df):
    ''' matches array of card_ids to names in card_df and returns names '''
    new_card_list = []
    for i in card_list:
        card = card_df.loc[(card_df['card_id'] == i)]['card_title'].item()
        new_card_list.append(card)
    return(new_card_list)


def change_card_ids_str_to_names(card_list, card_df):
    ''' matches str of card_ids to names in card_df and returns names '''
    new_card_list = []
    start = 2
    end = 38
    for i in range(36):
        card = card_df.loc[(card_df['card_id'] ==
                           card_list[start:end])]['card_title'].item()
        new_card_list.append(card)
        start = start + 40
        end = end + 40
    return(new_card_list)


def create_card_df():
    ''' load csv files from data/cards/ dir and return as single df '''
    list_of_cards = []
    files = [i for i in os.listdir("data/cards") if i.endswith("csv")]
    for file in files:
        path = "data/cards/" + file
        new_card_df = pd.read_csv(path)
        list_of_cards.append(new_card_df)
    card_df = pd.concat(list_of_cards)
    # remove the blank first column
    card_df.dropna(how='all', axis='columns', inplace=True)
    return(card_df)


def create_deck_df():
    ''' load csv files from data/decks/ dir and return as single df '''
    list_of_decks = []
    files = [i for i in os.listdir("data/decks") if i.endswith("csv")]
    for file in files:
        path = "data/decks/" + file
        new_deck_df = pd.read_csv(path)
        list_of_decks.append(new_deck_df)
    deck_df = pd.concat(list_of_decks)
    # remove the blank first column
    deck_df.dropna(how='all', axis='columns', inplace=True)
    return(deck_df)


def prepare_deck(deck_df):
    ''' takes deck_df and cleans the data for processing'''
    deck_df = add_house_columns(deck_df)
    # load the list of all cards to change the card_ids to names
    card_df = pd.read_csv("data/cards.csv")
    series_of_cards = card_df['card_title']
    list_of_cards = list(dict.fromkeys(series_of_cards))
    list_of_cards.sort()
    list_of_cards[568] = "REDACTED"
    deck_df['card_name_list'] = \
        deck_df['deck_list'].apply(change_card_ids_array_to_names,
                                   card_df=card_df)
    for n in list_of_cards:
        deck_df[n] = deck_df['card_name_list'].astype(str).str.count(n)
    # Add some expansion columns
    # CoA = Call of the Archons which was set number 1
    # AoA = Age of Ascension which was set number 2
    deck_df.loc[deck_df.deck_expansion == 435, 'expansion_coa'] = True
    deck_df.loc[deck_df.deck_expansion == 341, 'expansion_coa'] = False
    deck_df.loc[deck_df.deck_expansion == 341, 'expansion_aoa'] = True
    deck_df.loc[deck_df.deck_expansion == 435, 'expansion_aoa'] = False
    return deck_df


###############################################################################
# Code for when file is run from command line                                 #
###############################################################################

if __name__ == '__main__':

    print("This file should not be run from terminal")
