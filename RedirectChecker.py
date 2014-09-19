import win32com.client
from time import sleep
import csv

def openUrl(url):
    autoit.Send("^l")
    autoit.Send(url)
    autoit.Send("{Enter}")
    print 'Opened ' + url

    sleep(5.0)
    
def checkCurrentUrlAgainst(source, url):
    autoit.Send("^l")
    sleep(0.2)
    autoit.Send("^c")
    sleep(0.2)
    foundUrl = autoit.ClipGet()
    if url.strip() == foundUrl.strip():
        passed.write("Source " + source + " : " + foundUrl + " and " + url + " match.\n\n")
        print("Passed. " + str(passCnt + 1) + " passed total, " + str(len(table1)-passCnt-failCnt) + " URLS remaining.")
        return 0
    else:
        failed.write("Source " + source + " : Expected URL: " + url + " but was: " + foundUrl + "\n\n")
        print("Failed! " + str(failCnt + 1) + " failed total, " + str(len(table1)-passCnt-failCnt) + " URLS remaining.")
        return 1
def loadTable(fileLocation):
    f = open(fileLocation, 'rU')
    index = 0;
    try:
        reader = csv.reader(f)
        for rows in reader:
            table1.append(rows[0])
            table2.append(rows[1])
            
            if amount != -1: # -1 means read all files
                if index < amount-1:
                    index = index +1
                else:
                    return
        
    finally:
        f.close()
        
    
table1 = []
table2 = []

fileName = raw_input('CSV file (include location): ')
amount = int(input("How many redirects to test? (-1 for all): "))

if '.csv' in fileName:
    fileName = fileName.replace(".csv", "")

loadTable(fileName + ".csv")

passed = open(fileName + "_passed.txt", "w")
failed = open(fileName + "_failed.txt", "w")
passCnt = 0
failCnt = 0

autoit = win32com.client.Dispatch("AutoItX3.Control")
autoit.AutoItSetOption("WinTitleMatchMode", 2);

#webbrowser.open_new_tab('http://www.google.com')
autoit.WinActivate("Mozilla Firefox")

sleep(5.0)
n = 400
while n in range(len(table1)):
    openUrl(table1[n])
    passOrFail = checkCurrentUrlAgainst(table1[n],table2[n])
    if passOrFail == 0:
        passCnt = passCnt +1
    else:
        failCnt = failCnt +1
    sleep(3.0)
    
passed.close()
failed.close()
print "Testing completed. " + str(passCnt) + " passed and " + str(failCnt) + " failed. Please see output files."
input("Press enter to terminate.")