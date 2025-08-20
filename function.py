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

# Goal is to turn into [YYYY-MM-DD XX:XX AM, YYYY-MM-DD XX:XX PM]
string = '02:00 PM - 09:00 PM'
stringTwo = "2-4"

def timeBlock(shift,date):
    delimiter = "-"
    shift = shift.split(delimiter)
    startTime = f'{newDate(stringTwo)} {shift[0].strip()}'
    endtime = f"{newDate(stringTwo)} {shift[1].strip()}"
    timeBlockList = [startTime, endtime]

    return timeBlockList

print(timeBlock(string,stringTwo))
