from Chat_bot_Software_Engineer.api.settings import sale_id_api, chip_api, conversations_api
import requests


#check all are API's are return <200>

def test_apis_connection():
    api_list = [sale_id_api, chip_api, conversations_api]

    for api in api_list:

        response = requests.get(api)
        assert response.raise_for_status() is None

