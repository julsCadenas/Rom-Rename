import os

directoryPath = 'C:/Users/Juls/Desktop/rename test'
fileList = os.listdir(directoryPath)

os.chdir(directoryPath)

for file in fileList:
    splitFile=file.split(" ",1)
    newName=f"{splitFile[1]}"
    print(newName)
    os.rename(file,newName)