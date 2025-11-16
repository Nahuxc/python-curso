## USAR LA API DE GPT4 DE OPENAI

OPENAI_KEY = "sk-xxxxx"

def call_openai_gpt(api_key, prompt):


    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-type": "application/json",
        "Autorization": f"Bearer {api_key}"
    }

    data = {
        "model": "gpt-4o-mini",
        "menssages": [{"role": "user", "content": prompt}]
    }
    
    
    response = url.post(url, json=data, headers=headers)
    
call_openai_gpt(OPENAI_KEY, "escribe un breve poema sobre la programacion")