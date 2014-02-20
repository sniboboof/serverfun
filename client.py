import sys
import socket

#mostly taken from socket documentation and cewing's walkthru

def msgsend(mess, portnum=17745):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect( ("", portnum) )
    client.sendall(mess)
    client.shutdown(socket.SHUT_WR)
    data = ""
    mybuff = client.recv(1024)
    while mybuff:
        data += mybuff
        mybuff = client.recv(1024)
    client.close()
    return data

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        msg = sys.argv[1]
    else:
        msg = input("input request:\n")
    print "Response:\n" + msgsend(msg)
