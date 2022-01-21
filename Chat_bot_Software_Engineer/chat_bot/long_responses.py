import random

from Chat_bot_Software_Engineer.SQL.SQL_tools import *
from Chat_bot_Software_Engineer.api.api_tools import *
from Chat_bot_Software_Engineer.api.settings import contact_info


#---------------------------Delivery Response---------------------------

def delivery_response(merchant_id):

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
        return f"Concerning your current issue. Your machine it's expected to be deliver the {delivery_forecast}. To the following address: {state}, {city}, {street}, {neighborhood}, {zip_code}, {complement}. Status: {order_status}"
    else:
        return f"Concerning your current issue. Your machine it's expected to be deliver the {delivery_forecast}. To the following address: {state}, {city}, {street}, {neighborhood}, {zip_code}. Status: {order_status}"


#---------------------------Receipt Response---------------------------

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

    return f"First of all we would like to remind you that transactions have a 24h delay before being transfered.Concerning your demand here is some information: Transactions Date: {date} Number of Transactions: {total_transactions}, Transactions Total: R${total_value}, Status: {status}, Description: {description}, Transactions Involved:{transactions_info}"


#---------------------------Connection Response---------------------------

def connection_response(merchant_id):
    #get SQL receipt info
    try:
        chip_id_SQL = get_chip_id_SQL(merchant_id)
        chip_info = generate_chip_info(chip_id_SQL)
    except:
        return print('problem')

    #variables
    chip_id = chip_info.get('id')
    status = chip_info.get('status')
    description = chip_info.get('description')

    return f"Concerning your current issue: Chip id: {chip_id}, Status: {status}, Description: {description}"


#---------------------------Unknown Response---------------------------

def unknown():
    response = ["I'm affraid I did not understand your message.Could you re-phrase that, please? ",
                "Could you be more specific with your request?",
                "Could you give me only key words that define your problem?"][random.randrange(3)]

    return response


#---------------------------Customer Service Response---------------------------
customer_service = f"I'm affraid im not as smart as I though but surely one of our customer service employees is it.Here is their contact info {contact_info} they will be happy to support you. "
