import openai
from config import OPENAI_KEY

openai.api_key = OPENAI_KEY

def generate_tweet():
    prompt = "Generate a creative, engaging tweet on tech and AI"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=60
    )
    return response.choices[0].text.strip()