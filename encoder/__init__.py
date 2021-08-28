import json
class JSON:
    def encode(payload : dict) -> str:
        return json.dumps(payload)

    def decode(payload:str) -> dict:
        return json.loads(payload)