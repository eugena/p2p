import argparse
import sys

import stun

from twisted.internet import reactor

from client import Client
from server import Server

DEFAULT_MESSAGE = "Hello world!"
CLIENT = "client"
SERVER = 'server'


def make_argument_parser():
    """
    Makes arguments
    """
    parser = argparse.ArgumentParser(
        description='Peer-to-peer message transmission from client to server')
    parser.add_argument(
        '--mode',
        help='mode of the program (client or server, default "%s")')
    parser.add_argument(
        '--message',
        default=DEFAULT_MESSAGE,
        help='message content (default "%s")' % DEFAULT_MESSAGE)
    return parser


def main():
    try:
        parser = make_argument_parser()
        args = parser.parse_args()
        if args.mode == CLIENT:
            nat_type, host, port = stun.get_ip_info()
            reactor.listenUDP(0, Client(host, port, args.message))
            reactor.run()
        elif args.mode == SERVER:
            reactor.listenUDP(0, Server())
            reactor.run()
        else:
            parser.print_help()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
