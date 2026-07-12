import json
import requests

def log_to_api_tsx_session():
    """ Log to the topstepx api 
            # Projectx reference :
            # response code 200 =
            # {
            #     "success": true,
            #     "errorCode": 0,
            #     "errorMessage": "string",
            #     "token": "string"
            # }
    Parameters : 
        None
    Returns : 
        str : string messages
    """

    api_url = "https://api.topstepx.com/api/Auth/loginKey"
    USERNAME = ""
    API_TSX_KEY = ""
    PATH_AUTH_FILE = r"C:\Users\babin\Projects_trading_bot\project_DOM_analyzer\dev_dom_analyzer\source_dom_analyzer\resources\auth.json"
    headers = {
        "accept": "text/plain",
        "Content-Type": "application/json"
    }

    data = {
        "userName": USERNAME,
        "apiKey": API_TSX_KEY
    }

    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 200:
        print("response status code = ",response.status_code)
        print("Connexion à l'api réussi!")
        print("response message : ", response.json())
        result = response.json()
        token = result["token"]
        with open(PATH_AUTH_FILE,"w") as f:
            json.dump({"token": token}, f)
    else:
        print(response.status_code)
        print(response.text)





if __name__=="__main__":
    """Perform login to an online website session"""
    log_to_api_tsx_session()