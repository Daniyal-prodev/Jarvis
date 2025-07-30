import requests

API_KEY = "YOUR API PLEASE I HAVE USEDE OPENROUTER API YOU CAN EITHER CHANGE IT OR REMAIN IT SAME"
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
