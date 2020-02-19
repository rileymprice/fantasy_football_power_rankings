import sleeper_wrapper
import json

PLAYERS = sleeper_wrapper.Players()

all_players = PLAYERS.get_all_players()

with open("players.json", "w") as player_file:
    json.dump(all_players, player_file)
