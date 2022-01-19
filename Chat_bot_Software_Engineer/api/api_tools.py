import requests
from Chat_bot_Software_Engineer.api.settings import *

#----Functions sales_id: Tracking & Zip_code----
#Tracking Function

def generate_sale_tracking_info(params_request):
    contact_info = 'customer_service@help.br'
    url = sale_id_api+HTTP_request_sale_track

    try:
        response = requests.post(url, json=params_request, headers=header)
        response.raise_for_status()

    except requests.exceptions.HTTPError as errh:
        return f"An Http Error occurred: Please, contact us at: {contact_info}"
    except requests.exceptions.ConnectionError as errc:
        return f"A Connection Error occurred: Please, try again later or contact us at: {contact_info}"
    except requests.exceptions.Timeout as errt:
        return f"A Timeout Error occurred: Please, try again later or contact us at: {contact_info}"
    except requests.exceptions.RequestException as err:
        return f"An Unknown Error occurred: Please, contact us at: {contact_info}"

    return response.json()
#Zip code Function

def generate_sale_zip_info(params_request):
    contact_info = 'customer_service@help.br'
    url = sale_id_api+HTTP_request_sale_zip

    try:
        response = requests.post(url, json=params_request, headers=header)
        response.raise_for_status()

    except requests.exceptions.HTTPError as errh:
        return f"An Http Error occurred: Please, contact us at: {contact_info}"
    except requests.exceptions.ConnectionError as errc:
        return f"A Connection Error occurred: Please, try again later or contact us at: {contact_info}"
    except requests.exceptions.Timeout as errt:
        return f"A Timeout Error occurred: Please, try again later or contact us at: {contact_info}"
    except requests.exceptions.RequestException as err:
        return f"An Unknown Error occurred: Please, contact us at: {contact_info}"

    return response.json()


#----Function Chip Status-----
def generate_chip_info(params_request):
    contact_info = 'customer_service@help.br'
    url = chip_api+HTTP_request_chip

    try:
        response = requests.post(url, json=params_request, headers=header)
        response.raise_for_status()

    except requests.exceptions.HTTPError as errh:
        return f"An Http Error occurred: Please, contact us at: {contact_info}"
    except requests.exceptions.ConnectionError as errc:
        return f"A Connection Error occurred: Please, try again later or contact us at: {contact_info}"
    except requests.exceptions.Timeout as errt:
        return f"A Timeout Error occurred: Please, try again later or contact us at: {contact_info}"
    except requests.exceptions.RequestException as err:
        return f"An Unknown Error occurred: Please, contact us at: {contact_info}"

    return response.json()

#----Function all Active Conversations info----
def generate_all_act_conv_info():
    url = conversations_api+HTTP_request_conversation
    response = requests.post(url, headers=header)
    json_response = response.json() #retrieve active conversations ID

    active_chat_list = [] #Create a list of active conversations info
    for values in json_response.values():
        for val in values:
            params_conver_info = {'conversation_id': str(val)}
            response = requests.post(conversations_api+HTTP_request_conversation_info, headers=header, json=params_conver_info)
            active_chat_list.append(response.json())

        return active_chat_list

#----Function all Active Chats List----
def generate_act_convs_list():
    url = conversations_api+HTTP_request_conversation
    response = requests.post(url, headers=header)
    json_response = response.json() #retrieve active conversations ID

    active_convs_list = json_response.get('conversation_ids')
    return active_convs_list

#----Function one conversation info----
def generate_act_conv_info(conversation_id):

    url = conversations_api+HTTP_request_conversation_info
    params = {"conversation_id": conversation_id}
    response_conversation = requests.post(url, json=params, headers=header)
    conversation_info = response_conversation.json()

    return conversation_info

# for pipeline response
def generate_info_of_conv(conversation_id, info_needed):

    conversation_id = str(conversation_id)
    info_needed = str(info_needed)

    url = conversations_api+HTTP_request_conversation_info
    params = {"conversation_id": conversation_id}
    response = requests.post(url, json=params, headers=header)
    json_response = response.json()

    info = json_response.get(info_needed)

    return info

#Send API_Response

def send_response_api(conversation_id, message):

    conversation_id = str(conversation_id)
    message = str(message)

    url = conversations_api+HTTP_send_conversation
    params = {'conversation_id': conversation_id, 'message': message}

    try:
        response = requests.post(url,json=params, headers= header)
        response.raise_for_status()

    except requests.exceptions.HTTPError as errh:
        return f"An Http Error occurred: Please, contact us at: {contact_info}"
    except requests.exceptions.ConnectionError as errc:
        return f"A Connection Error occurred: Please, try again later or contact us at: {contact_info}"
    except requests.exceptions.Timeout as errt:
        return f"A Timeout Error occurred: Please, try again later or contact us at: {contact_info}"
    except requests.exceptions.RequestException as err:
        return f"An Unknown Error occurred: Please, contact us at: {contact_info}"

    return response.json()


#Check the status for delivery responses
def delivery_api_status(param, code):

    code = str(code)
    param = str(param)

    if code == 'zip_code':
        response = generate_sale_zip_info({code: param})
    elif code == 'id_sale':
        response = generate_sale_tracking_info({code: param})

    if isinstance(response,dict):

        return 'ok'

    else:
        return 'error'
