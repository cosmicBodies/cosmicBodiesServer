import pyodbc

def createConn(dsn):
    conn = pyodbc.connect(dsn)
    cursor = conn.cursor()
    return conn, cursor
    
def closeConn(conn,cursor):
    cursor.close()
    conn.close()
