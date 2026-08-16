import subprocess
import json
from pathlib import Path
from dataclasses import dataclass

class MCPClient:
    def __init__(self):
        self.process = None
        self.next_id = 1
        self.tools = {}


    def connect(self, command):
        self.process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            bufsize=1,
        )


    def send(self, message_dict):
        self.process.stdin.write(json.dumps(message_dict) + "\n")
        self.process.stdin.flush()


    def receive(self):
        line = self.process.stdout.readline()
        return json.loads(line)







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
        print(reply)
        self.notifications_initialized()


    def notifications_initialized(self):
        notification_msg = {
            "jsonrpc": "2.0",
            "method": "notifications/initialized",
            "params": {}
        }
        self.send(notification_msg)


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










