import requests
import json
import os


class KernelMemoryRequester:
    @staticmethod
    def answer(question):
        public_host = os.getenv("CONCURSOSGPT_PUBLIC_HOST")
        port = os.getenv("CONCURSOSGPT_PUBLIC_HOST_PORT")
        api_key = os.getenv("CONCURSOSGPT_HOST_API_KEY")

        data = {
            "index": "concurso-publico-gpt",
            "question": question,
            "minRelevance": 0,
        }

        response = requests.post(
            f"http://{public_host}:{port}/ask",
            headers={
                "Content-Type": "application/json",
                "Authorization": api_key,
            },
            data=json.dumps(data),
        ).json()

        if "text" in response:
            return {
                "text": response.get("text"),
                "sources": response.get("relevantSources"),
            }
        else:
            return "Infelizmente, eu não consegui responder essa pergunta se baseando no meu banco de conhecimento atual. Tente reescrever a sua pergunta de outro modo, talvez eu entende melhor :)"
