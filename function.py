import zoneinfo
from datetime import datetime
from zoneinfo import ZoneInfo

tz = ZoneInfo("America/New_York")

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

# Testing Function String/StringTwo
string = '02:00 PM - 09:00 PM'
stringTwo = "2025-08-18"

def timeBlock(shift, date):
    if shift != "No Shift Scheduled":
        times = shift.split('-')
        dateTimes = []
        isoTimes = []

        # Crazy that date time already formats as ISO 6801 just needed to added TimeZone
        for time in times:
            dt = datetime.strptime(f"{date} {time.strip()}", "%Y-%m-%d %I:%M %p")
            dateTime = dt.replace(tzinfo=tz)
            dateTimes.append(dateTime)
            isoTimes.append(dateTime.isoformat())

        hours = (dateTimes[1] - dateTimes[0]).total_seconds() / 3600
        return [isoTimes, hours]
    else:
        noShiftFound = ['No Shift Scheduled', 0]
        return noShiftFound

