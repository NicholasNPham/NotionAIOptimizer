import datetime

testDict = {'2025-09-07': ['No Shift Scheduled', 0], '2025-09-06': [['2025-09-06T05:30:00-04:00', '2025-09-06T14:30:00-04:00'], 9.0]}

for k, v in testDict.items():
    if v[0] != 'No Shift Scheduled':

        findStartTime = v[0][0][11:16]
        findEndTime  = v[0][1][11:16]

        print(findStartTime, findEndTime)
        if findStartTime == "05:30":
            print("Opening Shift")
        elif findEndTime == "21:00":
            print("Closing Shift")
        elif findStartTime == "10:00":
            print("Curbside Shift")
        else:
            print("Misc Shift")



