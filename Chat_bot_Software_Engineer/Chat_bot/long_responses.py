
from Chat_bot_Software_Engineer.api.api_status import *
import random
from Chat_bot_Software_Engineer.SQL.SQL_tools import *
from Chat_bot_Software_Engineer.api.api_tools import *
from Chat_bot_Software_Engineer.api.settings import contact_info

#Long response
customer_service = f"I'm affraid im not as smart as I though but surely one of our customer service employees is it.\nHere is their contact info {contact_info} they will be happy to support you. "

#Delivery Response
def delivery_response(merchant_id):
    contact_info = 'customer_service@help.br'
    #TBD check that all api are [200] if not -> answer internar error

    #get id sale from SQL
    id_sale = get_sale_id_SQL(merchant_id)

    #---------api_sale_status--------------------
    sale_api_status = delivery_api_status(id_sale,'id_sale')

    if sale_api_status == 'error':
        return f'Oh, we got an internal issue please contact: {contact_info}'
    #--------------------------------


    #get info from tracking API
    tracking_info = generate_sale_tracking_info(id_sale)
    #get info zip code API
    zip_code = tracking_info.get("destination_zip_code")

    # /!\ if tracking_info.get("destination_zip_code") == 'NA' -> 'we missing your delivery info' -> send delivery info to api

    #---------api_zip_code_status--------------------
    zip_code_api_status = delivery_api_status(zip_code,'zip_code')

    if zip_code_api_status == 'error':
        return f'Oh, we got an internal issue please contact: {contact_info}'
    #--------------------------------





    zip_code_info = generate_sale_zip_info({'zip_code':zip_code})
    #variables
    delivery_forecast = tracking_info.get('delivery_forecast')
    order_status = tracking_info.get('status')
    neighborhood = zip_code_info.get('neighborhood')
    city = zip_code_info.get('city')
    street = zip_code_info.get('street')
    state = zip_code_info.get('state')
    complement = zip_code_info.get('complement')

    if complement is not None and isinstance(complement,str) and len(complement)>0: #do something when there is a complement
        return print(f"Concerning your current issue\nYour machine it's expected to be deliver the \033[1m{delivery_forecast}\033[0m\nTo the following address:\n\033[1m{state}, {city}, {street}, {neighborhood}, {zip_code}\033[0m, \033[1m{complement}\033[0m.\nStatus: \033[1m{order_status}\033[0m")
    else:
        return print(f"Concerning your current issue\nYour machine it's expected to be deliver the \033[1m{delivery_forecast}\033[0m\nTo the following address:\n\033[1m{state}, {city}, {street}, {neighborhood}, {zip_code}\033[0m.\nStatus: \033[1m{order_status}\033[0m")




def unknown():
    response = ["I'm affraid I did not understand your message.\nCould you re-phrase that, please? ",
                "Could you be more specific with your request?",
                "Could you give me only key words that define your problem?"][random.randrange(3)]

    return response
