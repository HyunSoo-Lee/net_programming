import socket
import random
import struct
import binascii

class data:
    def __init__(self, sendId, recvId, lumi, humi, temp, air, seq):
        self.sendId = sendId
        self.recvId = recvId
        self.lumi = lumi
        self.humi = humi
        self.temp = temp
        self.air = air
        self.seq = seq

    def pack_data(self):
        packed = b''
        packed += struct.pack('!H', self.sendId)
        packed += struct.pack('!H', self.recvId)
        packed += struct.pack('!4B', self.lumi, self.humi, self.temp, self.air)
        packed += struct.pack('!L', self.seq)
        return packed

sender = random.randint(1,50000)
recver = random.randint(1,50000)
lumi = random.randint(1,100)
humi = random.randint(1,100)
temp = random.randint(1,100)
air = random.randint(1,100)
seq = random.randint(1,100000)

print(f'Sender:{sender}, Receiver:{recver}, Lumi:{lumi}, Humi{humi}, Temp:{temp}, Air:{air}, Seq:{seq}')
data = data(sender, recver, lumi, humi, temp, air, seq)
packed_data = data.pack_data()
# print(type(packed_data))
# print(packed_data)

port = 9999
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

msg, addr = sock.recvfrom(BUFFSIZE)
sock.sendto(packed_data, addr)