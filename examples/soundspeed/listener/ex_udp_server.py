import socket
import time
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


HOST = "localhost"
PORT = 5454
address = (HOST, PORT)
data = "Test data ﻑ"
print(type(data))

# SOCK_DGRAM is UDP, SOCK_STREAM (default) is TCP
# AF_INET (IPv4), AF_INET6 (IPv6)
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    sz = s.sendto(data.encode('utf-8'), address)
    print('%s sent: %s [%s] to %s' % (s.getsockname(), data, sz, address))
    time.sleep(1)
