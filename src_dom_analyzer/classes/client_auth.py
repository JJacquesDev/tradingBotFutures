"""
Docstring for dev_dom_analyzer.source_dom_analyzer.classes.client_auth
purpose : manage login and authentification  with topstep/projectx api
author : Jean-Jacques BABIN-DAMANA
Created : 13/01/2026
licence : jeanjacquesBD@

PROJECTX API RESOURCES 13/01/2026 :
-----------------------------------
FIRST CONNECTION
----------------
RESQUEST :
    curl -X 'POST' \
    'https://api.topstepx.com/api/Auth/loginKey' \
    -H 'accept: text/plain' \
    -H 'Content-Type: application/json' \
    -d '{
        "userName": "string",
        "apiKey": "string"
    }'
REPONSE :
    {
    "token": "your_session_token_here",
    "success": true,
    "errorCode": 0,
    "errorMessage": null
    }
WHEN TOKEN EXPIRE VALIDATE SESSION FOR NEW TOKEN
------------------------------------------------
REQUEST
    curl -X 'POST' \
    'https://api.topstepx.com/api/Auth/validate' \
    -H 'accept: text/plain' \
    -H 'Content-Type: application/json'
RESPONSE
    {
    "success": true,
    "errorCode": 0,
    "errorMessage": null,
    "newToken": "NEW_TOKEN"
    }


"""
import json
import requests

PATH_AUTH_FILE = r"C:\Users\babin\Projects_trading_bot\project_DOM_analyzer\dev_dom_analyzer\source_dom_analyzer\resources\auth.json"
# Endpoints
ENDPOINT_REVALIDATE_TOKEN = "/api/Auth/validate"

class Topstep_api_logging:
    """
    This class manage fir login connetion to the api,
    Autoreconnection with token for same session,
    manage token and connection errors
    """
    def __init__(self, api_url_base, api_url_login, 
                 username, 
                 api_key
                ):
        self.api_url_base = api_url_base
        self.api_url_login = api_url_login
        self.username = username
        self.api_key = api_key
        self.base_headers = {
            "accept": "text/plain",
            "Content-Type": "application/json"
        }
        self.json_request = {
            "userName": self.username,
            "apiKey": self.api_key
        }
        self.token = None

    
    def login(self):
        print("Trying to connect to the TopstepX API...")
        response = requests.post(self.api_url_login, 
                                headers=self.base_headers, 
                                json=self.json_request)
        print("HTTPS RESPONSE STATUS CODE : ", response.status_code)
        if not response.text:
            print("No response received (No json data)")
        # Success connected
        if response.json()["success"]:
            print("Successfully connected to API!")
            self.token = response.json()["token"]
            with open(PATH_AUTH_FILE,"w") as f:
                json.dump({"token": self.token}, f)
                print(f"Token loaded in {PATH_AUTH_FILE}")

        # If Token expired get a new one
        elif response.status_code == 401:
            print("Token expired, new connexion...")
            result_new_response = self.validate_token(ENDPOINT_REVALIDATE_TOKEN)
            self.token = result_new_response["newToken"]
            with open(PATH_AUTH_FILE,"w") as f:
                json.dump({"newToken": self.token}, f)
                print(f"New Token loaded in {PATH_AUTH_FILE}")
        else:
            print("ERROR during API Connexion")   
            response.raise_for_status()
        

    def validate_token(self, endpoint):
        """
        Effectue une requête POST sur un endpoint.
        Si le token est expiré (401), relance le login.
        """
        url = f"{self.api_url_base}{endpoint}"
        r = requests.post(url, headers=self.base_headers)
        r.raise_for_status()  # Lève une exception pour d'autres erreurs HTTP
        return r.json()

