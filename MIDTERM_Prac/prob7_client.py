import socket
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

def unpack_data(buffer):
    unpacked = struct.unpack('!HHBBBBL', buffer[:12])
    return unpacked

port = 9999
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = 'send data to client using packing'
sock.sendto(msg.encode(), ('localhost', port))
data, addr = sock.recvfrom(BUFFSIZE)
#print(data)
sock.close()

unpacked_data = unpack_data(data)
#print(unpacked_data)
print(f'Sender:{unpacked_data[0]}, Receiver:{unpacked_data[1]}, Lumi:{unpacked_data[2]}, Humi:{unpacked_data[3]}, Temp:{unpacked_data[4]}, Air:{unpacked_data[5]}, Seq:{unpacked_data[6]}')