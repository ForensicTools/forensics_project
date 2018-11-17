from initalizeProgram import initProgram
from calenderExport import Calender
from callsExport import Calls
from contactExport import Contacts
from notesExport import Notes
from photoDataExport import Photos
from webHistoryExport import WebHistory
from messagesExport import Messages


def main():

    path = input("Path: ")
    initProgram(path)
    print("Initialization Done")
    Calender(path)
    print("Calender Data Collected")
    Calls(path)
    print("Calls Data Collected")
    Contacts(path)
    print("Contact Data Collected")
    Notes(path)
    print("Note Data Collected")
    Photos(path)
    print("Photo Data Collected")
    WebHistory(path)
    print("Web History Data Collected")
    Messages(path)
    print("Messages Data Collected")


main()