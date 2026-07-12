"""
Docstring for dev_dom_analyzer.source_dom_analyzer.main_dom_analyzer
    Name : main_dom_analyzer.py
    purpoose : Collect and analyze data from DOM in a web site 
    author : Jean-Jacques BABIN-D.
    licence : LGPL
    creation date : 12/01/2026
"""
import json
import requests
from classes.client_auth import Topstep_api_logging

# API URL
API_BASE_URL = "https://api.topstepx.com"
API_LOGIN_URL = API_BASE_URL + "/api/Auth/loginKey"
API_ACCOUNT_SEARCH_URL = API_BASE_URL + "/api/Account/search"

HEADERS = {
    "accept": "text/plain",
    "Content-Type": "application/json"
}

PATH_ACCOUNTS_DATA = r"C:\Users\babin\Projects_trading_bot\project_DOM_analyzer\dev_dom_analyzer\source_dom_analyzer\resources\account_data_file.json"

def log_to_api_projectx():
    """ Log to the topstepx api 
        Parameters : 
            None
        Returns : 
            str : string messages
    """
    # Identifiants
    USERNAME = "JJ2226"
    API_TSX_KEY = "C3OxmgEjd/ScLLvogESQQYIPvrDKzw5HVWk8v8Mjf8Q="

    o_api_logging = Topstep_api_logging(API_BASE_URL, API_LOGIN_URL, USERNAME, API_TSX_KEY)
    try:
        login = o_api_logging.login()
    except Exception as e:
        print("API CONNECTION ERROR : ", e)


def pick_up_accounts_data():
    """pick up all account data associated with user"""
    print("\n")
    print("Trying to pick up account data...")
    # Pick up active account data
    response = requests.post(API_ACCOUNT_SEARCH_URL, headers=HEADERS,json={"onlyActiveAccounts": True})
    print("RESPONSE STATUS CODE : ", response.status_code)
    print("RESPONSE RECEIVED : ", response.text)
    print("\n")
    # if response.json()["success"]:
    #     print("Account data retreived!")
    #     with open(PATH_ACCOUNTS_DATA, "w") as f:
    #         json.dump({"ACCOUNTS DATA": response.json()},f)
    # else:
    #     print("Error bad data collection!")







if __name__=="__main__":
    """Perform DOM data anlyze"""
    log_to_api_projectx()
    pick_up_accounts_data()
