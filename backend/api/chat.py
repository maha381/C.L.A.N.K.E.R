from pathlib import Path

from llm.streaming import parseOutput
from mcp.registry import get_tools_data
from llm.tool_dispatch import dispatch



tool_list = [{"type": "function", "function": tool} for tool in get_tools_data().tool_list]
messages_abc = [
    {"role": "system", "content": f"you are Jarvis a personal ai assistant, talk like Jarvis from the ironman movies but DO NOT roleplay or come up with fake statistics or scenarios just because thats how jarvis in the movies would answer"},

]

print(tool_list)


def orchastration(prompt, messages):
    messages.append({"role": "user", "content": prompt})

    while True:
        content = ""
        for chunk in parseOutput(messages, tool_list):

            if chunk["content"]:
                content += chunk["content"]
                print(chunk["content"], end="", flush=True)                
        print()

        
        if chunk["tool_call"]:
            messages.append({"role": "assistant", "content": content, "tool_calls": chunk["tool_call"]})
            tool_return = dispatch(chunk["tool_call"])
            messages.extend(tool_return)
        else:
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