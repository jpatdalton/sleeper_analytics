from models.player import Player, COLUMNS

class Roster:
    def update_worksheet_with_roster(worksheet, roster_dict):
        players_update_arr = []
        for player_id in roster_dict['players']:
            player_data_arr = Player.gen_player_data_arr(player_id, roster_dict)

            players_update_arr.append(player_data_arr)

        players_update_arr.sort(key=lambda x: (x[3], x[2]), reverse=True)
        worksheet.batch_update([{
        'range': 'A1:L1',
        'values': [COLUMNS]},
        {'range': f"A2:L{len(players_update_arr)+2}",
        'values': players_update_arr}
        ])

