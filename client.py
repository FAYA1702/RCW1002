import requests

url = 'https://morfaye-c4arauaga5axf3ht.canadacentral-01.azurewebsites.net'

response = requests.get(url)

try:
    data = response.json()
    print(data['message'])
except Exception as e:
    print("Erreur lors de la lecture du JSON :", e)
    print("Contenu brut reçu :", response.text)
