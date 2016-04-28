from twisted.internet.protocol import DatagramProtocol


class Client(DatagramProtocol):
    """
    Sender
    """
    host = None
    port = None
    message = None

    def __init__(self, host, port, message):
        self.host = host
        self.port = port
        self.message = message

    def startProtocol(self):
        self.transport.connect(self.host, self.port)
        self.sendDatagram()

    def sendDatagram(self):
        self.transport.write(self.message)
