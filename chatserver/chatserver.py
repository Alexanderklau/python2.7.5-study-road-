from asyncore import dispatcher
import socket,asyncore
class ChatServer(dispatcher):
    def handle_accept(self):
        coon,addr = self.accept()
        print 'Connection attemot from',addr[0]

s = ChatServer()
s.create_socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',5005))
s.listen(5)
asyncore.loop()
