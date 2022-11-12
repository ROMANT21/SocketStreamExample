import cv2
import io
import socket
import struct
import time
import pickle
import zlib
import imutils

HOST = "127.0.0.1"      # Localhost IP
PORT = 65432            # Client port

# Create the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_address = (HOST, PORT)
print("HOST IP: ", HOST)

# Bind the socket to the port
server_socket.bind(socket_address)

# Let server listen for other connections
server_socket.listen(5)
print("LISTENING...")

# Accept incoming server requests from client
while True:
    client_socket, addr = server_socket.accept()

    # Send camera frames to client
    if client_socket:
        cam = cv2.VideoCapture(0)       # Create camera object

        while (cam.isOpened()):
            # Read frame and resize frame from camera
            img, frame = cam.read()    
            frame = imutils.resize(frame, width=320)
            
            # Serialize the frame (turn it into series of bits)
            a = pickle.dumps(frame)

            # Create message and append size of byte stream to message     
            message = struct.pack("Q", len(a)) + a

            # Send frame to client
            try:
                client_socket.sendall(message)
            except Exception as e:
                print(e)
                raise Exception(e)
            
            # Shows video stream on server side
            cv2.imshow('TRANSMITTING VIDEO', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()