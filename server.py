import socket

#give it the request string
#it will parse it and return the response
def getResponse(request_string):
    return "but why"

def simple_server_loop(portnum=17745):
    httpserv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", portnum))
    server.listen(1)
    while True:
        conn, addr = httpserv.accept()
        
        data = ""
        mybuff = conn.recv(1024)
        while mybuff:
            data += mybuff
            mybuff = conn.recv(1024)
        
        conn.sendall(getResponse(data))
        conn.shutdown(socket.SHUT_WR)
        
        conn.close()
    httpserv.close()

if __name__ == "__main__":
    simple_server_loop()