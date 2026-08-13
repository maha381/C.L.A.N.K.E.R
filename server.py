
import subprocess

def startServer():
    subprocess.Popen([
        "/home/maha/llama.cpp/build/bin/llama-server",
        "--host", "0.0.0.0",
        "--temp", "0.7",
        "-m", "/home/maha/Projects/models/Qwen3.5-9B/Qwen3.5-9B-IQ4_NL.gguf",

        "-ngl", "99",
        "-fa", "on",

  
        "-c", "40960", 
        "--cache-type-k", "q4_0", 
        "--cache-type-v", "q4_0",

        "--reasoning", "on",
        "--reasoning-budget", "192",
    ],
    start_new_session=True)

def server(ReasoningAmount) -> int:
    #shut down server first
    subprocess.run(["pkill", "llama-server"])

    startServer()




server(0)