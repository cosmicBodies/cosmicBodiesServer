from sharedFunctions import createConn,closeConn

class CredentialsManager():
    def __init__(self,dsn):
        self.dsn = dsn
    
    def checkCredentials(self,username,password):
        conn,cursor =  createConn(self.dsn)
        checkScript = "SELECT * FROM [Users] WHERE Password=? AND Username=?"
        cursor.execute(checkScript,(password,username))
        result = cursor.fetchone(checkScript)
        closeConn(conn,cursor)
        return ", ".join(map(str, result))  if result else False