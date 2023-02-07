# Faça uma requisição ao recurso usuários da API do Github,
#  exibindo o username e url de todos os usuários retornados.

import requests

url = "https://api.github.com/users"

users = requests.get(url).json()

for user in users:
    print(f"{user['login']} - {user['html_url']}")
