import sqlite3

class DBSqlite(object):
    con = None
    db_file = ''
    def __init__(self, filename):
        self.db_file = filename
        self.con = sqlite3.connect(filename)
    
    def updateData(self, sql):
        cur = self.con.cursor()
        cur.execute(sql)
        self.con.commit()
    
    def getData(self, sql):
        cur = self.con.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        return rows

    def getDB(self):
        return self.con

    def closeDB(self):
        self.con.close()
