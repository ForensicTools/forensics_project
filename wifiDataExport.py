import xml.etree.cElementTree as ET

def parseXML(xmlFile):

    tree = ET.parse(xmlFile)
    root = tree.getroot()



    for i in range(95):
        value = len(root[0][19][i])
        for j in range(value):
            asd = root[0][19][i][j].text

            if asd == "SSID_STR":
                value = root[0][19][i][j+1].text
                print("SSID: " + value)
            elif asd == "lastAutoJoined":
                value = root[0][19][i][j+1].text
                print("lastAutoJoined: " + value)
            elif asd == "lastJoined":
                value = root[0][19][i][j+1].text
                print("lastJoined: " + value)
        print("")



parseXML("ade0340f576ee14793c607073bd7e8e409af07a8.plist")