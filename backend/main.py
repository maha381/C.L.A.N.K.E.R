from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pathlib import Path
from pydantic import BaseModel

from api.chat import orchastrator
from api import chat 

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


#app = FastAPI()
#
#@app.post("/chat")
#def root():
#    return "hello world"

messages = []


def main(prompt, messages):
    content = ""

    messages.append({"role": "user", "content": prompt})
    for res in orchastrator(messages=messages):

        print(f"{color.WHITE}{res["content"] or ""}{color.RESET}", end="", flush=True)
        print(f"{color.DARK_GRAY}{res["reasoning_content"] or ""}{color.RESET}", end="", flush=True)





        content += res.get("content") or ""

        tool_calls = res.get("tool_calls", None)
        tool_return = res.get("tool_return", None)



    print()
    messages.append({"role": "assistant", "content": content or None, "tool_calls": tool_calls})
    if tool_calls:
        messages.extend(tool_return)
    print(color.CYAN, tool_calls or "", color.RESET)
    print(color.RED, tool_return or "", color.RESET)



if __name__ == "__main__":
    while True:
        prompt = input("prompt: ")
        if prompt == "END":
            break   
        main(prompt, messages)







#FIX ECHO TOOL NOT RETURNING THE ARGS PROPERLY