import re
fileToRead = 'directory.txt'
fileToWrite = 'extractedEmails.txt'
delimiterInFile = [',', ';']
def validateEmail(strEmail):
    # .* Zero or more characters of any type.
    if re.match("(.*)@(.*).(.*)", strEmail):
        return True
    return False
def writeFile(listData):
    file = open(fileToWrite, 'w+')
    strData = ""
    for item in listData:
        strData = strData+item+'\n'
    file.write(strData)
listEmail = []
file = open(fileToRead, 'rb')
listLine = file.readlines()
for itemLine in listLine:
    item = str(itemLine)

    # Remove the Control M's
    item = item.replace('\\r',';')

    for delimeter in delimiterInFile:
        item = item.replace(str(delimeter),' ')
    wordList = item.split()
    for word in wordList:
        if(validateEmail(word)):

            # Remove any "Households"
            word = word.replace("Household","")
            
            word = word + str(";")
            listEmail.append(word)
if listEmail:
    uniqEmail = set(listEmail)
    print(len(uniqEmail),"emails collected!")
    writeFile(uniqEmail)
else:
    print("No email found.")
