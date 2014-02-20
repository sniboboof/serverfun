import sys
import socket

#mostly taken from socket documentation and cewing's walkthru

def msgsend(mess):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect( ("", 7539) )
    client.sendall(mess)
    data = client.recv(1024)
    client.close()
    return data

if __name__ == '__main__':
    if sys.argv[1]:
        print "Response: " + msgsend(str(sys.argv[1]))
