import socket
import cv2
import pickle
import numpy as np
import struct ## new

HOST = "127.0.0.1"    # localhost IP
PORT = 65432          # The port used by server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

data = b""                              # Create a byte string
payload_size = struct.calcsize("Q")     # Q is a long integer, size 8 bytes

# Reconstruct frame
while True:

    # Receive packet of data from server and append to data variable
    while (len(data) < payload_size):             
        packet = client_socket.recv(4 * 1024)   # 4K, range(1024 byte to 64KB)  
        if not packet: break
        data += packet
    
    # Find size of frame (i.e. the size of the frame)
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]                          
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    # Recover frame byte stream
    while len(data) < msg_size:
        data += client_socket.recv(4 * 1024)
    frame_data = data[:msg_size]        # Recover actual frame data
    data = data[msg_size:]
    frame = pickle.loads(frame_data)    
    
    # Display frames
    cv2.imshow("RECEIVING VIDEO", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
