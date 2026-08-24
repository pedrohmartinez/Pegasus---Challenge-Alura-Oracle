import requests

url = "http://localhost:1234/v1/models"

response = requests.get(url)

print("Status:", response.status_code)

print("\nResposta:")
print(response.json())