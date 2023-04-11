
import gspread
from google.oauth2.service_account import Credentials


#def authenticate():

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

# Get the auth_dict worksheet

auth_dict_worksheet = SHEET.worksheet('auth_dict')
data = auth_dict_worksheet.get_all_values()
print(data)
