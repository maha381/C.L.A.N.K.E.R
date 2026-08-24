from pathlib import Path

from llm.streaming import parseOutput
from mcp.registry import get_tools_data
from llm.tool_dispatch import dispatch

class color:
    DARK_GRAY = '\033[90m'
    WHITE = '\033[97m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    RESET = '\033[0m'



tool_list = [{"type": "function", "function": tool} for tool in get_tools_data().tool_list] # list of tools

messages_abc = [

]



# calls the right shi
def orchastration(prompt, messages):
    messages.append({"role": "user", "content": prompt})

    while True:
        content = ""
        # output from the llm after parseOutput already parsed the tool calls
        for chunk in parseOutput(messages, tool_list):

            if chunk["reasoning_content"]:
                print(color.DARK_GRAY + chunk["reasoning_content"] + color.RESET, end="", flush=True)


            # the actual output from the llm
            if chunk["content"]:
                content += chunk["content"]
                print(chunk["content"], end="", flush=True) # currently just prints the output because i havent made the frontend        
        print()

        # 
        if chunk["tool_call"]:
            messages.append({"role": "assistant", "content": content, "tool_calls": chunk["tool_call"]}) # appends the toolcalls to messages
            tool_return = dispatch(chunk["tool_call"]) # dispatches them to be actually called
            messages.extend(tool_return) # adds the tool returns to context

        if content: # adds the llms content aka answer to the context
            messages.append({"role": "assistant", "content": content}) 
            break


if __name__ == "__main__":
    while True:
        orchastration(input("Input: "), messages_abc)




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