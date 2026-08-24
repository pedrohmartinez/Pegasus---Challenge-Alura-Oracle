import requests

url = "http://localhost:1234/v1/chat/completions"

payload = {
    "model": "llama-3.2-1b-instruct",
    "messages": [
        {
            "role": "user",
            "content": "Explique em uma frase o que é microsserviço."
        }
    ],
    "temperature": 0.2,
    "max_tokens": 100
}


response = requests.post(
    url,
    json=payload
)

data = response.json()

answer = data["choices"][0]["message"]["content"]

print("\nResposta:")
print(answer)