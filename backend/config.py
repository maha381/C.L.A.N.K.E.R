import json
from pathlib import Path
from dataclasses import dataclass

@dataclass
class modelInfo:
    name: str
    id: str
    url: str
    api_key_name: str

    @classmethod
    def model_info(cls):
        models_raw = json.loads((Path(__file__).parent.parent / "models.json").read_text())

        model_dict = None
        model_list = models_raw.keys()
        print("_"*9)
        print(f"{"\n".join(list(model_list))}\n")

        while not model_dict:
            wanted_model = input(f"pick a model: \n > ")

            model_dict = models_raw.get(wanted_model, None)
            if model_dict is not None:
                print("-"*9)

                return cls(
                    name = model_dict["name"],
                    id = model_dict["id"],
                    url = model_dict["endpoint"],
                    api_key_name = model_dict["api_key_name"]
                )
        