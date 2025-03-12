from sharedFunctions import createConn,closeConn


class CosmicBodyManager():
    def __init__(self,dsn):
        self.dsn = dsn

    def get(self,id:int):
        try:
            id = int(id)
        except Exception as e:
            print(e)
            return False
        
        select_script = f"SELECT * FROM CosmicBodies WHERE ID=?"
        conn, cursor = createConn(self.dsn)
        cursor.execute(select_script,(id))
        cosmicBody = cursor.fetchone()
        closeConn(conn,cursor)
        return ", ".join(map(str, cosmicBody))

    def getAll(self):
        select_script = "SELECT * FROM CosmicBodies"
        conn,cursor = createConn(self.dsn)
        cursor.execute(select_script)
        cosmicBodies = cursor.fetchall()
        closeConn(conn,cursor)
        return [", ".join(map(str, row)) for row in cosmicBodies]

    def create(self, name:str,type:str,distanceToEarth:int,size:int,YearOfDiscovery:str):
        if(len(name) > 255 or len(type) > 255):
            return False
        try:
            distanceToEarth = int(distanceToEarth)
            size = int(size)
        except Exception as e:
            print(str(e))
            return False
                
        try:
            conn,cursor = createConn(self.dsn)
            inset_Query = "INSERT INTO CosmicBodies [[name],[type],[distanceToEarth],[size],[YearOfDiscovery] VALUES (?,?,?,?)]"
            cursor.execute(inset_Query,(name,type,distanceToEarth,size,YearOfDiscovery))
            closeConn(conn,cursor)
        except Exception as e:
            print(str(e))
            closeConn(conn,cursor)
            return False
        
        return True

    def delete(self,id:int):
        try:
            id = int(id)
        except Exception as e:
            print(str(e))
            return False
        
        conn,cursor = createConn(self.dsn)
        delete_script = F"DELETE FROM CosmicBodies WHERE ID={id}"
        try:
            cursor.execute(delete_script)
            closeConn(conn,cursor)
        except Exception as e:
            print(str(e))
            closeConn(conn,cursor)
            return