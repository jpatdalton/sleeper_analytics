from preload_data import *
from models.league import PLAYERS_DICT


class Transaction:
    COLUMN_MAPPING = {
            'type': lambda x: x,
            'transaction_id': lambda x: x,
            'status': lambda x: x,
            'roster_ids': lambda x: ', '.join([roster_to_users_dict[roster_id] for roster_id in x]),
            'drops': lambda x: ', '.join([f"{PLAYERS_DICT[player_id]['first_name']} {PLAYERS_DICT[player_id]['last_name']}" for player_id in x]),
            'creator': lambda x: users_dict[x]['display_name'],
            'adds': lambda x: ', '.join([f"{PLAYERS_DICT[player_id]['first_name']} {PLAYERS_DICT[player_id]['last_name']}" for player_id in x])
            }

    def update_worksheet_with_transactions(worksheet, transaction_rows):
        import pdb
        #pdb.set_trace()
        worksheet.batch_update([{
        'range': 'A1:H1',
        'values': [list(Transaction.COLUMN_MAPPING.keys()) + ['week']]},
        {'range': f"A2:H{len(transaction_rows)+2}",
        'values': transaction_rows}
        ])

    def generate_transaction_row(transaction_dict, week):
        import pdb
        #pdb.set_trace()
        transaction_row = []
        for column, func in Transaction.COLUMN_MAPPING.items():
            if transaction_dict[column]:
                transaction_row.append(func(transaction_dict[column]))
            else:
                transaction_row.append('')

        transaction_row.append(week)

        return transaction_row


