import os
import mysql.connector



def main(path):
    foldersInPath = os.listdir(path)
    rows = []
    for folder in foldersInPath:
        getFilesPath = os.path.join(path, folder)
        filesInFolder = os.listdir(getFilesPath)
        for img in filesInFolder:
            pathToImage = os.path.join(getFilesPath, img) #Full Path to Each Image
            filename = os.path.basename(pathToImage)
            if saveInDatabase(filename, folder) == -1:
                print(f"DB Insert SUCCESS for {pathToImage}")
            else:
                print(f"DB Insert FAILURE for {pathToImage}")

def saveInDatabase(path, folder):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            database="batik"
        )
        mycursor = mydb.cursor()
        onSale = True if folder == "onSale" else False
        sql = "INSERT INTO images (path, onSale) VALUES (%s, %s)"
        val = (path, onSale)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return mycursor.rowcount
    except Exception as e:
        print(f"An Error {e} occurred!")


if __name__ == "__main__":
    main("C:\\Personal\\Laravel\\Projects\\BatikProject\\src\\public\\images")