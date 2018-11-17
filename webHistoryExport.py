import sqlite3
from datetime import datetime
import os

def databaseConnection(pathToBackup):
    filepath = os.path.dirname(pathToBackup) + "iBackupData\\DBFiles\\e74113c185fd8297e140cfcf9c99436c5cc06b57.db"
    conn = sqlite3.connect(filepath)
    c = conn.cursor()
    return c

def convertCocoa(value):
    unix = datetime(1970, 1, 1)  # UTC
    cocoa = datetime(2001, 1, 1)  # UTC
    delta = cocoa - unix  # timedelta instance
    timestamp = datetime.fromtimestamp(int(value)) + delta
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')


def getWebHistory(pathToBackup):
    filename = os.path.dirname(pathToBackup) + "iBackupData\\Web History\\web_history.txt"
    file = open(filename, "wb")

    c = databaseConnection(pathToBackup)
    rows = c.execute("SELECT history_visits.id, history_visits.visit_time, history_visits.title, history_items.url,"
              " history_items.domain_expansion, history_items.visit_count from history_visits LEFT JOIN history_items"
              " ON history_items.ROWID = history_visits.history_item")

    for row in rows:
        time = convertCocoa(row[1])
        string = str(row[0]) + " | " + time + " | " + str(row[2]) + " | " + str(row[3]) + " | " + str(row[4]) + "\n"

        file.write(string.encode(encoding='UTF-8'))


def WebHistory(path):
    getWebHistory(path)


if __name__ == '__WebHistory__':
    main("D:\cc9e2052aae826987a63f0cd60e81369774adeb4")