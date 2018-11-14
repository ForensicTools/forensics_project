import sqlite3
from datetime import datetime
import json
import hashlib
import pathlib
from pathlib import Path
from shutil import copyfile
import exifread
import exifread as ef

###BE EXTREMELY CAREFUL THIS WILL GENERATE ALOT OF DATA BASED ON THE SIZE OF YOUR IPHONE BACK UP
###


def convertCocoa(value):
    unix = datetime(1970, 1, 1)  # UTC
    cocoa = datetime(2001, 1, 1)  # UTC
    delta = cocoa - unix  # timedelta instance
    timestamp = datetime.fromtimestamp(int((value/1000000000))) + delta
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')

def databaseConnection():
    conn = sqlite3.connect('3d0d7e5fb2ce288813306e4d4636395e047a3d28.db')
    c = conn.cursor()
    return c

def getHandleIds():
    handleIds = []
    c = databaseConnection()
    rows = c.execute("SELECT ROWID FROM handle")
    for row in rows:
        handleIds += [row[0]]
    c.close()
    return handleIds


def getAttachmentROWIDs():
    attachmentIds = []
    c = databaseConnection()
    rows = c.execute("SELECT ROWID FROM attachment")
    for row in rows:
        attachmentIds += [row[0]]
    c.close()
    return attachmentIds

def getGroupChatIDs():
    groupChatIDs = []
    c = databaseConnection()
    rows = c.execute("SELECT room_name FROM chat")
    for row in rows:
        if row[0] not in groupChatIDs and row[0] is not None:
            groupChatIDs += [row[0]]
    return groupChatIDs

def createDirectories(handles):
    for handle in handles:
        file_path_handle = "C:\\Users\\Peter\\Desktop\\images\\" + str(handle)
        pathlib.Path(file_path_handle).mkdir(parents=True, exist_ok=True)




def getChatGroupMessages(pathToBackup):
    GCIds = getGroupChatIDs()
    check = createDirectories(GCIds)
    for i in range(len(GCIds)):
        filename = "C:\\Users\\Peter\\Desktop\\files\\" + str(GCIds[i]) + ".txt"
        c = databaseConnection()
        rows = c.execute("SELECT handle_id, ROWID, text, service, date, is_from_me, cache_has_attachments FROM message WHERE cache_roomnames=" + "\"" + str(GCIds[i]) + "\"")
        file = open(filename, "w+")
        arrayOfJSON = []
        for row in rows:
            if row[3] is not None:

                data = {
                    "handle_id": str(row[0]),
                    "ROWID": str(row[1]),
                    "text": str(row[2]),
                    "service": str(row[3]),
                    "date": str(row[4]),
                    "is_from_me": str(row[5]),
                    "cache_has_attachments": str(row[6])
                }

                if row[6] == 1:
                    c = databaseConnection()
                    otherRows = c.execute(
                        "SELECT attachment.filename, attachment.mime_type, attachment.is_outgoing, attachment.transfer_name FROM attachment "
                        "INNER JOIN message_attachment_join ON attachment.ROWID=message_attachment_join.attachment_id "
                        "INNER JOIN message ON message_attachment_join.message_id=message.ROWID "
                        "WHERE message.ROWID=" + str(row[1]))

                    data["attachments"] = [

                    ]

                    for string in otherRows:

                        hashString = "MediaDomain-" + string[0][2::]
                        h = hashlib.sha1(hashString.encode())
                        hash = h.hexdigest()
                        prefix = hash[0:2]
                        idxOfDot = str(string[3]).index(".")
                        extension = str(string[3])[idxOfDot::]
                        fileAndExtension = hash + extension

                        Attachementdata = {
                            "filename": fileAndExtension,
                            "mime_type": str(string[1]),
                            "is_outgoing": str(string[2]),
                            "transfer_name": str(string[3])
                        }
                        data["attachments"].append(Attachementdata)


                        source = pathToBackup + "\\" + prefix + "\\" + hash
                        destination = "C:\\Users\\Peter\\Desktop\\images\\" + str(GCIds[i]) + "\\" + hash
                        myFile = Path(source)
                        if myFile.is_file():
                            copyfile(source, destination + extension)



                    c.close()

                arrayOfJSON.append(data)

        json_data = json.dumps(arrayOfJSON, sort_keys=True, indent=4, separators=(',', ': '))
        file.write(json_data)
        file.close()


def openFile(filename):
    file = open(filename, "w+")
    return file

def closeFile(file):
    file.close()

def getIndividualChats(pathToBackup):
    ids = getHandleIds()
    createDirectories(ids)
    for i in range(len(ids)):
        filename = "C:\\Users\\Peter\\Desktop\\files\\" + str(ids[i]) + ".txt"
        c = databaseConnection()
        rows = c.execute("SELECT handle_id, ROWID, text, service, date, is_from_me, cache_has_attachments FROM message WHERE cache_roomnames IS NULL AND handle_id=" + str(ids[i]))
        file = open(filename, "w+")
        arrayOfJSON = []
        for row in rows:
            if row[3] is not None:
                    data = {
                        "handle_id": str(row[0]),
                        "ROWID": str(row[1]),
                        "text": str(row[2]),
                        "service": str(row[3]),
                        "date": str(row[4]),
                        "is_from_me": str(row[5]),
                        "cache_has_attachments": str(row[6])
                    }


                    if row[6] == 1:
                        c = databaseConnection()
                        otherRows = c.execute("SELECT attachment.filename, attachment.mime_type, attachment.is_outgoing, attachment.transfer_name FROM attachment "
                                        "INNER JOIN message_attachment_join ON attachment.ROWID=message_attachment_join.attachment_id "
                                        "INNER JOIN message ON message_attachment_join.message_id=message.ROWID "
                                        "WHERE message.ROWID=" + str(row[1]))

                        data["attachments"] = [

                        ]


                        for string in otherRows:

                            hashString = "MediaDomain-" + string[0][2::]
                            h = hashlib.sha1(hashString.encode())
                            hash = h.hexdigest()
                            prefix = hash[0:2]
                            idxOfDot = str(string[3]).index(".")
                            extension = str(string[3])[idxOfDot::]
                            fileAndExtension = hash + extension

                            Attachementdata = {
                                "filename": fileAndExtension,
                                "mime_type": str(string[1]),
                                "is_outgoing": str(string[2]),
                                "transfer_name": str(string[3])
                            }
                            data["attachments"].append(Attachementdata)


                            source = pathToBackup + "\\" + prefix + "\\" + hash
                            destination = "C:\\Users\\Peter\\Desktop\\images\\" + str(row[0]) + "\\" + hash
                            myFile = Path(source)
                            if myFile.is_file():
                                copyfile(source, destination + extension)


                        c.close()

                    arrayOfJSON.append(data)

        json_data = json.dumps(arrayOfJSON, sort_keys=True, indent=4, separators=(',', ': '))
        file.write(json_data)
        file.close()


def setup(pathToBackup):
    file_path_main = "C:\\Users\\Peter\\Documents\\iBackupData"
    pathlib.Path(file_path_main).mkdir(parents=True, exist_ok=True)

    file_path_dbFiles = "C:\\Users\\Peter\\Documents\\iBackupData\\DBFiles"
    pathlib.Path(file_path_dbFiles).mkdir(parents=True, exist_ok=True)

    source = pathToBackup + "\\Manifest.db"
    copyfile(source, file_path_dbFiles)

    source = pathToBackup + "\\3d0d7e5fb2ce288813306e4d4636395e047a3d28"
    copyfile(source, file_path_dbFiles)







def main():
    file_path = "C:\\Users\\Peter\\Desktop\\images"
    pathlib.Path(file_path).mkdir(parents=True, exist_ok=True)
    file_path = "C:\\Users\\Peter\\Desktop\\files"
    pathlib.Path(file_path).mkdir(parents=True, exist_ok=True)

    getIndividualChats("D:\\cc9e2052aae826987a63f0cd60e81369774adeb4")
    getChatGroupMessages("D:\\cc9e2052aae826987a63f0cd60e81369774adeb4")


main()