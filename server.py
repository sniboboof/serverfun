import socket
import os

#give it the request string
#it will parse it and return the response
def getResponse(requeststring):
    responsestring = "HTTP/1.1"
    
    requesttokens = requeststring.split('\n', 1)[0].split(None, 3)
    if requesttokens[0] == "GET" and (requesttokens[2] == "HTTP/1.1" or requesttokens[2] == "HTTP/1.0"):
        responsestring += get_request(requesttokens[1])
    else:
        responsestring += bad_request()
    
    responsestring += "\r\n"
    return responsestring

def get_request(filepath):
    message = ""
    
    if os.path.exists(os.getcwd()+filepath):
        if os.path.isdir(os.getcwd()+filepath):
            message = get_dir_info(os.open(os.getcwd()+filepath))
        else:
            message = get_file_info(os.open(os.getcwd()+filepath))
    else:
        message = " 404 File Not Found"
    
    return message

def get_dir_info(requesteddir):
    return ""

def get_file_info(requestedfile):
    return ""

def bad_request():
    return " 400 Bad Request"

def simple_server_loop(portnum=17745):
    httpserv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    httpserv.bind(("", portnum))
    httpserv.listen(1)
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