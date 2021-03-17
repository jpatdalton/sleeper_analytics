
class TradedPicks:
    def update_worksheet_with_traded_picks(roster_to_users_dict, league, worksheet):
        COLUMN_MAPPING = {
                    'previous_owner_id': lambda x: roster_to_users_dict[x],
                    'owner_id': lambda x: roster_to_users_dict[x],
                    'round': lambda x: x,
                    'season': lambda x: x
                }

        GSHEET_COLUMNS = ['traded_from', 'traded_to', 'round', 'season']

        traded_picks = league.get_traded_picks()


        traded_picks_to_upload = []

        for traded_pick in traded_picks:
            traded_pick_arr = []
            for api_mapping, func in COLUMN_MAPPING.items():
                traded_pick_arr.append(func(traded_pick[api_mapping]))
            traded_picks_to_upload.append(traded_pick_arr)

        traded_picks_to_upload.sort(key=lambda x: (x[3], x[2], x[1]), reverse=False)

        worksheet.batch_update([{
        'range': 'A1:D1',
        'values': [GSHEET_COLUMNS]},
        {'range': f"A2:D{len(traded_picks_to_upload)+2}",
        'values': traded_picks_to_upload}
        ])