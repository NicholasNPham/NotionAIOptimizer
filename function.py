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

def newFormattedTime(time):
    lastTwoChars = time[-2:]
    if lastTwoChars == 'PM':
        addingTime = int(time[:2]) + 12
        stringTime = f'{addingTime}:{time[3:5]}'
    elif time == '12:00 AM':
        stringTime = '00:00'
    else:
        stringTime = f'{time[0:2]}:{time[3:5]}'
    return stringTime

# Testing Function String/StringTwo
# string = '02:00 PM - 09:00 PM'
# stringTwo = "2-4"

def timeBlock(shift):
    if shift != "No Shift Scheduled":
        delimiter = "-"
        shift = shift.split(delimiter)

        startTime = f'{newDate(stringTwo)}T{newFormattedTime(shift[0].strip())}:00-05:00'
        endtime = f"{newDate(stringTwo)}T{newFormattedTime(shift[1].strip())}:00-05:00"
        timeBlockList = [startTime, endtime]
    else:
        timeBlockList = ['No Shift Scheduled', 0]

    return timeBlockList

# Calling timeBlock Function
# print(timeBlock(string))
