from chatroom import ServerTCP

if __name__ == "__main__":
    server = ServerTCP(12345)
    server.run()
