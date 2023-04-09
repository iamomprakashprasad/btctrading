import requests
import json
import constants

LOGGER = constants.LOGGER


class CoinmarketcapGateway:
    def __init__(self):
        self.session = requests.session()
        self.base_url = constants.COINMARKETCAP_BASE_URL
        self.session.headers['Content-Type'] = 'Application/json'
        self.session.headers['Authorization'] = constants.COINMARKETCAP_API_KEY
    
    def make_api_call(self, endpoint:str, method:str,params:dict, payload:dict):
        LOGGER.debug("Initializing api call for coinmarketcap api gateway")
        method = method.upper()
        url = f"{self.base_url}{endpoint}"
        payload = json.dumps(payload) if payload is not str else payload
        LOGGER.info("URL --> %s", url)
        LOGGER.debug("Method --> %s", method)
        LOGGER.info("Params --> %s", json.dumps(params))
        LOGGER.info("Payload --> %s", payload)
        response = self.session.request(method=method, url=url, params=params, data=payload)
        if response.status_code == 401:
            LOGGER.error("Heades --> %s", json.dumps(self.session.headers))
        if response and response.status_code == 400 or 500:
            LOGGER.error("Error Response --> %s", response)
        response.raise_for_status()
        json_response = response.json()
        LOGGER.info("Response --> %s", json.dumps(json_response))

    

