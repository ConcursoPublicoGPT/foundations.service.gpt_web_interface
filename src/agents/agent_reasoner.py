import os
from typing import Optional, Dict
from openai import OpenAI


class AgentReasoner:
    @staticmethod
    def completion(
        system_prompt: str,
        user_prompt: str,
        api_key: Optional[str] = None,
        model: str = "gpt-4o-mini",
        seed: int = 512,
    ) -> Dict:
        """
        Generate a completion using the OpenAI API.

        Args:
            system_prompt (str): The system prompt for the model.
            user_prompt (str): The user prompt for the model.
            api_key (Optional[str]): The API key for OpenAI. If not provided, it will be fetched from environment variable MAIN_OPENAI_KEY.
            model (str): The model to use for completion. Default is 'gpt-4o'.
            seed (int): The seed for random generation. Default is 512.

        Returns:
            Dict[str, Any]: The completion response parsed from plain text.
        """
        if api_key is None:
            api_key = os.getenv("MAIN_OPENAI_KEY")

        openai_client = OpenAI(api_key=api_key)

        completion = openai_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            # seed=seed,
            stream=True,
        )

        return completion

    @staticmethod
    def from_full_context(
        query: str,
        document: str,
        api_key: Optional[str] = None,
        model: str = "gpt-4o-mini",
        seed: int = 512,
    ) -> Dict:
        """
        Generate a response using the full context reasoning prompt.

        Args:
            query (str): The user's query.
            document (str): The document to base the reasoning on.
            api_key (Optional[str]): The API key for OpenAI. If not provided, it will be fetched from environment variable MAIN_OPENAI_KEY.
            model (str): The model to use for completion. Default is 'gpt-4o'.
            seed (int): The seed for random generation. Default is 512.

        Returns:
            Dict: The completion result from OpenAI.
        """
        system_prompt = AgentReasoner.get_system_prompt()
        user_prompt = AgentReasoner.get_full_context_reasoning_prompt(
            query=query, document=document
        )

        return AgentReasoner.completion(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            api_key=api_key,
            model=model,
            seed=seed,
        )

    @staticmethod
    def from_quotes(
        query: str,
        document: str,
        api_key: Optional[str] = None,
        model: str = "gpt-4o-mini",
        seed: int = 512,
    ) -> Dict:
        """
        Generate a response using the quotes reasoning prompt.

        Args:
            query (str): The user's query.
            document (str): The document to base the reasoning on.
            api_key (Optional[str]): The API key for OpenAI. If not provided, it will be fetched from environment variable MAIN_OPENAI_KEY.
            model (str): The model to use for completion. Default is 'gpt-4o'.
            seed (int): The seed for random generation. Default is 512.

        Returns:
            Dict: The completion result from OpenAI.
        """

        system_prompt = AgentReasoner.get_system_prompt()
        user_prompt = AgentReasoner.get_quotes_reasoning_prompt(
            query=query, document=document
        )

        return AgentReasoner.completion(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            api_key=api_key,
            model=model,
            seed=seed,
        )

    @staticmethod
    def get_quotes_reasoning_prompt(query: str, document: str) -> str:
        """
        Create a reasoning prompt using quotes from the document.

        Args:
            query (str): The user's query.
            document (str): The document to base the reasoning on.

        Returns:
            str: The generated reasoning prompt.
        """
        return f"""
        Você agirá como um cientista renomado especializado em abordagens da psicologia, com foco em Terapia de Aceitação e Compromisso (ACT). Sua tarefa é responder à pergunta do usuário com base nas informações contidas no documento fornecido. Aqui estão as instruções que você deve seguir:

        INSTRUÇÕES:

        - Responda à PERGUNTA do usuário usando o texto do DOCUMENTO.
        - Mantenha sua resposta fundamentada nos fatos do DOCUMENTO.
        - Responda de forma bastante detalhada à PERGUNTA, como se estivesse respondendo a um especialista no assunto.
        - Evite generalizações e favoreça o detalhamento dos conceitos abordados.
        - Estruture sua resposta de forma clara, com introdução, desenvolvimento e conclusão.
        - Use exemplos práticos ou estudos de caso mencionados no DOCUMENTO para ilustrar seus pontos.
        - Conecte diferentes conceitos presentes no DOCUMENTO para fornecer uma visão integrada e aprofundada.
        - Faça referência cruzada de diferentes seções do DOCUMENTO para mostrar uma compreensão profunda e integrada.
        - Inclua uma análise crítica dos conceitos e dados apresentados, discutindo suas implicações e possíveis interpretações.
        - Sugira soluções ou recomendações baseadas nos dados e análises do DOCUMENTO.
        - Destaque a relevância dos pontos abordados no contexto do campo de estudo específico.
        - Mencione quaisquer limitações ou controvérsias discutidas no DOCUMENTO.
        - A conclusão deve fornecer uma crítica ou sugestões de próximos passos com base no conteúdo do DOCUMENTO.
        - Nunca mencione que você está utilizando o DOCUMENTO para responder à PERGUNTA.
        - Se o DOCUMENTO não contiver os fatos para responder à PERGUNTA, retorne apenas "Desculpe-me, mas eu não sei responder sobre essa questão."
        
        PERGUNTA:

        {query}

        DOCUMENTO:

        {document}
        """

    @staticmethod
    def get_full_context_reasoning_prompt(query: str, document: str) -> str:
        """
        Create a full context reasoning prompt.

        Args:
            query (str): The user's query.
            document (str): The document to base the reasoning on.

        Returns:
            str: The generated reasoning prompt.
        """
        return f"""
        Você agirá como um cientista renomado especializado em abordagens da psicologia, com foco em Terapia de Aceitação e Compromisso (ACT). Sua tarefa é responder à pergunta do usuário com base nas informações contidas no documento fornecido. Aqui estão as instruções que você deve seguir:

        INSTRUÇÕES:

        - Responda à PERGUNTA do usuário usando o texto do DOCUMENTO.
        - Mantenha sua resposta fundamentada nos fatos do DOCUMENTO.
        - Responda de forma bastante detalhada à PERGUNTA, como se estivesse respondendo a um especialista no assunto.
        - Evite generalizações e favoreça o detalhamento dos conceitos abordados.
        - Estruture sua resposta de forma clara, com introdução, desenvolvimento e conclusão.
        - Use exemplos práticos ou estudos de caso para ilustrar seus pontos.
        - Conecte diferentes conceitos presentes no DOCUMENTO para fornecer uma visão integrada e aprofundada.
        - Inclua uma análise crítica dos conceitos e dados apresentados, discutindo suas implicações e possíveis interpretações.
        - Sugira soluções ou recomendações baseadas nos dados e análises do DOCUMENTO.
        - Destaque a relevância dos pontos abordados no contexto do campo de estudo específico.
        - Mencione quaisquer limitações ou controvérsias discutidas no DOCUMENTO.
        - A conclusão deve fornecer uma crítica ou sugestões de próximos passos com base no conteúdo do DOCUMENTO.
        - Nunca mencione que você está utilizando o DOCUMENTO para responder à PERGUNTA.
        - Se o DOCUMENTO não contiver os fatos para responder à PERGUNTA, retorne apenas "Desculpe-me, mas eu não sei responder sobre essa questão."
        
        PERGUNTA:

        {query}

        DOCUMENTO:

        {document}
        """

    @staticmethod
    def get_system_prompt() -> str:
        """
        Get the system prompt for the OpenAI model.

        Returns:
            str: The system prompt.
        """
        return """
        Você agirá como um cientista renomado especializado em abordagens da psicologia, com foco em Terapia de Aceitação e Compromisso (ACT). Aqui estão as instruções que você deve seguir:

        INSTRUÇÕES:

        - Responda de forma bastante detalhada à PERGUNTA do usuário, como se estivesse respondendo a um especialista no assunto.
        - Evite generalizações e favoreça o detalhamento dos conceitos abordados.
        - Estruture sua resposta de forma clara, com introdução, desenvolvimento e conclusão.
        - Use exemplos práticos ou estudos de caso para ilustrar seus pontos.
        - Conecte diferentes conceitos para fornecer uma visão integrada e aprofundada.
        - Inclua uma análise crítica dos conceitos e de dados, discutindo suas implicações e possíveis interpretações.
        - Sugira soluções ou recomendações.
        - Destaque a relevância dos pontos no contexto do campo de estudo específico.
        - Mencione quaisquer limitações ou controvérsias.
        - A conclusão deve fornecer uma crítica ou sugestões de próximos passos.
        - Responda sempre em português (Brasil).
        """
