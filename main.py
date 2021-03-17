import pdb

from gsheet_utils import GsheetUtils

from models.traded_picks import TradedPicks
from models.transaction import Transaction
from preload_data import *


# traded picks
print(f"updating traded picks worksheet")
#worksheet = GsheetUtils.fetch_or_create_worksheet(spreadsheet, 'traded picks')
#TradedPicks.update_worksheet_with_traded_picks(roster_to_users_dict, league, worksheet)

# transactions
print(f"updating transactions worksheet")

transaction_rows = []

for week in range(1, 16):
    transactions = league.get_transactions(week)
    for transaction_dict in transactions:
        transaction_row = Transaction.generate_transaction_row(transaction_dict, week)
        transaction_rows.append(transaction_row)
    print(f"Got transactions for week [{week}]")


worksheet = GsheetUtils.fetch_or_create_worksheet(spreadsheet, 'transactions')
Transaction.update_worksheet_with_transactions(worksheet, transaction_rows)

import pdb
pdb.set_trace()
# update roster sheets

print("creating roster worksheets")
rostered_players = set()
for roster in rosters:
    user_display_name = users_dict[roster['owner_id']]['display_name']
    roster_sheet_name = f"{user_display_name}_roster"
    print(f"updating {roster_sheet_name} worksheet")
    #worksheet = GsheetUtils.fetch_or_create_worksheet(spreadsheet, roster_sheet_name)
    #Roster.update_worksheet_with_roster(worksheet, roster)
    rostered_players.update(roster['players'])

# unrostered players
print(f"updating unrostered worksheet")
worksheet = GsheetUtils.fetch_or_create_worksheet(spreadsheet, 'unrostered')
unrostered_dict = {}
unrostered_dict['players'] = set(PLAYERS_DICT.keys()) - rostered_players
unrostered_dict['starters'] = []
# Roster.update_worksheet_with_roster(worksheet, unrostered_dict)

