from datetime import datetime

def newDate(date):
    now = datetime.now()
    month, day = map(int, date.split('-'))
    isoDate = f'{now.year}-{month:02d}-{day:02d}'
    return isoDate

def formattedHour(hour):
    removedLetterString = []
    for char in hour:
       if char.isdigit() or char == '.':
           removedLetterString.append(char)
    return "".join(removedLetterString)

# Goal is to turn into [YYYY-MM-DD XX:XX AM, YYYY-MM-DD XX:XX PM]
string = '02:00 PM - 09:00 PM'
stringTwo = "2-4"

def timeBlock(shift):
    delimiter = "-"
    shift = shift.split(delimiter)
    startTime = f'{newDate(stringTwo)} {shift[0].strip()}'
    endtime = f"{newDate(stringTwo)} {shift[1].strip()}"
    timeBlockList = [startTime, endtime]

    return timeBlockList

print(timeBlock(string))
