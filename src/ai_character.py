import openai
from typing import List

class AICharacter:
    def __init__(self, name: str, expertise: List[str], api_key: str):
        self.name = name
        self.expertise = expertise
        openai.api_key = api_key

    def generate_code(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are {self.name}, an AI with expertise in {', '.join(self.expertise)}."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
