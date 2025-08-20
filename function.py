from datetime import datetime

def newDate(date):
    now = datetime.now()
    formattingDate = "%m-%d"
    date = datetime.strptime(date,formattingDate)
    isoDate = f'{now.year}-{date.strftime("%m-%d")}'
    return isoDate

def formattedHour(hour):
    removedLetterString = []
    for char in hour:
       if char.isdigit() or char == '.':
           removedLetterString.append(char)
    return "".join(removedLetterString)



