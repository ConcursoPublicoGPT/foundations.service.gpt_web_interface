import requests
import json
import os


class KernelMemoryRequester:
    @staticmethod
    def answer(question):
        public_host = os.getenv("CONCURSOSGPT_PUBLIC_HOST")
        port = os.getenv("CONCURSOSGPT_PUBLIC_HOST_PORT")

        data = {
            "question": question,
            "minRelevance": 0,
        }

        response = requests.post(
            f"http://{public_host}:{port}/ask",
            headers={
                "Content-Type": "application/json",
                # "Authorization": api_key,
            },
            data=json.dumps(data),
        ).json()

        if "text" in response:
            return response
        else:
            return "Infelizmente, eu não consegui responder essa pergunta se baseando no meu banco de conhecimento atual. Tente reescrever a sua pergunta de outro modo, talvez eu entende melhor :)"
