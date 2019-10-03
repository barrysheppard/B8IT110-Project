
###############################################################################
# Title: Keyforge Project                                                     #
# Student: Barry Sheppard ID: 10387786                                        #
# Task: Load keyforge decks from https://www.keyforgegame.com                 #
###############################################################################

# Decks are listed on the keyforgegame.com website.
# The API there returns details of a single deck
# Each deck has the following
# data - This is the dictionary of all the following
#    name - This is the name of the deck e.g. 'Dr. "The Old" Jeffries'
#    expansion - This is the release wave the deck was in
#    power_level - This is calculated 'strength' of the deck based on wins
#    chains - This is a penalty in play for being powerful
#    wins - The number of wins in tournaments
#    losses - The number of losses in tournaments
#    id - The unique reference for the deck
#    is_my_deck - When you're logged in, this is True if you own the deck
#    cards - This is an array of ids giving all the cards in the deck
#    notes - When you're logged in, your notes appear here
#    is_my_favorite - When you're logged in, you can flag this
#    is_on_my_watchlist - When you're logged in, you can flag this
#    casual_wins - This is the number of casual wins as recorded
#    casual_losses - This is the number of casual losses as recorded
#    set_era_cards - Some cards come from different expansions
# _links - This has some extra data, see below
#    houses - Each deck has 3 houses, every card is in one of those 3
# count - This is the total number of decks registered in the database
# _linked - This has more detailed info for houses and cards
#    houses - id, name, image
#    cards - id, card_title, house, card_type, front_image, card_text,
#            traits, amber, power, armor, rarity, flavor_Text, card_number,
#            expansion, is_maverick


###############################################################################
# Import                                                                      #
###############################################################################
import requests
import json
import pandas as pd
import numpy as np

###############################################################################
# Functions                                                                   #
###############################################################################


def load_decks(start_num, num_load):
    """Return details of max 25 decks from keyforgegame.com website"""
    website = "https://www.keyforgegame.com/api/decks/"
    start = "?page=" + str(start_num)
    num_decks = "&page_size=" + str(num_load)
    end = "&links=cards"
    url = website + start + num_decks + end
    r = requests.get(url)
    data = json.loads(r.content.decode())
    return(data)


def load_bulk_decks(start_num, num_load):
    """Return details of decks from keyforgegame.com website"""
    bulk_decks = []
    while start_num <= num_load:
        data = load_decks(start_num, 25)
        bulk_decks += data
        start_num += 25
    return bulk_decks


def decode_decks(data):
    """Takes a list of decks in json format and returns decks in pd df"""
    df = pd.DataFrame(columns=['deck_id', 'deck_name', 'deck_wins',
                               'deck_losses', 'deck_expansion', 'deck_list',
                               'houses'])
    decks = data['data']
    for i in decks:
        deck_id = i['id']
        deck_name = i['name']
        deck_wins = i['wins']
        deck_losses = i['losses']
        deck_expansion = i['expansion']
        deck_list = i['_links']['cards']
        deck_houses = i['_links']['houses']
        new_deck = [deck_id, deck_name, deck_wins, deck_losses, deck_expansion,
                    deck_list, deck_houses]
        df = df.append(pd.Series(new_deck, index=df.columns),
                       ignore_index=True)
    return df


def decode_cards(data):
    """Takes a list of decks in json format and returns cards in pd df"""
    df = pd.DataFrame(columns=['card_id', 'card_title', 'card_type',
                               'card_amber', 'card_power', 'card_armor',
                               'card_traits'])
    decks = data['_linked']['cards']
    for i in decks:
        card_id = i['id']
        card_title = i['card_title']
        card_type = i['card_type']
        card_amber = i['amber']
        card_power = i['power']
        card_armor = i['armor']
        card_traits = i['traits']
        new_card = [card_id, card_title, card_type, card_amber, card_power,
                    card_armor, card_traits]
        df = df.append(pd.Series(new_card, index=df.columns),
                       ignore_index=True)
    return df


def total_decks():
    """Returns the total number of decks registered on keyforgegame.com"""
    # We load the details of deck number 1
    # Every deck detail includes the number of all decks registered
    website = "https://www.keyforgegame.com/api/decks/?page="
    url = website + "1" + "&page_size=1"
    r = requests.get(url)
    data = json.loads(r.content.decode())
    return data['count']


###############################################################################
# Code for when file is run from command line                                 #
###############################################################################

if __name__ == '__main__':

    # This will load the very first deck and only that deck

    data = load_bulk_decks(start_num=1, num_load=100)
    print(data)
