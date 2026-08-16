from dataclasses import dataclass
import json
from pathlib import Path

from mcp.client import MCPClient



@dataclass
class tools_data:
    clients: dict
    tool_registry: dict
    tool_list: list

    @classmethod
    def startup(cls):
        clients = {}
        tool_registry = {}
        tool_list = []

        servers = json.loads((Path(__file__).parent / "mcp_servers.json").read_text())

        for server, command in servers.items():
            client = MCPClient()
            clients[server] = client

            client.connect(command)
            client.initialize()
            tools = client.tools_list()

            tool_list.extend(tools["result"]["tools"])
            #print(tool_list)
            tool_registry.update({tool["name"]: server for tool in tools["result"]["tools"]})


        return cls(
            clients=clients,
            tool_registry=tool_registry,
            tool_list=tool_list
        )


_tools = None

def get_tools_data():
    global _tools
    if _tools is None:
        _tools = tools_data.startup()
    return _tools




if __name__ == "__main__":
    _tools = get_tools_data()

    print(_tools.tool_list)