# Jarvis — To-do List

High-level roadmap. Keep it scannable; add detail as checkboxes under each item.

## 🔧 1. Fix the Codebase

### Basics & setup
- [ ] Set up the basics again
    - [ ] Loading models & settings — `config.py` is currently broken (`profile` used before assignment)
    - [ ] Local vs cloud LLM support
    - [ ] Streaming vs non-streaming support

### Core rewrite
- [ ] Redo main files (`main.py`, tool calling)
    - [ ] Cleaner `main.py` — move non-request logic out of `SendRequest`
    - [ ] Turn `SendRequest` into a generator
    


### Tool calling
- [ ] Rework tool-calling to use MCP

### Observability
- [ ] Logging everywhere: tool calls, tool returns, failure rate, tokens, input/output, cache hit/miss

## ✨ 2. New Stuff

- [ ] **Frontend website** (`frontend/`)
    - [ ] Basic site talking to the backend
    - [ ] Later: fancy stuff (streaming UI, voice control, …)
- [ ] **Tools** — more beyond weather / location
- [ ] **RAG** — retrieval-augmented generation
- [ ] **Voice mode** (`backend/voice/` is empty)

## 💡 3. Related Ideas

- [ ] Finetune Nvidia LocateAnything on a smaller model (e.g. Qwen3.5-0.8B)
- [ ] Hook Jarvis up to Meta smart glasses





STILL NEED AI TO ORGANIZE CORRECTLY:

additionally add something more to the llm profiles like global shared profiles between models


locate anything hooked up to meta smart glasses to 