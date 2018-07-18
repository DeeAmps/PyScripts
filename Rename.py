import os
import shutil

def readFiles(path, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    files = os.listdir(path)
    for fil in files:
        fullpath = os.path.join(path, str(fil))
        filename, extension = os.path.splitext(fullpath)
        newfilename = str(files.index(fil) + 1)
        newPath = f"{destination}\{newfilename}{extension}"
        shutil.move(fullpath, newPath)
        print(f"File Moved. New Path {newPath}")


if __name__ == "__main__":
    readFiles('C:\\Users\\danye\\Downloads\\batik', 'C:\\Users\\danye\\Downloads\\new_batik')