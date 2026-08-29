from pathlib import Path

from llm.streaming import parseOutput
from mcp.registry import get_tools_data
from llm.tool_dispatch import dispatch

class color:
    BLACK = '\033[30m'
    DARK_GRAY = '\033[90m'
    WHITE = '\033[97m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    RESET = '\033[0m'



class ChatSession:
    def __init__(self):
        self.messages = []



tool_list = [{"type": "function", "function": tool} for tool in get_tools_data().tool_list] # list of tools


# calls the right shi
def orchastrator(messages):
    tool_return = None

    # output from the llm after parseOutput already parsed the tool calls
    for chunk in parseOutput(messages, tool_list):
        chunk["tool_return"] = tool_return

        # {'content': None, 'reasoning_content': None, 'tool_call': None, 'tool_return': None}


        # outside the loop because parseOutput returns the already parsed tool calls
        if chunk["tool_calls"]:
            tool_return = dispatch(chunk["tool_calls"]) # dispatches them to be actually called
            #print(f"\033[34m AAAAABBBBCCCC {tool_return}\033[0m")

        chunk["tool_return"] = tool_return
        #print(f"\033[35m AAAAABBBBCCCC {chunk}\033[0m")
        yield chunk

    



# yo call the echo tool twice with different arguments




"""
Decorators
Generators ✅
Iterators
Iterator protocol
Context managers
closures
multithreading
multiprocessing
"""