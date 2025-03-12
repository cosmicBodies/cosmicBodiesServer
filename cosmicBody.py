import pyodbc
from fakeEnv import dsn

class CosmicBodyManager():
    def __init__(self,dsn):
        self.dsn = dsn

    def createConn(self):
        conn = pyodbc.connect(dsn)
        cursor = conn.cursor()
        return conn, cursor
    
    def closeConn(self,conn,cursor):
        conn.close()
        cursor.close()

    def get(self,id:int):
        try:
            id = int(id)
        except Exception as e:
            print(e)
            return False
        
        select_script = f"SELECT ID FROM CosmicBodies WHERE ID={id}"
        conn, cursor = self.createConn()
        cursor.execute(select_script)
        cosmicBody = cursor.fetchall()
        self.closeConn(conn,cursor)
        return ", ".join(map(str, cosmicBody))

    def getAll(self):
        select_script = "SELECT * FROM CosmicBodies"
        conn,cursor = self.createConn()
        cursor.execute(select_script)
        cosmicBodies = cursor.fetchall()
        self.closeConn(conn,cursor)
        return [", ".join(map(str, row)) for row in cosmicBodies]

    def create(self, name:str,type:str,distanceToEarth:int,size:int):
        if(len(name) > 255 or len(type) > 255):
            return False
        try:
            distanceToEarth = int(distanceToEarth)
            size = int(size)
        except Exception as e:
            print(str(e))
            return False
                
        try:
            conn,cursor = self.createConn()
            inset_Query = "INSERT INTO CosmicBodies [[name],[type],[distanceToEarth],[size] VALUES (?,?,?,?)]"
            cursor.execute(inset_Query,(name,type,distanceToEarth,size))
            self.closeConn(conn,cursor)
        except Exception as e:
            print(str(e))
            self.closeConn(conn,cursor)
            return False
        
        return True

    def delete(self,id:int):
        try:
            id = int(id)
        except Exception as e:
            print(str(e))
            return False
        
        conn,cursor = self.createConn()
        delete_script = F"DELETE FROM CosmicBodies WHERE ID={id}"
        try:
            cursor.execute(delete_script)
            self.closeConn(conn,cursor)
        except Exception as e:
            print(str(e))
            self.closeConn(conn,cursor)
            return