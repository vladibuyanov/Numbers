import gspread


def reader():
    sa = gspread.service_account(filename='service_account.json')
    sh = sa.open('Numbers')
    wks = sh.worksheet('Orders')
    return wks.get_all_values()[1:]
