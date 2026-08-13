jarvis/
├── backend/
│   ├── main.py                  # FastAPI app instance, startup/shutdown, route registration
│   ├── config.py                # loads env vars + settings.json into one Settings object
│   │                                                       
│   ├── api/                     # HTTP/WS route handlers only — thin, no logic
│   │   ├── chat.py              # SSE/streaming chat endpoint
│   │   └── voice.py             # WS endpoint for STT/TTS once built
│   │                                                                       
│   ├── llm/
│   │   ├── client.py            # OpenAI SDK client pointed at llama.cpp
│   │   ├── streaming.py         # tool-call accumulation logic (the dict-by-index stuff)
│   │   └── tool_dispatch.py     # central dispatcher: name -> call -> format result
│   │                                                                                           
│   ├── tools/
│   │   ├── __init__.py          # TOOL_REGISTRY = {name: (fn, schema)}
│   │   ├── web_search.py
│   │   ├── geocode.py
│   │   └── weather.py           # etc, one file per tool
│   │                                                                                                       
│   ├── rag/
│   │   ├── store.py             # vector store connection/queries
│   │   ├── ingest.py            # md+frontmatter chunk/embed pipeline
│   │   └── curator.py           # future: background fetch/classify/store agent
│   │                                                                                                   
│   ├── voice/                   # add only once you build this
│   │   ├── stt.py
│   │   └── tts.py
│   │                                                               
│   ├── db/
│   │   ├── models.py            # schema/dataclasses
│   │   └── session.py           # connection handling
│   │                                                                           
│   └── utils/
│       └── ...                  # pure stateless helpers, no I/O to llm/db/tools
│                                                                           
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js                                                                                      
│                                                        
├── data/                        # things that grow/change at runtime — gitignore most of this
│   ├── knowledge/               # Obsidian-style *.md notes (RAG source)
│   ├── vectors/                 # vector db files (chroma/faiss/etc)
│   ├── cache/                   # tool call caches (e.g. web_search.py results, geocode lookups)
│   ├── logs/                    # rotating log files (app.log, errors.log)
│   └── chat_history/            # if persisting conversations outside a db
│                                                                                        
├── settings.json                # user-editable runtime config (model name, ports, feature flags)
├── .env                         # secrets only (API keys) — never committed
└── .gitignore                   # data/, .env, __pycache__, etc