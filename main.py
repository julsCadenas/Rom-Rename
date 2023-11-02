import os

filename='insert one file name'
directoryPath = 'insert your file directory here'
fileList = os.listdir(directoryPath)

os.chdir(directoryPath)

for file in fileList:
    splitFile=file.split(" ",1)
    newName=f"{splitFile[1]}"
    print(newName)
    os.rename(file,newName)