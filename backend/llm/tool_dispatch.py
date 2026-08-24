
from mcp.client import MCPClient
from mcp.registry import get_tools_data
import json



#thing = get_tools_data()

def dispatch(toolcall_list):
    tools_data = get_tools_data()

    return_list = []
    for x in toolcall_list:

        id = x["id"]
        name = x["function"]["name"]
        arguments = json.loads(x["function"]["arguments"])

        server = tools_data.tool_registry[name]
        client = tools_data.clients[server]

        output = client.tools_call(name=name, arguments=arguments)

        content = json.dumps(output["result"]["content"])
        return_list.append({"role": "tool", "tool_call_id": id, "content": content})

    return return_list



"""
MCP OUTPUT

{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      { "type": "text", "text": "result string here" }
    ],
    "isError": false
}

"""
"""
  {
    "role": "tool",
    "tool_call_id": "call_abc123XYZ",
    "content": "{\"temperature\": \"16°C\", \"condition\": \"Partly Cloudy\"}"
  }
"""






"""

MCP INPUT

tool_msg = {
    "jsonrpc": "2.0",
    "id": self.next_id,
    "method": "tools/call",
    "params": {
        "name": name,
        "arguments": arguments
    }
}
"""





#connect
#dispatch


"""
[
    {'id': 'call_00_8z4qkdnN475locIrqtY31700', 'type': 'function', 'function': {'name': 'echo', 'arguments': '{"text": "Echo call one"}'}}, 
    {'id': 'call_01_tZd27J6ETeaq2hpskLsP0209', 'type': 'function', 'function': {'name': 'echo', 'arguments': '{"text": "Echo call two"}'}}
]
"""



