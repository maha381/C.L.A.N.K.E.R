models_raw = {
    "model_lookup": {
        "Qwen3.5-9B": 0,
        "Deepseek_V4_Flash": 1,       
        "Deepseek_V4_Pro": 2
    },

    "models": [
        {
            "id": "Qwen3.5-9B",

            "model": {
                "family": "Qwen",
                "architecture": "Qwen3",
                "version": "3.5",
                "finetune_of": None,
                "parameters_b": 9,
                "layers": 32,
                "max_context_length": 262144
            },
            "capabilities": {
                "multimodal": { "image": True, "video": False, "audio": False },
                "tools": True,
                "tools_notes": "Reliable for simple calls, occasionally drops args on nested JSON",
                "reasoning": True
            },
            "metadata": {
                "source": "https://huggingface.co/Qwen/Qwen3.5-9B",
                "release_date": "02-03-2026",
                "notes": None
            },
            "jinja": None,
            "access": {
                "local": {
                    "available": True,
                    "files": {
                        "mmproj": {
                            "location": "/home/maha/Projects/models/Qwen3.5-9B/mmproj-F16.gguf",
                            "size_gb": 0.92
                            },
                        "quant_lookup": {
                            "IQ4_NL": 0
                        },
                        "quants": [
                            {
                                "id": "IQ4_NL",
                                "location": "/home/maha/Projects/models/Qwen3.5-9B/Qwen3.5-9B-IQ4_NL.gguf",
                                "source": "https://huggingface.co/unsloth/Qwen3.5-9B-GGUF",
                                "size_gb": 5.4,
                                "kv_gb_per_1k": {
                                "f16": 0.45,
                                "q8_0": 0.25,
                                "q4_0": 0.15
                                }
                            }
                        ]
                    }
                }
            },
            
        "profiles": [
            {
                "name": "assistant",

                "local": True,

                "quant": "IQ4_NL",
                "k_cache_quant": "IQ4_NL",
                "v_cache_quant": "IQ4_NL",
                "gpu_layers": 99,

                "context_length": 32768,
                "reasoning": True,
                "reasoning_budet": 192,
                "sampling": {
                    "temperature": 0.7,
                    "top_p": 0.95,
                    "top_k": 40,
                    "min_p": 0.05,
                    "repeat_penalty": 1.05
                }
            }
        
        ]
        },
        {
            "id": "Deepseek-V4-Flash",

            "model": {
                "family": "Deepseek",
                "architecture": "Deepseek-V4",
                "version": "V4-Flash",
                "finetune_of": None,
                "parameters_b": 304,
                "max_context_length": 1048576
            },
            "capabilities": {
                "multimodal": {"image": False, "video": False, "audio": False },
                "tools": True,
                "tools_notes": None,
                "reasoning": True
            },
            "metadata": {
                "source": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731",
                "release_date": "31-07-2026",
                "notes": None
            },
            "jinja": None,

            "access": {
                "local": {
                    "available": False
                },
    
            "cloud": {
                "available": True,
                "provider": "DeepSeek",
                "api_endpoint": "https://api.deepseek.com",
                "id": "deepseek-v4-flash",
                "api_key_env": "DEEPSEEK_API_KEY",
                "pricing_per_m_tokens": { "input": 0.14, "output": 0.28 }
            
            } 
            }

        },
        {
            "id": "Deepseek-V4-Pro",

            "model": {
                "family": "Deepseek",
                "architecture": "Deepseek-V4",
                "version": "V4-Pro",
                "finetune_of": None,
                "parameters_b": 1659,
                "max_context_length": 1048576
            },
            "capabilities": {
                "multimodal": {"image": False, "video": False, "audio": False },
                "tools": True,
                "tools_notes": None,
                "reasoning": True
            },
            "metadata": {
                "source": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro",
                "release_date": "24-04-2026",
                "notes": None
            },
            "jinja": None,

            "access": {
                "local": {
                    "available": False
                },
    
            "cloud": {
                "available": True,
                "provider": "DeepSeek",
                "api_endpoint": "https://api.deepseek.com",
                "id": "deepseek-v4-pro",
                "api_key_env": "DEEPSEEK_API_KEY",
                "pricing_per_m_tokens": {"input": 0.44, "output": 0.87}
            
            } 
            }

        }
    ]
    
}



settings_raw = {
    "llamaCPP_binary": "/home/maha/llama.cpp/build/bin/llama-server",

    "llm": {
        "active_model": {
            "model": "Qwen3.5-9B",
            "quant": "IQ4_NL"
        },
        "context": 40960,
        "temperature": 0.7,
        "profile": "assistant"


    },
    "prefrences": {
        
    }





}

#print(models_raw["models"][models_raw["model_lookup"][settings_raw["llm"]["active_model"]["model"]]["quants"]["quant_lookup"][settings_raw["llm"]["active_model"]["quant"]]])

