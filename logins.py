import gspread
from google.oauth2.service_account import Credentials


# Set up Google Sheets credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Battleship')
LOGINS = SHEET.worksheet('auth_dict')


def get_logins() -> list:
    """
    Pull all values from auth_dict work sheet and return as list
    of lists
    """
    login_data = LOGINS.get_all_records()
    return login_data
