import openai


class OpenAIAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_response(self, prompt: str) -> str:
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=f"{prompt}:",
                temperature=0.7,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Произошла ошибка при обработке вашего запроса."

