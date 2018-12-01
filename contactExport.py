import sqlite3
from datetime import datetime
import os

def databaseConnection(pathToBackup):
    filepath = os.path.dirname(pathToBackup) + "\\iBackupData\\DBFiles\\31bb7ba8914766d4ba40d6dfb6113c8b614be442.db"
    conn = sqlite3.connect(filepath)
    c = conn.cursor()
    return c


def convertCocoa(value):
    unix = datetime(1970, 1, 1)  # UTC
    cocoa = datetime(2001, 1, 1)  # UTC
    delta = cocoa - unix  # timedelta instance
    timestamp = datetime.fromtimestamp(int(value)) + delta
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')


def getContactData(pathToBackup):

    filename = os.path.dirname(pathToBackup) + "\\iBackupData\\Contacts\\contact_data.txt"
    file = open(filename, "wb")
    c = databaseConnection(pathToBackup)
    rows = c.execute("SELECT docid, c0First, c1Last, c2Middle, c6Organization, c11JobTitle, c12Nickname, c16Phone, c17Email, c18Address FROM ABPersonFullTextSearch_content")
    string = ""
    for row in rows:
        for i in range(10):
            if row[i] is not None:
                if i != 9:
                    string += str(row[i]) + " | "
                else:
                    string += str(row[i])
        string += "\n"
        file.write(string.encode(encoding='UTF-8'))
        string = ""



def Contacts(path):
    getContactData(path)


if __name__ == '__Contacts__':
    main("D:\cc9e2052aae826987a63f0cd60e81369774adeb4")