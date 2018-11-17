import sqlite3
from datetime import datetime
import os


def databaseConnection(pathToBackup):
    filepath = os.path.dirname(pathToBackup) + "iBackupData\\DBFiles\\12b144c0bd44f2b3dffd9186d3f9c05b917cee25.db"
    conn = sqlite3.connect(filepath)
    c = conn.cursor()
    return c

def convertCocoa(value):
    unix = datetime(1970, 1, 1)  # UTC
    cocoa = datetime(2001, 1, 1)  # UTC
    delta = cocoa - unix  # timedelta instance
    timestamp = datetime.fromtimestamp(int(value)) + delta
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')

def getPhotoData(pathToBackup):

    filename = os.path.dirname(pathToBackup) + "iBackupData\\Photo Data\\photo_data.txt"
    file = open(filename, "wb")
    c = databaseConnection(pathToBackup)
    rows = c.execute("SELECT ZDATECREATED, ZDURATION, ZLONGITUDE, ZLATITUDE, ZDIRECTORY, ZFILENAME FROM ZGENERICASSET")

    for row in rows:
        if row[0] is None or row[1] is None or row[2] is None or row[3] is None or row[4] is None or row[5] is None:
            print("err")
        else:
            time = convertCocoa(row[0])
            string = str(time) + " | " + str(row[1]) + " | " + str(row[2]) + " | " + str(row[3]) + " | " + str(row[4]) + " | " + row[5] + "\n"
            file.write(string.encode(encoding='UTF-8'))



def main():
    getPhotoData("D:\cc9e2052aae826987a63f0cd60e81369774adeb4")


main()