import openai
from django.conf import settings

openai.api_key = settings.APIKEY

def send_code_to_api(code, method):
    res = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are so handsome"},
            {"role": "user", "content": f"{method}: {code}"},
        ],
    )
    return res["choices"][0]["message"]["content"]