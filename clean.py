
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
import numpy as np
import ast
import os

###############################################################################
# Functions                                                                   #
###############################################################################


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
    # remove the duplicates based on card id, this is because in rare cases
    # cards can appear in a different house 'color' and will have a different
    # card_id.
    card_df.drop_duplicates(subset='card_id', keep='first', inplace=True)
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
    # the format for some is in text but we need to change it to an array
    #deck_df['deck_list'] = \
    #    deck_df['deck_list'].apply(lambda x: np.array(ast.literal_eval(x)))
    # deck_df['deck_houses'] = \
    #    deck_df['deck_houses'].apply(lambda x: np.array(ast.literal_eval(x)))
    return(deck_df)


###############################################################################
# Code for when file is run from command line                                 #
###############################################################################


if __name__ == '__main__':
    '''
    deck_df = create_deck_df()
    print(deck_df.iloc[0])
    print("Total decks:" + str(len(deck_df)))
    print("Decks with wins:" +
          str(len(deck_df.loc[(deck_df['deck_wins'] > 0)])))

    card_df = create_card_df()
    print(card_df.iloc[0])
    print("Total cards:" + str(len(card_df)))
    print(card_df.loc[(card_df['card_title'] == 'Grasping Vines')])
    '''
