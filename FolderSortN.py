import os
import re
import tkinter
from tkinter import filedialog
from tkinter import simpledialog
from pathlib import Path

def fileMake(matrixPos, matrix, dirPath, foldPaths):
    os.rename(foldPaths[matrixPos[0]], dirPath / matrix[matrixPos[0]][matrixPos[1]])
    if(matrixPos[0] < len(matrix) - 1):
        folderMake([matrixPos[0] + 1, 0], matrix, dirPath.parents[matrixPos[1] - 1], foldPaths)
    return
def folderMake(matrixPos, matrix, dirPath, foldPaths):
    if(matrixPos[1] >= len(matrix[matrixPos[0]]) - 1):
        fileMake(matrixPos, matrix, dirPath, foldPaths)
        return
    elif((dirPath / matrix[matrixPos[0]][matrixPos[1]]).is_dir()):
        folderMake([matrixPos[0], matrixPos[1] + 1], matrix, dirPath / matrix[matrixPos[0]][matrixPos[1]], foldPaths)
        return
    else:
        os.mkdir(dirPath / matrix[matrixPos[0]][matrixPos[1]])
        folderMake([matrixPos[0], matrixPos[1] + 1], matrix, dirPath / matrix[matrixPos[0]][matrixPos[1]], foldPaths)
        return

def main():
    tkinter.Tk().withdraw()
    dirPath = Path(filedialog.askdirectory(title = 'Select directory to sort...'))
    fileSplit = "--"
    splitWithWhiteSpace = " " + fileSplit + " ", " " + fileSplit, fileSplit + " ", fileSplit
    delimiters= '|'.join(map(re.escape, splitWithWhiteSpace))
    #List all files that aren't folders
    dirList = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
    if(not dirList):
        print("No files in directory. Enter a different path value: ")
        return
    #Now, for each file in the list, split it into folder name and file name.\
    dirList.sort()
    fileList = []
    pathList = []
    for dirFile in dirList:
        fileObj = (re.split(delimiters, dirFile))
        if(len(fileObj) == 1):
            continue
        else:
            fileList.append(fileObj)
            pathList.append(dirPath / dirFile)
    folderMake([0,0], fileList, dirPath, pathList)
if(__name__ == "__main__"):
    main()