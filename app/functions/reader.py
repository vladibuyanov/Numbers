import gspread
from app.config import credentials


def reader():
    sa = gspread.service_account_from_dict(credentials)
    sh = sa.open('Numbers')
    wks = sh.worksheet('Orders')
    return wks.get_all_values()[1:]
