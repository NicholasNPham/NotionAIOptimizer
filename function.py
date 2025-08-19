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

string = "7.00hr"

def formattedHour(hour):
    removedLetterString = []
    for char in hour:
       if char.isdigit() or char == '.':
           removedLetterString.append(char)
    print(removedLetterString)
    return "".join(removedLetterString)

newHour = (formattedHour(string))
print(newHour)

