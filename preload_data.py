import gspread
from models.league import *
from models.roster import Roster
# gspread init
gc = gspread.service_account()
SPREADSHEET_ID = '1FJgNslmgCFu94_s5A_PEbbDYVmN9jgi0kDtLBFWZF-c'

spreadsheet = gc.open_by_key(SPREADSHEET_ID)

# sleeper init
LEAGUE_ID = 650064757319118848
league = League(LEAGUE_ID)


# get users
users = league.get_users()
users_dict = {}
for user in users:
    users_dict[user['user_id']] = user

print(f"got {len(users)} users")


rosters = league.get_rosters()
roster_to_users_dict = {}
for roster in rosters:
    roster_to_users_dict[roster['roster_id']] = users_dict[roster['owner_id']]['display_name']