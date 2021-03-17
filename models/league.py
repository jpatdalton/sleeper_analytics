from sleeper_wrapper import League, Players
import json


def update_cached_player_data():
    players = Players()
    players_data = players.get_all_players()
    with open('cached_data/players.json', 'w') as f:
            json.dump(players_data, f)


def get_cached_player_data():
    with open('cached_data/players.json', 'r') as f:
        players = json.load(f)
    return players


PLAYERS_DICT = get_cached_player_data()