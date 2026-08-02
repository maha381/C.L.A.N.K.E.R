from .tools.get_weather import get_weather
from .tools.get_location_info import get_location_info
import json

#something to automatically add new tools from tools.json to tools


tools = {
    "get_weather": get_weather,
    "get_location_info": get_location_info
}


def toolcall(toolCalls):
    for x in toolCalls.keys():
        tool = toolCalls[x]
        print(tool)

        
        tool["function"]["arguments"] = json.loads(tool["function"]["arguments"])

        args = []
        for argKey, argVal in tool["function"]["arguments"].items():
            args.append(argVal)

        try:
            thing = tools[tool["function"]["name"]](*args)

            return thing
        except Exception as e:
            print(f"\033[93m tool call failed: {tool["function"]["name"]} | args: {str(args)} | error: {str(e)}\033[0m")
            return f"tool call failed: {tool["function"]["name"]} | args: {str(args)} | error: {str(e)}"

{
0: {'index': 0, 'id': 'JN6cYUQJOlxrcnPBiS8HekcuzIuTNsgb', 'type': 'function', 'function': {'name': 'get_weather', 'arguments': {"param1": "oslo"}}},
1: {'index': 1, 'id': 'bgsNTuIzuckeH8SiBPncrxlOJQUYc6NJ', 'type': 'function', 'function': {'name': 'get_weather', 'arguments': {"param1": "rome"}}},
}


