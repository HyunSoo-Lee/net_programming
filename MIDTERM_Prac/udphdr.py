import socket
import struct
import binascii

class Udphdr:
    def __init__(self, srce_port, dest_port, length, chksm):
        self.srce_port = srce_port
        self.dest_port = dest_port
        self.length = length
        self.chksm = chksm

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!H', self.srce_port)
        packed += struct.pack('!H', self.dest_port)
        packed += struct.pack('!H', self.length)
        packed += struct.pack('!H', self.chksm)
        return packed

def unpack_udp(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:10])
    return unpacked

def getSourcePort(unpacked_udpheader):
    return unpacked_udpheader[0]
    
def getDestinationPort(unpacked_udpheader):
    return unpacked_udpheader[1]
    
def getLength(unpacked_udpheader):
    return unpacked_udpheader[2]

def getChecksum(unpacked_udpheader):
    return unpacked_udpheader[3]

udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udp = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udp))
unpacked_udp = unpack_udp(packed_udp)
print(unpacked_udp)
print(f"Source Port : {getSourcePort(unpacked_udp)}")
print(f"Destination Port: {getDestinationPort(unpacked_udp)}")
print(f"Length : {getLength(unpacked_udp)}")
print(f"Checksum : {getChecksum(unpacked_udp)}")

