import datetime

def newDate(date):
    now = datetime.datetime.now()
    year = now.year
    if date[1] == '-':
        date = "0" + date
    else:
        date = date

    isoDate = str(year)+ '-' + date
    return isoDate