import pandas as pd
import requests as request
import json

sdw2023_api_url = 'https://sdw-2023-prod.up.railway.app'

#EXTRACT
#TODO Extrair os IDs do Arquivo CSV.
df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()
#print(user_ids)

#TODO Obter os dados de cada ID usando a API da Santander Dev Week 2023
def get_user(id):
    response = request.get(f'{sdw2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if(user := get_user(id)) is not None]
#print(json.dumps(users, indent=2))

#TRANSFORM
pip install openai

