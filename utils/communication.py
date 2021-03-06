###############################################################################
# The communication module (communication.py)
###############################################################################
try:
  import cPickle as pickle
except:
  import pickle

import socket
import struct
#import utils
#from utils import app

marshall = pickle.dumps
unmarshall = pickle.loads
flSimpleTransfer=1

def send(channel, *args):
    if flSimpleTransfer:
        buf=args[0]
    else:
        buf = marshall(args)

    value = socket.htonl(len(buf))
    size = struct.pack("L",value)
    channel.send(size)
#    app.Log(str(size))
    if len(buf):
        channel.send(buf)
#    app.Log(buf)

def receive(channel):

    size = struct.calcsize("L")
    size = channel.recv(size)
    try:
        size = socket.ntohl(struct.unpack("L", size)[0])
    except struct.error as e:
        return ''

    buf = ""

    while len(buf) < size:
        tBuf = channel.recv(size - len(buf))
        buf+=tBuf
#        print size,tBuf

    if flSimpleTransfer:
    	return buf
    else:
    	return unmarshall(buf)[0]