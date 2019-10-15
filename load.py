
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
import time
from requests.exceptions import HTTPError

###############################################################################
# Functions                                                                   #
###############################################################################


def create_blank_csv(start_num, end_num):
    ''' Creates deck.csv and cards.csv with required headers and suffix'''
    # creates file for decks
    deck_file_name = "deck_" + str(start_num) + "_" + str(end_num) + ".csv"
    df_deck = pd.DataFrame(columns=['deck_id', 'deck_name', 'deck_wins',
                                    'deck_losses', 'deck_expansion',
                                    'deck_list', 'houses'])
    df_deck.to_csv(deck_file_name, header=True)
    # creates file for cards
    card_file_name = "card_" + str(start_num) + "_" + str(end_num) + ".csv"
    df_card = pd.DataFrame(columns=['card_id', 'card_title', 'card_type',
                                    'card_amber', 'card_power', 'card_armor',
                                    'card_traits'])
    df_card.to_csv(card_file_name, header=True)


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


def load_bulk_decks(start_num, end_num):
    """Save decks and cards from .csv files"""
    while start_num <= end_num:
        data = load_decks(start_num, 25)
        new_decks = decode_decks(data)
        new_decks.to_csv('decks.csv', mode='a', header=False)
        new_cards = decode_cards(data)
        new_cards.to_csv('cards.csv', mode='a', header=False)
        # each page has 25 decks, we increment by pages not decks
        print("Added page: " + str(start_num))
        start_num += 1
        # As the website has a 429 'too many requests' response if it
        # gets overwhelmed, we're adding a 30 sec break after every 5
        # pages
        if ((start_num-1) % 5) == 0:
            print("Sleeping")
            time.sleep(60)
    print("Finished")


def load_decks(start_num, num_load):
    """Return details of max 25 decks from keyforgegame.com website"""
    website = "https://www.keyforgegame.com/api/decks/"
    start = "?page=" + str(start_num)
    num_decks = "&page_size=" + str(num_load)
    end = "&links=cards"
    url = website + start + num_decks + end
    try:
        r = requests.get(url, headers={'User-agent': 'Keyforge Bot 0.1'})
        # If the response was successful, no Exception will be raised
        r.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        # We're expecting 429 (too many requests) errors
        print("Waiting for 60 minutes")
        time.sleep(3600)  # Delay for 60 minutes, then try again
        r = requests.get(url, headers={'User-agent': 'Keyforge Bot 0.1'})
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        data = json.loads(r.content.decode())
    return(data)


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

    start_num = 27001
    end_num = 29000

    create_blank_csv(start_num, end_num)
    load_bulk_decks(start_num, end_num)
