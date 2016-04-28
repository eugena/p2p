import argparse
import socket
import sys

import stun

DEFAULT_MESSAGE = "Hello world!"
#DEFAULT_MODE = "client"

def mode_server(host, port):
    '''
    Simple udp socket server
        Silver Moon (m00n.silv3r@gmail.com)
    '''


    #HOST = ''   # Symbolic name meaning all available interfaces
    #PORT = 8888 # Arbitrary non-privileged port

    host= "0.0.0.0"
    port = 8888

    # Datagram (udp) socket
    try :
        socket.setdefaulttimeout(20)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        print 'Socket created'
    except socket.error, msg :
        print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()


    # Bind socket to local host and port
    try:
        s.bind((host, port))
    except socket.error , msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    print 'Socket bind complete'

    #now keep talking with the client
    while 1:
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        data = d[0]
        addr = d[1]

        if not data:
            break

        reply = 'OK...' + data

        s.sendto(reply , addr)
        print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()

    s.close()


def mode_client(host, port, message):
    '''
    udp socket client
    Silver Moon
    '''


    # create dgram udp socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print 'Failed to create socket'
        sys.exit()

    host= "0.0.0.0"
    port = 8888

    #while(1) :
        #msg = raw_input('Enter message to send : ')

    try :
        #Set the whole string
        s.sendto(message, (host, port))

        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        print 'Server reply : ' + reply

    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Peer-to-peer message transmission from client to server')
    parser.add_argument(
        '--mode',
        help='mode of the program (client or server, default "%s")')
    parser.add_argument(
        '--message',
        default=DEFAULT_MESSAGE,
        help='message content (default "%s")' % DEFAULT_MESSAGE)
    args = parser.parse_args()

    nat_type, host, port = stun.get_ip_info()

    if args.mode == "client":
        mode_client(host, port, args.message)
    elif args.mode == "server":
        mode_server(host, port)
    else:
        parser.print_help()

