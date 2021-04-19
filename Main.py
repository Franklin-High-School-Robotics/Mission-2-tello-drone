# Taken and adapter from https://github.com/dbaldwin/DroneBlocks-Tello-Python/blob/master/lesson4-box-mission/TelloBoxMission.ipynb
# This example script demonstrates how use Python to fly Tello in a box mission
# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Import the necessary modules
import socket
import threading
import time
import numpy as np
import sys
import matplotlib.pyplot as plt
import scipy as sp
import Code.waypoint_class


# EDIT HERE
def main_function(waypoints, sock):
    send('command', 3)
    send('takeoff', 5)
    send('left 100', 10 )
    send('cameraon', 3)
    send('cw 360', 5)
    send('cameraoff', 3)
    send('forward 50', 5)
    smed('flip f',5)
    send('flip b',5)
    send('back 50', 5)
    send('right 100', 10)
#     Circle()
    send('right 200', 15)
    send('curve 200 200 0 0 400 0', 10)
    send('ccw 180')
    send('curve 200 200 0 0 400 0', 10)
    semd('land', 5)


    return
def Circle():
    send('right 200', 15)
    for x in range(0,11):
        send('ccw 36', 4)
        send('forward 124', 10)
    send('left 200', 15)

##############################################
# DO NOT EDIT ANYTHING BELOW HERE
##############################################


def ex_main_function(waypoints, sock):

    ##################
    # DRAW plot first
    ##################
    plt.figure()
    plt.plot([0, 0, 100, 100, 0], [0, 100, 100, 0, 0, 0], '*-')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    ####################
    # Now run drone code
    ####################

    # Each leg of the box will be 100 cm. Tello uses cm units by default.
    box_leg_distance = 100

    # Yaw 90 degrees
    yaw_angle = 90

    # Yaw clockwise (right)
    #yaw_direction = "cw"

    # Put Tello into command mode
    send("command", 3)

    # Send the takeoff command
    send("takeoff", 5)

    # Fly forward
    send("forward " + str(box_leg_distance), 4)

    # Yaw right
    send("cw " + str(yaw_angle), 3)

    # Fly forward
    send("forward " + str(box_leg_distance), 4)

    # Yaw right
    send("cw " + str(yaw_angle), 3)

    # Fly forward
    send("forward " + str(box_leg_distance), 4)

    # Yaw right
    send("cw " + str(yaw_angle), 3)

    # Fly forward
    send("forward " + str(box_leg_distance), 4)

    # Yaw right
    send("cw " + str(yaw_angle), 3)

    # Land
    send("land", 5)

    # Print message
    print("Mission completed successfully!")

    return


# IP and port of Tello
tello_address = ('192.168.10.1', 8889)

# IP and port of local computer
local_address = ('', 9000)

# Create a UDP connection that we'll send the command to
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the local address and port
sock.bind(local_address)

# Send the message to Tello and allow for a delay in seconds


def send(message, delay):
    # Try to send the message otherwise print the exception
    try:
        sock.sendto(message.encode(), tello_address)
        print("Sending message: " + message)
    except Exception as e:
        print("Error sending: " + str(e))

    # Delay for a user-defined period of time
    time.sleep(delay)

# Receive the message from Tello


def receive():
    # Continuously loop and listen for incoming messages
    while True:
        # Try to receive the message otherwise print the exception
        try:
            response, ip_address = sock.recvfrom(128)
            print("Received message: " + response.decode(encoding='utf-8'))
        except Exception as e:
            # If there's an error close the socket and break out of the loop
            sock.close()
            print("Error receiving: " + str(e))
            break


if __name__ == "main":

    # Create and start a listening thread that runs in the background
    # This utilizes our receive functions and will continuously monitor for incoming messages
    receiveThread = threading.Thread(target=receive)
    receiveThread.daemon = True
    receiveThread.start()

    waypoints = []  # This will contain an array of Waypoint class objects

    # Execute the actual algorithm
    #ex_main_function(waypoints, sock)
    main_function(waypoints, sock)

    # Close the socket
    sock.close()
