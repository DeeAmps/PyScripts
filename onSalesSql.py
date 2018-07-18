import os
import mysql.connector



def main(path):
    foldersInPath = os.listdir(path)
    rows = []
    for folder in foldersInPath:
        if folder == "onSale":
            getFilesPath = os.path.join(path, folder)
            filesInFolder = os.listdir(getFilesPath)
            for img in filesInFolder:
                pathToImage = os.path.join(getFilesPath, img) #Full Path to Each Image
                filename = os.path.basename(pathToImage)
                if saveInDatabase(filename) == -1:
                    print(f"DB Insert SUCCESS for {pathToImage}")
                else:
                    print(f"DB Insert FAILURE for {pathToImage}")

def saveInDatabase(filename):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="",
            database="batik"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO on_sales (path, name, price) VALUES (%s, %s, %s)"
        val = (filename, "Fabric", 35.00)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return mycursor.rowcount
    except Exception as e:
        print(f"An Error {e} occurred!")


if __name__ == "__main__":
    main("C:\\Personal\\Laravel\\Projects\\BatikProject\\src\\public\\images")