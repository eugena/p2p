from twisted.internet.protocol import DatagramProtocol


class Server(DatagramProtocol):
    """
    Receiver
    """
    def datagramReceived(self, data, (host, port)):
        print "received %r from %s:%d" % (data, host, port)
        self.transport.write(data, (host, port))
