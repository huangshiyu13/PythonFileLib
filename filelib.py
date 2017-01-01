import os

def getAllFiles(dirName, houzhui=' '):
    results = []

    for file in os.listdir(dirName):
        file_path = os.path.join(dirName, file)
        if houzhui == ' ':
            if os.path.isfile(file_path):
                results.append([file_path, os.path.splitext(file)[0]])
        else:
            if os.path.isfile(file_path) and os.path.splitext(file_path)[1] == houzhui:
                results.append([file_path,os.path.splitext(file)[0]])
    return results


def checkFile(fileName):
    if os.path.isfile(fileName):
        return True
    else:
        print fileName, 'is not found!'
        exit()


def checkDir(fileName, creat=False):
    if os.path.isdir(fileName):
        if creat:
            shutil.rmtree(fileName)
            os.mkdir(fileName)
    else:
        if creat:
            os.mkdir(fileName)
        else:
            print fileName, 'is not found!'
            exit()


if __name__ == '__main__':
    checkFile('filelib.py')
    checkDir('./.git')
    print getAllFiles('./')