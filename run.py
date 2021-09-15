import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figures input from the user
    """
    while True:
        print("Please enter sales data from the alst market.")
        print("Data should be six numbers, seperated by commas.")
        print("Example: 10, 20, 30, 40, 50, 60\n")

        data_srt = input("Enter data here:")
        
        sales_data = data_srt.split(",")
        
        if validate_data(sales_data):
            print("Data is valid")
            break
    
    return sales_data

def validate_data(values):
    """ 
    Inside try, converts all data to ints, 
    Raise ValueError if string can not be converted to int, 
    or if not exactly 6 values
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"exactly six values required, you gave {len(values)} values"
            )
    except ValueError as e:
        print(f"Invalid data {e}, please try again.\n")
        return False
    
    return True

def update_sales_worksheet(data):
    """ 
    update sales worksheet, add new row with the list data provided
    """

    print("updating sales worksheet..........\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("sales worksheet updated successfully\n")

data = get_sales_data()

sales_data = [int(num) for num in data]
update_sales_worksheet(sales_data)
