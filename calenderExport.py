import sqlite3
from datetime import datetime
import os
import platform

def databaseConnection(pathToBackup):
    filepath = os.path.dirname(pathToBackup) + "iBackupData\\DBFiles\\2041457d5fe04d39d0ab481178355df6781e6858.db"
    conn = sqlite3.connect(filepath)
    c = conn.cursor()
    return c


def convertCocoa(value):
    if value < 0:
        value = value * -1

    if value < 86400:
        value += 86400

    unix = datetime(1970, 1, 1)  # UTC
    cocoa = datetime(2001, 1, 1)  # UTC
    delta = cocoa - unix  # timedelta instance
    timestamp = datetime.fromtimestamp(int(value)) + delta
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')


def getCalenderItemData(pathToBackup):
    filename = os.path.dirname(pathToBackup) + "iBackupData\\Calender\\calender_records.txt"
    file = open(filename, "wb")
    c = databaseConnection(pathToBackup)
    rows = c.execute("SELECT ROWID, summary, start_date, start_tz, end_date, all_day, calendar_id FROM CalendarItem")

    for row in rows:
        if row[2] is not None and row[4] is not None:

            startTime = convertCocoa(row[2])
            endTime = convertCocoa(row[4])
            string = str(row[0]) + " | " + str(row[1]) + " | " + str(startTime) + " | " + str(row[3]) + " | " + str(
                endTime) + \
                     " | " + str(row[5]) + " | " + str(row[6]) + "\n"
            file.write(string.encode(encoding='UTF-8'))



def main():
    getCalenderItemData("D:\cc9e2052aae826987a63f0cd60e81369774adeb4")


main()