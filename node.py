import socket

class Node:

    def __init__(self, address, port):
        self.address = address
        self.port = port

    def ping(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.address, self.port))
                s.sendall(b'{"jsonrpc": "2.0", "method": "server.version", "params": ["", "1.4"], "id": 0}\n')
                data = s.recv(1028)
        except Exception as e:
            return False

        return True

    def get_utxos(self, scripthash: str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.address, self.port))
            method = '{"jsonrpc": "2.0", "method": "blockchain.scripthash.listunspent", "params": ["' + str(scripthash) + '"], "id": 0}\n';
            s.sendall(method.encode())
            data = s.recv(1028)
            return data
