import requests
from config import OPENROUTER_API_KEY, OPENROUTER_URL, MODEL


class AI:

    def ask(self, prompt):

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "You are ACE, a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        try:

            response = requests.post(
                OPENROUTER_URL,
                headers=headers,
                json=data,
                timeout=30
            )

            response.raise_for_status()

            return response.json()["choices"][0]["message"]["content"]

        except Exception as e:
            return f"Error: {e}"