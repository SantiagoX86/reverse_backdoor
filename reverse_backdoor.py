#!/usr/bin/env python
# SCP initial commit from separate branch
import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
kali_ip = input('What is the IP of the attacker machine? \n')
connection.connect((kali_ip, 4444))

connection.send("Eagles beat uo on the Lions!!!!".encode())

recieved_data = connection.recv(1024)
print(recieved_data)


connection.close()