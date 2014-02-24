import socket
import os

#give it the request string
#it will parse it and return the response
def getResponse(requeststring):
    responsestring = "HTTP/1.1"
    
    requesttokens = requeststring.split('\n', 1)[0].split(None, 3)
    
    if requesttokens[0] is "GET" \
    and (requesttokens[2] is "HTTP/1.1" or requesttokens[2] is "HTTP/1.0"):
        responsestring += get_request(requesttokens[1])
    else:
        responsestring += bad_request()
    
    responsestring += "\r\n"
    return responsestring

def get_request(filepath):
    message = ""
    return message

def bad_request():
    return " 400 Bad Request"

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