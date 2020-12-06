import mysql.connector
import dbconfig as cfg

# Creating a class called MemberDAO
class MemberDAO:
    db = ""

    # passing mySQL server details from dbconfig.py file
    def __init__(self):
        self.db =  mysql.connector.connect(
        host = cfg.mysql['host'],
        user = cfg.mysql['user'],
        password = cfg.mysql['password'],
        database = cfg.mysql['database']
        )
    
    # function that creats a new record of a member
    def create(self, values):
        cursor = self.db.cursor()
        sql = "INSERT INTO member (name, surname, age) VALUES (%s, %s, %s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid
    
    # function that shows all members in the DB
    def getAll(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM member"
        cursor.execute(sql)
        results = cursor.fetchall()

        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))

        return returnArray
    
    # function that performs a serch by member ID
    def findByID(self, id):
        cursor = self.db.cursor()
        sql = "SELECT * FROM member WHERE id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    # function that updates member record
    def update(self, values):
        cursor = self.db.cursor()
        sql = "UPDATE member SET name = %s, surname = %s, age = %s WHERE id = %s"
        cursor.execute(sql, values)

        self.db.commit()
    
    # function to delete a record from DB
    def delete(self, id):
        cursor = self.db.cursor()
        sql = "DELETE FROM member WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)

        self.db.commit()
        print("Delete done")

    # function that converts table to dictionary
    def convertToDictionary(self, result):
        colnames = ['id', 'name', 'surname', 'age']
        item = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item

memberDAO = MemberDAO()



