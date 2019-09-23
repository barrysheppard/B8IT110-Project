
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

###############################################################################
# Functions                                                                   #
###############################################################################


def load_deck(deck_number):
    """Return details of deck from keyforgegame.com website"""
    # Load the deck in json format
    website = "https://www.keyforgegame.com/api/decks/?page="
    url = website + deck_number + "&page_size=1&links=cards"
    r = requests.get(url)
    data = json.loads(r.content.decode())
    # Pull out the data of interest
    deck_name = data['data'][0]['name']
    deck_wins = data['data'][0]['wins']
    deck_losses = data['data'][0]['losses']
    deck_expansion = data['data'][0]['expansion']
    card_list = extract_detail(data['_linked']['cards'], 'card_title')
    card_house = extract_detail(data['_linked']['cards'], 'house')
    card_type = extract_detail(data['_linked']['cards'], 'card_type')
    card_amber = extract_detail(data['_linked']['cards'], 'amber')
    card_power = extract_detail(data['_linked']['cards'], 'power')
    card_armor = extract_detail(data['_linked']['cards'], 'armor')
    return [deck_name, deck_wins, deck_losses, deck_expansion, card_list,
            card_house, card_type, card_amber, card_power, card_armor]


def extract_detail(card_list, detail):
    """Returns the list of detail from a json decklist"""
    deck_list = []
    for card in card_list:
        deck_list.append(card[detail])
    return deck_list


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
    deck_number = "1"
    deck = load_deck(deck_number)

    print('Total Decks:', total_decks())
    print('Deck Name:', deck[0])
    print('Wins:', deck[1])
    print('Losses:', deck[2])
    print('Expansion:', deck[3])
    print('Cards:', deck[4][0])
    print('Card House:', deck[5][0])
    print('Card Type:', deck[6][0])
    print('Card Amber:', deck[7][0])
    print('Card Power:', deck[8][0])
    print('Card Armor:', deck[9][0])
