import sqlite3
from datetime import datetime
import os

def databaseConnection(pathToBackup):
    filepath = os.path.dirname(pathToBackup) + "\\iBackupData\\DBFiles\\5a4935c78a5255723f707230a451d79c540d2741.db"
    conn = sqlite3.connect(filepath)
    c = conn.cursor()
    return c


def convertCocoa(value):
    unix = datetime(1970, 1, 1)  # UTC
    cocoa = datetime(2001, 1, 1)  # UTC
    delta = cocoa - unix  # timedelta instance
    timestamp = datetime.fromtimestamp(int(value)) + delta
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')


def getCallRecords(pathToBackup):
    filename = os.path.dirname(pathToBackup) + "\\iBackupData\\Calls\\call_records.txt"
    file = open(filename, "wb")
    c = databaseConnection(pathToBackup)
    rows = c.execute("SELECT Z_PK, ZDATE, ZDURATION, ZISO_COUNTRY_CODE, ZLOCATION, ZSERVICE_PROVIDER, ZADDRESS FROM ZCALLRECORD")

    for row in rows:
        time = convertCocoa(row[1])
        string = str(row[0]) + " | " + str(time) + " | " + str(row[2]) + " | " + str(row[3]) + " | " + str(row[4]) +\
                 " | " + str(row[5]) + " | " + str(row[6]) + "\n"
        file.write(string.encode(encoding='UTF-8'))



def Calls(path):
    getCallRecords(path)


if __name__ == '__Calls__':
    main("D:\cc9e2052aae826987a63f0cd60e81369774adeb4")