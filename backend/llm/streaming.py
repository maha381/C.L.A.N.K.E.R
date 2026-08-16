
import os
from dotenv import load_dotenv
from dataclasses import dataclass

from llm.client import sendRequest

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



#systemPrompt = (Path(__file__).parent.parent.parent / "systemprompts/Jarvis-v2.md").read_text(encoding="utf-8")

#tools = json.loads((Path(__file__).parent.parent /  "tools/tools.json").read_text(encoding="utf-8"))

#messages = [{"role": "system", "content": f"{systemPrompt}"}]



#parses h
def parseOutput(messages, tools):
    """
    handles parsing the returns from the llm
    """

    tool_dict = {}   
    for chunk in sendRequest(messages=messages, tools=tools):
        delta = chunk.choices[0].delta

        # handles any tool_call part of the return
        if getattr(delta, "tool_calls", None):
            for tc in delta.tool_calls:
                index = tc.index
                #print("def", tc)
                # seperate the tool_calls 
                if index not in tool_dict:
                    tool_dict[index]={
                        "id": None,
                        "type": "function",
                        "function": {"name": None, "arguments": ""}
                        }

                entry = tool_dict[index]

                # handles id and names arriving in different chunks from the rest
                if entry["id"] is None and tc.id:
                    entry["id"] = tc.id
                if entry["function"]["name"] is None and tc.function and tc.function.name:
                    entry["function"]["name"] = tc.function.name

                if tc.function and tc.function.arguments:
                    entry["function"]["arguments"] += tc.function.arguments





    # returns the empty ones to make it easier to sort later
        yield {
            "content": getattr(delta, "content", None),
            "reasoning_content": getattr(delta, "reasoning_content", None),
            "tool_call": None
        }

    yield {
        "tool_call": list(tool_dict.values()),
        "content": None,
        "reasoning_content": None
    }

