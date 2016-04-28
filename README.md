Simple utility for peer-to-peer message transmission from client to server.

# Installation
    git clone https://github.com/eugena/p2p.git
    pip install -r requirements.txt

# Usage help
    python p2p.py -h
    usage: p2p.py [-h] [--mode MODE] [--message MESSAGE]
    
    Peer-to-peer message transmission from client to server
    
    optional arguments:
      -h, --help         show this help message and exit
      --mode MODE        mode of the program ("client" or "server")
      --message MESSAGE  message content (default "Hello world!")
