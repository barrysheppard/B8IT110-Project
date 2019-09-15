
#####################################################################
# Title: Keyforge Project                                           #
# Student: Barry Sheppard ID: 10387786                              #
# Task: Load keyforge decks from https://www.keyforgegame.com       #
#####################################################################


#####################################################################
# Import                                                            #
#####################################################################
import requests
import json
#####################################################################
# Functions                                                         #
#####################################################################


#####################################################################
# Code                                                              #
#####################################################################

# This will load the very first deck and only that deck
deck_number = "1"
url = "https://www.keyforgegame.com/api/decks/?page=" + deck_number + "&page_size=1"
r = requests.get(url)
data = json.loads(r.content.decode())
# print(data)

# Each deck has the following
# data - This is the dictionary of all the following
#    name - This is the name of the deck e.g. 'Dr. "The Old" Jeffries'
#    expansion - This is the release wave the deck was in
#    power_level - This is calculated 'strength' of the deck based on wis
#    chains - This is a penalty in play for being poewrful
#    wins - The number of wins in tournaments
#    losses - The number of losses in tournaments
#    id - The unique reference for the deck
#    is_my_deck - When you're logged in, this is True if you own the deck
#    cards - This is an array of ids giving all the cards in the deck
#    notes - When you're logged in, your notes appear here
#    is_my_favorite - When you're logged in, you can flag this
#    is_on_my_watchlist - When you're logged in, you can flag this
#    casual_wins - This is the number of casual wins as recorded by owner
#    casual_losses - This is the number of casual losses as recorded by owner
#    set_era_cards - Some cards come from different expansions
# _links - This has some extra data, see below
#    houses - Each deck has 3 houses, every card is in one of those 3
# count - This is the total number of decks registered in the database


print('Total Decks:', data['count'])
print('Deck Name:', data['data'][0]['name'])
house1 = data['_linked']['houses'][0]['name']
house2 = data['_linked']['houses'][1]['name']
house3 = data['_linked']['houses'][2]['name']
print('Houses:', house1, house2, house3)
