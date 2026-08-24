from dataclasses import dataclass
import json
from pathlib import Path

from mcp.client import MCPClient



@dataclass
class tools_data:
    clients: dict # all the objects connected to each mcp client
    tool_registry: dict # all tools and which server they belong too
    tool_list: list # list of all tools with descriptions and requirements/params

    @classmethod
    def startup(cls):
        clients = {}
        tool_registry = {}
        tool_list = []

        servers = json.loads((Path(__file__).parent / "mcp_servers.json").read_text()) # all the mcp servers , prolly gonna make a more dynamic thing in the future 

        for server, command in servers.items():
            client = MCPClient() # creates an object for each mcp server
            clients[server] = client

            
            client.connect(command)
            client.initialize()
            tools = client.tools_list()

            tool_list.extend(tools["result"]["tools"])

            tool_registry.update({tool["name"]: server for tool in tools["result"]["tools"]})


        return cls(
            clients=clients,    #all the objects connected to each mcp client
            tool_registry=tool_registry, # all tools and which server they belong too
            tool_list=tool_list # list of all tools with descriptions and requirements/params
        )


tools = None

#easily importable function with the tools_data (clients, tool_registry and tool_list)
def get_tools_data():
    global tools
    if tools is None:
        tools = tools_data.startup()
    return tools




if __name__ == "__main__":
    tools = get_tools_data()

    print(tools.tool_list)