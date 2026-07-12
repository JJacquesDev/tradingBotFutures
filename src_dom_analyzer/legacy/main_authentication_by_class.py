"""
    Name : main_authentication_by_class
    purpoose : main code wich call class client_auth to connect my bot to projectx api
    author : Jean-Jacques BABIN-D.
    licence : jeanjacquesBD@
    creation date : 12/01/2026
"""
from classes.client_auth import Topstep_api_logging

def log_to_api_tsx():
    """ Log to the topstepx api 
        Parameters : 
            None
        Returns : 
            str : string messages
    """
    # API URL
    API_BASE_URL = "https://api.topstepx.com"
    API_LOGIN_URL = API_BASE_URL + "/api/Auth/loginKey"

    # Identifiants
    USERNAME = "JJ2226"
    API_TSX_KEY = "C3OxmgEjd/ScLLvogESQQYIPvrDKzw5HVWk8v8Mjf8Q="
    

    o_api_logging = Topstep_api_logging(API_BASE_URL, API_LOGIN_URL, USERNAME, API_TSX_KEY)
    try:
        login = o_api_logging.login()
    except Exception as e:
        print("API CONNECTION ERROR : ", e)


if __name__=="__main__":
    """Perform login to an online website session"""
    log_to_api_tsx()