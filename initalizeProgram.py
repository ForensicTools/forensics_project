import os
import pathlib
from shutil import copyfile

def initalizeProgram(path):
    path = os.path.dirname(path)
    mainPath = path + "\\iBackupData"
    pathlib.Path(path + "\\iBackupData").mkdir(parents=True, exist_ok=True)
    pathlib.Path(mainPath + "\\SMS").mkdir(parents=True, exist_ok=True)
    pathlib.Path(mainPath + "\\SMS\\Texts").mkdir(parents=True, exist_ok=True)
    pathlib.Path(mainPath + "\\SMS\\Attachments").mkdir(parents=True, exist_ok=True)
    pathlib.Path(mainPath + "\\Calls").mkdir(parents=True, exist_ok=True)
    pathlib.Path(mainPath + "\\Web History").mkdir(parents=True, exist_ok=True)
    pathlib.Path(mainPath + "\\Calender").mkdir(parents=True, exist_ok=True)
    pathlib.Path(mainPath + "\\Contacts").mkdir(parents=True, exist_ok=True)
    pathlib.Path(mainPath + "\\Notes").mkdir(parents=True, exist_ok=True)
    pathlib.Path(mainPath + "\\Photo Data").mkdir(parents=True, exist_ok=True)
    pathlib.Path(mainPath + "\\DBFiles").mkdir(parents=True, exist_ok=True)


def copyFiles(path):

    files = ["3d0d7e5fb2ce288813306e4d4636395e047a3d28", "12b144c0bd44f2b3dffd9186d3f9c05b917cee25",
             "2041457d5fe04d39d0ab481178355df6781e6858", "e74113c185fd8297e140cfcf9c99436c5cc06b57",
             "31bb7ba8914766d4ba40d6dfb6113c8b614be442", "ca3bc056d4da0bbf88b5fb3be254f3b7147e639c",
             "5a4935c78a5255723f707230a451d79c540d2741", "4f98687d8ab0d6d1a371110e6b7300f6e465bef2"]


    extension = ".db"

    for file in files:
        filePath = path + "\\" + file[0:2] + "\\" + file
        destination = os.path.dirname(path) + "\\iBackupData\\DBFiles\\" + file
        copyfile(filePath, destination + extension)



def initProgram(path):
    initalizeProgram(path)
    copyFiles(path)


if __name__ == '__initProgram__':
    main("D:\cc9e2052aae826987a63f0cd60e81369774adeb4")
