import random

from Chat_bot_Software_Engineer.SQL.SQL_tools import *
from Chat_bot_Software_Engineer.api.api_tools import *
from Chat_bot_Software_Engineer.api.settings import contact_info

#Long response
customer_service = f"I'm affraid im not as smart as I though but surely one of our customer service employees is it.\nHere is their contact info {contact_info} they will be happy to support you. "

#---------------------------Delivery Response---------------------------

def delivery_response(merchant_id):
    #TBD check that all api are [200] if not -> answer internar error

    #get id sale from SQL
    id_sale = get_sale_id_SQL(merchant_id)

    #----api_sale_status
    sale_api_status = delivery_api_status(id_sale,'id_sale')

    if sale_api_status == 'error':
        return f'Oh, we got an internal issue please contact: {contact_info}'
    #----


    #get info from tracking API
    tracking_info = generate_sale_tracking_info(id_sale)
    #get info zip code API
    zip_code = tracking_info.get("destination_zip_code")

    # /!\ if tracking_info.get("destination_zip_code") == 'NA' -> 'we missing your delivery info' -> send delivery info to api

    #----api_zip_code_status----
    zip_code_api_status = delivery_api_status(zip_code,'zip_code')

    if zip_code_api_status == 'error':
        return f'Oh, we got an internal issue please contact: {contact_info}'
    #----

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
        return f"Concerning your current issue\nYour machine it's expected to be deliver the \033[1m{delivery_forecast}\033[0m\nTo the following address:\n\033[1m{state}, {city}, {street}, {neighborhood}, {zip_code}\033[0m, \033[1m{complement}\033[0m.\nStatus: \033[1m{order_status}\033[0m"
    else:
        return f"Concerning your current issue\nYour machine it's expected to be deliver the \033[1m{delivery_forecast}\033[0m\nTo the following address:\n\033[1m{state}, {city}, {street}, {neighborhood}, {zip_code}\033[0m.\nStatus: \033[1m{order_status}\033[0m"


#---------------------------receipt Response---------------------------

def receipt_response(merchant_id):

    #get SQL receipt info
    try:
        total_receipt_info = get_receipt_info_SQL(merchant_id)
        total_transactions = get_transactions_aggregate_SQL(merchant_id).get('transactions_amount') #string
        transactions_info = get_transactions_info_SQL(merchant_id)
    except:
        return None

    #variables
    status = total_receipt_info.get('status')
    description = total_receipt_info.get('description')
    total_value = total_receipt_info.get('value')
    date = total_receipt_info.get('created_at')

    return f"\033[1mFirst of all we would like to remind you that transactions have a 24h delay before being transfered.\033[0m\nConcerning your demand here is some information:\nTransactions Date: \033[1m{date}\033[0m\nNumber of Transactions: \033[1m{total_transactions}\033[0m\nTransactions Total: \033[1mR${total_value}\033[0m\nStatus: \033[1m{status}\033[0m\nDescription: \033[1m{description}\033[0m\nTransactions Involved:\033[1m{transactions_info}\033[0m"



def unknown():
    response = ["I'm affraid I did not understand your message.\nCould you re-phrase that, please? ",
                "Could you be more specific with your request?",
                "Could you give me only key words that define your problem?"][random.randrange(3)]

    return response
