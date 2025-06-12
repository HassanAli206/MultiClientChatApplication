from chatroom import ServerUDP

if __name__ == "__main__":
    server = ServerUDP(12345)
    server.run()
