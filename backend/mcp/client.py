import subprocess
import json
from pathlib import Path
from dataclasses import dataclass

"""
all the stuff needed to call, connect, initialize mcp servers
"""





# class with the stuff needed for each mcp client
class MCPClient:
    def __init__(self):
        self.process = None
        self.next_id = 1
        self.tools = {}

    # connects to the mcp server and saves the connection to the client
    def connect(self, command):
        self.process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            bufsize=1,
        )

    # function to send to the mcp server
    def send(self, message_dict):
        self.process.stdin.write(json.dumps(message_dict) + "\n")
        self.process.stdin.flush()


    def receive(self):
        line = self.process.stdout.readline()
        return json.loads(line)






    # initializes the server connection
    def initialize(self):
        current_id = self.next_id
        self.next_id += 1
        initialize_msg = {
            "jsonrpc": "2.0",
            "id": current_id,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "jarvis",
                    "version": "0.1"
                }
            }
        }
        self.send(initialize_msg)
        reply = self.receive()
        print("67",reply)
        self.notifications_initialized()


    # tells the server the intialization was sucessful
    def notifications_initialized(self):
        notification_msg = {
            "jsonrpc": "2.0",
            "method": "notifications/initialized",
            "params": {}
        }
        self.send(notification_msg)


    # ask the server for a list of its tools
    def tools_list(self):
        tools_msg = {
            "jsonrpc": "2.0",
            "id": self.next_id,
            "method": "tools/list",
            "params": {}
        }
        self.next_id += 1
        self.send(tools_msg)
        reply = self.receive()
        return reply


    # calls a tool from the server
    def tools_call(self, name, arguments):
        tool_msg = {
            "jsonrpc": "2.0",
            "id": self.next_id,
            "method": "tools/call",
            "params": {
                "name": name,
                "arguments": arguments
            }
        }
        self.next_id += 1
        self.send(tool_msg)
        reply = self.receive()
        return reply










