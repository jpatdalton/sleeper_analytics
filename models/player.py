from models.league import PLAYERS_DICT

COLUMNS = ['player_id',
          'full_name',
          'position',
          'in_starting_lineup',
          'age',
          'college',
          'height',
          'weight',
          'years_exp',
          'active',
          'injury_status',
          'injury_notes']

class Player:
    def gen_player_data_arr(player_id, roster_dict):
        player_data_arr = []
        player_dict = PLAYERS_DICT[player_id]

        for column in COLUMNS:
            try:
                if column == 'in_starting_lineup':
                    player_data_arr.append(player_id in roster_dict['starters'])
                else:
                    if column == 'full_name' and player_dict['position'] == 'DEF':
                        player_data_arr.append(f"{player_dict['first_name']} {player_dict['last_name']}")
                    else:
                        if not player_dict[column]:
                            player_data_arr.append(' ')
                        else:
                            player_data_arr.append(player_dict[column])
            except KeyError:
                if player_dict['position'] != 'DEF':
                    print(f"[roster load error] could not get {column} from {player_dict}")
                player_data_arr.append(' ')
        return player_data_arr