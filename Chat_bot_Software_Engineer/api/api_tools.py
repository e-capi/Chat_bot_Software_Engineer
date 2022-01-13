import requests
from api.settings import *


#----Functions sales_id: Tracking & Zip_code----
#Tracking Function

def generate_sale_tracking_info(params_request):
    url = sale_id_api+HTTP_request_sale_track

    response_sale_track = requests.post(url, json=params_request, headers=header)
    return response_sale_track.json()

#Zip code Function

def generate_sale_zip_info(params_request):
    url = sale_id_api+HTTP_request_sale_zip

    response_sale_zip = requests.post(url, json=params_request, headers=header)
    return response_sale_zip.json()


#----Function Chip Status-----
def generate_chip_info(params_request):
    url = chip_api+HTTP_request_chip

    response_chip = requests.post(url, json=params_request, headers=header)
    return response_chip.json()

#----Function Active Conversations info----
def generate_act_conv_info():
    response_conversation = requests.post(conversations_api+HTTP_request_conversation, headers=header)
    json_response_conversation = response_conversation.json() #retrieve active conversations ID

    active_chat_list = [] #Create a list of active conversations info
    for values in json_response_conversation.values():
        for val in values:
            params_conver_info = {'conversation_id': str(val)}
            response_conversation = requests.post(conversations_api+HTTP_request_conversation_info, headers=header, json=params_conver_info)
            active_chat_list.append(response_conversation.json())

        return active_chat_list
