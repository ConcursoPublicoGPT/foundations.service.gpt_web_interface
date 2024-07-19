import requests
import json


class DocumentsRequester:
    @staticmethod
    def get():
        response = requests.get(
            "https://hcj05gvorj.execute-api.us-east-1.amazonaws.com/v1_0_0/embeddings/documents",
        )

        if response.status_code == 200:
            data = json.loads(json.loads(response.content).get("body"))

            return data
        else:
            return None
