import openai
from django.conf import settings

openai.api_key = settings.APIKEY

def send_code_to_api(code):
    res = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are so handsome"},
            {"role": "user", "content": f"Check Grammar of this sentence: {code}"},
        ],
    )
    return res["choices"][0]["message"]["content"]