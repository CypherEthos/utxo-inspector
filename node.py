import socket
import socks
import config

class Node:

    def ping(self):
        try:
            if (config.TOR_PROXY_ADDRESS):
                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, config.TOR_PROXY_ADDRESS, config.TOR_PROXY_PORT, True)
                socket.socket = socks.socksocket

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((config.SERVER_ADDRESS, config.SERVER_PORT))
                s.sendall(b'{"jsonrpc": "2.0", "method": "server.version", "params": ["", "1.4"], "id": 0}\n')
                data = s.recv(1028)
        except Exception as e:
            return False

        return True

    def get_utxos(self, scripthash: str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((config.SERVER_ADDRESS, config.SERVER_PORT))
            method = '{"jsonrpc": "2.0", "method": "blockchain.scripthash.listunspent", "params": ["' + str(scripthash) + '"], "id": 0}\n';
            s.sendall(method.encode())
            data = s.recv(1028)
            return data
