import socket
from threading import Thread

# Socket config
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 8089))
serversocket.listen(5)

# Find desktop in dhcp network
def findServer():
    while True:
        connection, address = serversocket.accept()
        buf = connection.recv(4096)
        ipstr = str(address)
        indexComma = ipstr.find(",")
        ipstr = ipstr[:indexComma]
        ipstr = ipstr.replace("(", "").replace("'", "")

        if len(buf) > 0:
            if buf == b'rasp?':
                respond('rasp!', ipstr)

# Send message to server
def respond(msg, ip):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ip, 8089))
    print('Sending: ' + str(msg) + '\n')
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()

# Thread - Listen to connections & Respond
findServerThread = Thread(target=findServer)
findServerThread.start()
