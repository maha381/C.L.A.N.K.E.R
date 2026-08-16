

"/home/maha/llama.cpp/build/bin/llama-server",
"--host", "0.0.0.0",
"--temp", "0.7",
"-m", "/home/maha/Projects/models/Qwen3.5-9B/Qwen3.5-9B-IQ4_NL.gguf",

"--mmproj", "",

"-ngl", "99",
"-fa", "on",

#"--chat-template-kwargs", "{\"model_identity\":\" ... \"}",

"-c", "32768", 
"--cache-type-k", "q4_0", 
"--cache-type-v", "q4_0",

"--jinja"

"--reasoning", "off",
"--reasoning-budget", "192",