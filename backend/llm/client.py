
from openai import OpenAI

import os
from dotenv import load_dotenv
from typing import Any, Iterator
from config import modelInfo

load_dotenv()

model_info = modelInfo.model_info()
DeepseekAPIK=os.getenv(model_info.api_key_name)




def sendRequest(messages: list[dict[str, Any]], tools: list[dict] | None = None):
    #print("\033[35m", tools, "\033[0m")
    client = OpenAI(
        #http://0.0.0.0:8080/v1
        base_url=model_info.url,
        api_key=DeepseekAPIK
    )

    response = client.chat.completions.create(
        messages=messages,
        tools=tools,
        max_tokens=512,
        stream=True,
        parallel_tool_calls=True,
        extra_body={"thinking": {"type": "enabled"}},
        model=model_info.id    
    )

    for chunk in response:
        yield chunk