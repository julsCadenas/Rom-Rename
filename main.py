import os

directoryPath = 'insert folder directory here'
fileList = os.listdir(directoryPath)

os.chdir(directoryPath)

for file in fileList:
    splitFile=file.split(" ",1)
    newName=f"{splitFile[1]}"
    print(newName)
    os.rename(file,newName)