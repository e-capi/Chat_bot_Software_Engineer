import imp
import random
from Chat_bot_Software_Engineer.SQL.SQL_tools import *
from Chat_bot_Software_Engineer.api.api_tools import *
from Chat_bot_Software_Engineer.api.settings import contact_info

#Long response
customer_service = f"I'm affraid im not as smart as I though but surely one of our customer service employees is it.\nHere is their contact info {contact_info} they will be happy to support you. "

#Delivery Response
def delivery_response(merchant_id):

    #get id sale from SQL
    id_sale = get_sale_id_SQL(merchant_id)

    #get info from tracking API
    tracking_info = generate_sale_tracking_info(id_sale)

    #get info zip code API
    zip_code = tracking_info.get("destination_zip_code")
    zip_code_info = generate_sale_zip_info(zip_code)

    #variables
    delivery_forecast = tracking_info.get('delivery_forecast')
    order_status = tracking_info.get('status')
    neighborhood = zip_code_info.get('neighborhood')
    city = zip_code_info.get('city')
    street = zip_code_info.get('street')
    state = zip_code_info.get('state')
    complement = zip_code_info.get('complement')
    pass



def unknown():
    response = ["I'm affraid I did not understand your message.\nCould you re-phrase that, please? ",
                "Could you be more specific with your request?",
                "Could you give me only key words that define your problem?"][random.randrange(3)]

    return response
