import requests
import json
from .toolcall import toolcall
from openai import OpenAI
import os
import copy
from dotenv import load_dotenv
from typing import Any, Iterator

load_dotenv()
DeepseekAPIK=os.getenv("DEEPSEEK_API_KEY")

with open(os.path.join(os.path.dirname(__file__), "systemprompt.md"), "r") as file:
    systemPrompt = file.read()


with open(os.path.join(os.path.dirname(__file__), "tools/tools.json"), "r") as file:
    tools = json.loads(file.read())
messages = [{"role": "system", "content": f"{systemPrompt}"},
]



def sendRequest(messages: list[dict[str, Any]], tools: list[dict]) -> Iterator[Any]:



    client = OpenAI(
        #http://0.0.0.0:8080/v1
        base_url="https://api.deepseek.com",
        api_key=DeepseekAPIK
    )

    response = client.chat.completions.create(
        messages=messages,
        tools=tools,
        max_tokens=512,
        stream=True,
        parallel_tool_calls=True,
        model="deepseek-v4-flash"    
    )

    content = ""
    #for each token in the response


    toolsthingmhm = {}
    for chunk in response:

        delta = chunk.choices[0].delta


        #response
        if delta.content:
            print(f"\033[92m{delta.content:}\033[0m", end="", flush=True)
            content += delta.content

        #if reasoning content, print it    
        elif getattr(delta, 'reasoning_content', None):
            print(f"\033[91m{getattr(delta, 'reasoning_content', None)}\033[0m", end="", flush=True)
        #toolcall

        #handles everything for sending the toolcalls
        elif delta.tool_calls:

            for tc in delta.tool_calls:

                if tc.index not in toolsthingmhm:
                    index = tc.index
                    toolsthingmhm[index] = {"id": tc.id, "type": "function", "function": {"name": tc.function.name, "arguments": ""}}


                toolsthingmhm[index]["function"]["arguments"] += tc.function.arguments or ""



    if content:
        messages.append({"role": "assistant", "content": content})

    if toolsthingmhm:
        #print(f"yooyoyo  --{tool_args}--")

        messages.append({
            "role": "assistant",
            "tool_calls": [copy.deepcopy(toolsthingmhm[x]) for x in toolsthingmhm]})
        #print(f"parsed: --{parsedtool}--")

        toolReturn = toolcall(toolsthingmhm)
        print(f"\033[93m{toolReturn}\033[0m")

        messages.append({
            "role": "tool",
            "tool_call_id": toolsthingmhm[index]["id"],
            "content": json.dumps(toolReturn)
        })


        #print(f"\033[93m{toolReturn}\033[0m")

        sendRequest(messages, tools)


local = True

while True:
    messages.append({"role": "user", "content": input("\nInput: ")})
    sendRequest(messages, tools)    

