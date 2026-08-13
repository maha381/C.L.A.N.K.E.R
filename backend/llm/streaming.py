
import os
from llm.client import sendRequest
from dotenv import load_dotenv
from dataclasses import dataclass

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

load_dotenv()
DeepseekAPIK=os.getenv("DEEPSEEK_API_KEY")

#systemPrompt = (Path(__file__).parent.parent.parent / "systemprompts/Jarvis-v2.md").read_text(encoding="utf-8")

#tools = json.loads((Path(__file__).parent.parent /  "tools/tools.json").read_text(encoding="utf-8"))

#messages = [{"role": "system", "content": f"{systemPrompt}"}]

messages = [{"role": "system", "content": f"you are Jarvis a personal ai assistant, talk like Jarvis from the ironman movies but DO NOT roleplay or come up with fake statistics or scenarios just because thats how jarvis in the movies would answer"},]

prompt = ""

@dataclass
class streamEvent:
    content: str | None
    reasoning_content: str | None
    tool_call: dict | None

#parses h
def parseOutput(prompt):
    tool_dict = {}

    messages.append({"role": "user", "content": prompt})    


    for chunk in sendRequest(messages=messages):
        delta = chunk.choices[0].delta


        # checks if theres tool_calls in the chunk
        if getattr(delta, "tool_calls", None):

            # incase delta.tool_calls contains parts of multiple toolcalls at once
            for tc in delta.tool_calls:
                index = tc.index

                # if its new to the tool_dict
                if index not in tool_dict:
                    tool_dict[index] = {
                        "id": None,
                        "type": "function",
                        "function": {"name": None, "arguments": ""}
                        }

                entry = tool_dict[index]

                # edits the entry and also the equivalent in tool_dict
                # sets the other stuff like id and name
                if entry["id"] is None and tc.id:
                    entry["id"] = tc.id
                if entry["function"]["name"] is None and tc.function and tc.function.name:
                    entry["function"]["name"] = tc.function.name

                # adds the tool arguments as they come
                if tc.function and tc.function.name:
                    entry["function"]["arguments"] += tc.function.arguments

        yield streamEvent(
            content=getattr(delta, "content", None),
            reasoning_content=getattr(delta, "reasoning_content", None),
            tool_call=tool_dict
        )






if __name__ == "__main__":

    while prompt != "Quit":

        prompt = input("\nPrompt: ")
        parseOutput(prompt)

