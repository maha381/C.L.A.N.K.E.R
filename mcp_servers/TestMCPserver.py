import sys
import json

# {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "jarvis", "version": "0.1"}}}

# {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}}

# {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}

# {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "echo", "arguments": {"text": "hello"}}}





def log(msg):
    print(f"\033[33m[fake-server] {msg}\033[0m", file=sys.stderr, flush=True)


def send(msg):
    print(json.dumps(msg), flush=True)


def main():
    for line in sys.stdin:
        line = line.strip()

        if not line:
            continue


        try: 
            msg = json.loads(line)
        except json.JSONDecodeError:
            log(f"bad json: {line}")

        msg_id = msg.get("id")
        method = msg.get("method")

        if method == "initialize":
            send({
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "fake-server", "version": "0.1"}
                }
            })


        elif method == "Intialized":
            log("client confirmed initialized")

        elif method == "tools/list":
            send({
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools":[
                        {
                            "name": "echo",
                            "description": "Echoes back whatever text you give it",
                            "paramaters": {
                                "type": "object",
                                "properties": {
                                    "text": {"type": "string"}
                                },
                                "required": ["text"]
                            }
                        }
                    ]
                }
            })

        elif method == "tools/call":
            params = msg.get("params", {})
            tool_name = params.get("name")
            args = params.get("arguments", {})
            log(f"tool called: {tool_name} with args {args}")
            send({
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [
                        {"type": "text", "text": f"echo: {args.get('text', '')}"}
                    ],
                    "isError": False
                }
            })

        else:
            log(f"unkown method: {method}")
            if msg_id is not None:
                send({
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "error": {"code": -32601, "message": f"unknown method: {method}"}
                })

if __name__ == "__main__":
    main()