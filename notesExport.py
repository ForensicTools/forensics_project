import sqlite3
from datetime import datetime
import os


def databaseConnection(pathToBackup):
    filepath = os.path.dirname(pathToBackup) + "\\iBackupData\\DBFiles\\4f98687d8ab0d6d1a371110e6b7300f6e465bef2.db"
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



def getNoteData(pathToBackup):

    filename = os.path.dirname(pathToBackup) + "\\iBackupData\\Notes\\note_data.txt"
    file = open(filename, "wb")
    c = databaseConnection(pathToBackup)
    rows = c.execute("SELECT Z_PK, ZCREATIONDATE1, ZMODIFICATIONDATE1, ZSNIPPET, ZTITLE1 FROM ZICCLOUDSYNCINGOBJECT")

    for row in rows:
        if row[0] is not None and row[1] is not None and row[2] is not None and row[3] is not None and row[4] is not None:
            time = convertCocoa(row[0])
            modTime = convertCocoa(row[2])
            string = str(row[0]) + " | " + str(time) + " | " + str(modTime) + " | " + str(row[3]) + " | " + str(row[4]) + "\n"
            file.write(string.encode(encoding='UTF-8'))


def Notes(path):
    getNoteData(path)


if __name__ == '__Notes__':
    main("D:\cc9e2052aae826987a63f0cd60e81369774adeb4")