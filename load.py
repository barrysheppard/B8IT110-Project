
#####################################################################
# Title: Keyforge Project                                           #
# Student: Barry Sheppard ID: 10387786                              #
# Task: Load keyforge decks from https://www.keyforgegame.com       #
#####################################################################

# Decks are listed on the keyforgegame.com website.
# The API there returns details of a single deck
# Each deck has the following
# data - This is the dictionary of all the following
#    name - This is the name of the deck e.g. 'Dr. "The Old" Jeffries'
#    expansion - This is the release wave the deck was in
#    power_level - This is calculated 'strength' of the deck based on wins
#    chains - This is a penalty in play for being poewrful
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

#####################################################################
# Import                                                            #
#####################################################################
import requests
import json

#####################################################################
# Functions                                                         #
#####################################################################


def load_deck(deck_number):
    """Return details of deck from keyforgegame.com website"""
    # Load the deck in json format
    website = "https://www.keyforgegame.com/api/decks/?page="
    url = website + deck_number + "&page_size=1"
    r = requests.get(url)
    data = json.loads(r.content.decode())
    # Pull out the data of interest
    deck_name = data['data'][0]['name']
    deck_house1 = data['_linked']['houses'][0]['name']
    deck_house2 = data['_linked']['houses'][1]['name']
    deck_house3 = data['_linked']['houses'][2]['name']
    deck_wins = data['data'][0]['wins']
    deck_losses = data['data'][0]['losses']
    deck_expansion = data['data'][0]['expansion']
    deck_card_list = data['data'][0]['cards']
    return [deck_name, deck_house1, deck_house2, deck_house3, deck_wins,
            deck_losses, deck_expansion, deck_card_list]


def total_decks():
    """Returns the total number of decks registered on keyforgegame.com"""
    # We load the details of deck number 1
    # Every deck detail includes the number of all decks registered
    website = "https://www.keyforgegame.com/api/decks/?page="
    url = website + "1" + "&page_size=1"
    r = requests.get(url)
    data = json.loads(r.content.decode())
    return data['count']


#####################################################################
# Code                                                              #
#####################################################################

if __name__ == '__main__':

    # This will load the very first deck and only that deck
    deck_number = "1"
    deck = load_deck(deck_number)

    print('Total Decks:', total_decks())
    print('Deck Name:', deck[0])
    print('Houses:', deck[1], deck[2], deck[3])
    print('Wins:', deck[4])
    print('Losses:', deck[5])
    print('Expansion:', deck[6])
    print('Cards:', deck[7])
