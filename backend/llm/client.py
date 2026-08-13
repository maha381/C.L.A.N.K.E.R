
from openai import OpenAI
import os
from dotenv import load_dotenv
from typing import Any, Iterator

load_dotenv()
DeepseekAPIK=os.getenv("DEEPSEEK_API_KEY")


def sendRequest(messages: list[dict[str, Any]], tools: list[dict] | None = None) -> Iterator[Any]:
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
        extra_body={"thinking": {"type": "enabled"}},
        model="deepseek-v4-flash"    
    )

    for chunk in response:
        yield chunk