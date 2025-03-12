import socket
import json

from fakeEnv import host,port,dsn
from cosmicBody import CosmicBodyManager

class Server():
    def __init__(self):
        self.bodyManager = CosmicBodyManager(dsn)
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind((host,port))
        self.server_socket.listen(1)
        print('Waiting for connection')
        self.client_socket, self.client_address = self.server_socket.accept()
        print("User accepted")
    
    def _recvData(self):
        parsedJson = json.loads(self.client_socket.recv(1024).decode())
        return parsedJson
    
    def _sendData(self,data,message):
        self.client_socket.send(json.dumps({"message":message,"data":data}).encode())
        return True
    
    def runServer(self):
        while(True):
            parsedJson = self._recvData()
            
            action = parsedJson["action"]
            if(action == "0"):
                cosmicBodies = self.bodyManager.getAll()
                return self._sendData(cosmicBodies,"all cosmic Bodies")
            if(action == "1"):
                cosmicBody = self.bodyManager.get(parsedJson["data"]["id"])
                return self._sendData(cosmicBody,"Body")
            if(action == "2" and parsedJson["credentials"] == "....."):
                isCreated = self.bodyManager.create(**parsedJson["data"])
                return self._sendData(isCreated,"Created")
            if(action == "3" and parsedJson["credentials" == "....."]):
                isDeleted = self.bodyManager.delete(parsedJson["data"]["id"])
                return self._sendData(isDeleted,"Deleted")