import socket
import os
import datetime

#give it the request string
#it will parse it and return the response
def getResponse(requeststring):
    responsestring = "HTTP/1.1"
    
    requesttokens = requeststring.split('\n', 1)[0].split(None, 3)
    if requesttokens[0] == "GET" \
    and requesttokens[2][:-1] == "HTTP/1.":
        responsestring += get_request(os.getcwd()+requesttokens[1])
    else:
        responsestring += bad_request()
    
    return responsestring

def get_request(filepath):
    message = ""
    
    if os.path.exists(filepath):
        message = " 200 OK\r\n"
        if os.path.isdir(filepath):
            message += get_dir_info(filepath)
        else:
            message += get_file_info(filepath)
    else:
        message = " 404 File Not Found\r\n"
    
    return message

def get_dir_info(requesteddir):
    dircontents = os.listdir(requesteddir)
    
    payload = ""
    for singlefile in dircontents:
        if os.path.isdir(requesteddir+'/'+singlefile):
            payload += "dir: "
        else:
            payload += "file: "
        payload += singlefile + "\r\n"
        
        
    message = "Date: " + str(datetime.datetime.now()) + " GMT\r\n"
    message += "Content-Type: directory\r\n"
    message += "Content-Length: " + str(len(payload)) + "\r\n"
    message += "\r\n"
    
    message += payload + "\r\n"
    return message

def get_file_info(requestedfilepath):
    requestedfile = open(requestedfilepath, "r")
    content = requestedfile.read()
    
    message = "Date: " + str(datetime.datetime.now()) + " GMT\r\n"
    message += "Content-Type: file\r\n"
    message += "Content-Length: " + str(len(content)) + "\r\n"
    message += "\r\n"
    
    message += content + "\r\n"
    
    return message

def bad_request():
    return " 400 Bad Request\r\n"

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