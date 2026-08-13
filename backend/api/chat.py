from pathlib import Path
from llm import streaming


behavior_prompt = "path to behavior prompt"

def orchastration():

    for chunk in streaming.parseOutput(prompt=input("Prompt: ")):

        if chunk.tool_call:
            pass

        yield chunk

    print()



        
if __name__ == "__main__":
    orchastration()