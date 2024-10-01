def writeToFile(filename, text):
    with open(filename,'w') as fileObj:
        fileObj.write(text)

def readFromFile(filename):
    with open(filename) as fileObj:
        return fileObj.read()

def appendToFile(filename,text):
    with open(filename,'a') as fileObj:
        fileObj.write("\n"+text)

writeToFile('text.txt',"hello world")
print(readFromFile('text.txt'),end='\n')
appendToFile('text.txt','hello indra')
print(readFromFile('text.txt'))
