import gspread

class GsheetUtils:
    def fetch_or_create_worksheet(spreadsheet, name):
        try:
            work_sheet = spreadsheet.worksheet(name)
        except gspread.exceptions.WorksheetNotFound:
            print(f"Worksheet {name} not found, creating a new sheet")
            work_sheet = spreadsheet.add_worksheet(title=name, rows="100", cols="20")
        return work_sheet