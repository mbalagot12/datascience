
import requests as req
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

LOCATIONS = {"MB": "6352493312212992",
    "CityOfSparks": "5838646402875392",
    "McDonalds": "5700129931657216",
    "VTeamSE": "5356387243655168",
    "DenverMuseum": "4824167898152960"}

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

username = os.getenv("MERIDIAN_USER")
password = os.getenv("MERIDIAN_PASSWORD")
mylocation = os.getenv("LOCATION")

mauth = HTTPBasicAuth(username=username, password=password)

loginUri = 'https://edit.meridianapps.com/api/login'

def get_token_id() -> object:
    token = req.post(loginUri, {'password': password, 'email': username})
    return token.json()['token']

headers = {"Content-Type": "multipart/form-data", "Authorization": "Token " + str(get_token_id())}



