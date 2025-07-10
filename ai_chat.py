import requests

API_KEY = "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"
MODEL = "gpt-4o-mini"

def chat_response(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 100
    }
    try:
        res = requests.post(url, headers=headers, json=data)
        return res.json()["choices"][0]["message"]["content"].strip()
    except:
        return "I'm having trouble connecting to AI."
