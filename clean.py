
###############################################################################
# Title: Keyforge Project                                                     #
# Student: Barry Sheppard ID: 10387786                                        #
# Task: Prep data of keyforge decks                                           #
###############################################################################

# csv files are saved in the data/ folder. These will be cards or decks
# starting with cards_ or decks_ then having the starting page number _ and
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


###############################################################################
# Code for when file is run from command line                                 #
###############################################################################

if __name__ == '__main__':
    """
    # load up the decks
    list_of_decks = []
    files = [i for i in os.listdir("data/decks") if i.endswith("csv")]
    for file in files:
        path = "data/decks/" + file
        new_deck_df = pd.read_csv(path)
        list_of_decks.append(new_deck_df)
    deck_df = pd.concat(list_of_decks)
    # remove the blank first column
    deck_df.dropna(how='all', axis='columns', inplace=True)

    print(deck_df.iloc[0])
    print("Total decks:" + str(len(deck_df)))
    print("Decks with wins:" +
          str(len(deck_df.loc[(deck_df['deck_wins'] > 0)])))

    """
    # load up the cards
    list_of_cards = []
    files = [i for i in os.listdir("data/cards") if i.endswith("csv")]
    for file in files:
        path = "data/cards/" + file
        new_card_df = pd.read_csv(path)
        list_of_cards.append(new_card_df)
    card_df = pd.concat(list_of_cards)
    # remove the blank first column
    card_df.dropna(how='all', axis='columns', inplace=True)
    # remove the duplicats of cards
    card_df.drop_duplicates(subset=None, keep='first', inplace=True)

    print(card_df.iloc[0])
    print("Total cards:" + str(len(card_df)))
