import gevent
import gevent.socket
from gevent import select


class ChatClient(object):

    def __init__(self, host, port, pipe_in, pipe_out):
        try:
            self.socket = gevent.socket.create_connection((host, port))
        except IOError:
            print "Server not ready:", host, port
            exit(2)
        self.pipe_out = pipe_out
        self.pipe_in = pipe_in
        self.dispatcher = {self.pipe_in: self.write_connection, self.socket: self.listen_connection}
        gevent.joinall([gevent.spawn(self.scheduler)])

    def listen_connection(self, zzz):
        try:
            self.pipe_out.write(self.socket.recv(1024))
            self.pipe_out.flush()
        except IOError as e:
            print e
            raise gevent.GreenletExit

    def write_connection(self, a_pipe):
        line = a_pipe.readline()
        try:
            self.socket.sendall(line)
        except IOError as e:
            print e
            raise gevent.GreenletExit

    def scheduler(self):
        while True:
            to_read, to_write, to_err = select.select(self.dispatcher.keys(), [], [], 1)
            for an_input in to_read:
                self.dispatcher[an_input](an_input)

