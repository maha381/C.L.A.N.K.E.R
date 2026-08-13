from pathlib import Path
from dataclasses import dataclass
from dotenv import load_dotenv

import json

settings_raw = json.loads((Path(__file__).parent.parent / "settings.json").read_text())

models_raw = json.loads((Path(__file__).parent.parent / "models.json").read_text())





@dataclass
class ModelSettings:

    local: bool
    model: str

    capabilities: dict[str, bool]
    max_context_length: int

    api_endpoint: str
    api_key_env: str | None

    stream: bool
    parallel_tool_calls: bool

    @classmethod
    def from_dict(cls, settings_raw):
        llm_settings = settings_raw["llm"]

        local = llm_settings["local"]
        model = llm_settings["local_model" if local else "cloud_model"]["model"]

        model_lookup = {m["id"]: m for m in models_raw["models"]}
        model_dict = model_lookup[model]


        return cls(
            local=local,
            model=model,

            capabilities=model_dict["capabilities"],
            max_context_length=model_dict["model"]["max_context_length"],

            api_endpoint=model_dict["access"]["cloud"]["api_endpoint"],
            api_key_env=model_dict["access"]["cloud"]["api_key_env"], 

            stream=llm_settings["models"]["stream"],
            stream=llm_settings["models"]["parallel_tool_calls"]
            

            )
    

@dataclass
class ServerSettings:         # llama.cpp
    llama_cpp_binary: str
    address: str
    port: int


    model: str 
    model_path: str

    profile: str

    quantization: str

    mmproj: bool
    mmproj_path: str | None

    context_length: int
    k_cache_quant: str
    v_cache_quant: str

    reasoning: bool
    reasoning_length: int

    gpu_layers: int


    @classmethod
    def from_dict(cls, models_raw, settings_raw):

        llm_settings = settings_raw["llm"]
        model_id = llm_settings["models"]["local_model"]


        model_lookup = {m["id"]: m for m in models_raw["models"]}

        if model_id not in model_lookup:
            raise ValueError(f"no model \"{model_id}\" in models.json")

        model_dict = model_lookup.get(model_id)


        if model_dict["access"]["local"]["available"] == False:
            raise ValueError(f"model: {model_id} not accessible locally")
        
        model_files = model_dict["access"]["local"]["files"]


        if not llm_settings["models"]["profile"]:
            raise ValueError(f"no profile selected in llm settings")
        profile_id = llm_settings["models"]["profile"]

        if profile_id not in model_dict["profiles"]:
            raise ValueError(f"profile {profile_id} not in profiles for {model_id}")

        profile = model_dict["profiles"][profile_id]

        
        quant = profile["quant"]
        quants = model_files["quants"]

        quant_lookup = {q["id"]: q for q in quants}
        model_path = quant_lookup[quant]["location"]
        mmproj = True if model_files["mmproj"] else False
        llama_cpp_dict = settings_raw["llama_cpp"]


        return cls(

            llama_cpp_binary=llama_cpp_dict["binary-path"],
            address=llama_cpp_dict["address"],
            port=llama_cpp_dict["port"],


            model=model_id,

            quantization=quant,
            model_path=model_path,

            profile=profile_id,

            gpu_layers=profile["gpu_layers"],

            mmproj=mmproj,
            mmproj_path=model_files["mmproj"]["location"] if mmproj else None,

            context_length=profile["context_length"],
            k_cache_quant=profile["k_cache_quant"],
            v_cache_quant=profile["v_cache_quant"],

            reasoning=profile["reasoning"],
            reasoning_length=profile["reasoning_budget"]
        )


if settings_raw["llm"]["local"] == True:
    llama_cpp_settings = ServerSettings.from_dict(models_raw, settings_raw)

@dataclass
class secrets:

    pass