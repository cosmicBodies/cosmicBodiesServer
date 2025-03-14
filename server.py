import socket
import json

from fakeEnv import host,port,dsn
from cosmicBody import CosmicBodyManager
from credentialsManager import CredentialsManager

class Server():
    def __init__(self):
        self._bodyManager = CosmicBodyManager(dsn)
        self._server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self._server_socket.bind((host,port))
        self._credentialsManager = CredentialsManager(dsn)
        self._server_socket.listen(1)
        print('Waiting for connection')
        self.client_socket, self.client_address = self._server_socket.accept()
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
                cosmicBodies = self._bodyManager.getAll()
                self._sendData(cosmicBodies,"all cosmic Bodies")
            if(action == "1"):
                cosmicBody = self._bodyManager.get(parsedJson["data"]["id"])
                self._sendData(cosmicBody,"Body")
            if(action == "2" and self._credentialsManager.checkCredentials(**parsedJson["credentials"])):
                isCreated = self._bodyManager.create(**parsedJson["data"])
                self._sendData(isCreated,"Created")
            if(action == "3" and self._credentialsManager.checkCredentials(**parsedJson["credentials"])):
                isDeleted = self._bodyManager.delete(parsedJson["data"]["id"])
                self._sendData(isDeleted,"Deleted")
            if(action == "4"):
                self.client_socket.close()
                self._server_socket.close()
                break
        
outPut = {"message":"message","data":"data"}

serverInput = {
    "credentials": {
        "username": "Petro",
        "password": "Poroshenko"
    },
    "data": {
        ...
    },
    "action": "1-4"
}

server = Server()
server.runServer()

