import mysql.connector
import dbconfig as cfg

class MemberDAO:
    db = ""
    def __init__(self):
        self.db =  mysql.connector.connect(
        host = cfg.mysql['host'],
        user = cfg.mysql['user'],
        password = cfg.mysql['password'],
        database = cfg.mysql['database']
        )
    
    def create(self, values):
        cursor = self.db.cursor()
        sql = "INSERT INTO member (name, surname, age) VALUES (%s, %s, %s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid
    
    def getAll(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM member"
        cursor.execute(sql)
        results = cursor.fetchall()

        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))

        return returnArray
    
    def findByID(self, id):
        cursor = self.db.cursor()
        sql = "SELECT * FROM member WHERE id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql = "UPDATE member SET name = %s, surname = %s, age = %s WHERE id = %s"
        cursor.execute(sql, values)

        self.db.commit()
    
    def delete(self, id):
        cursor = self.db.cursor()
        sql = "DELETE FROM member WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)

        self.db.commit()
        print("Delete done")

    def convertToDictionary(self, result):
        colnames = ['id', 'name', 'surname', 'age']
        item = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item

memberDAO = MemberDAO()



