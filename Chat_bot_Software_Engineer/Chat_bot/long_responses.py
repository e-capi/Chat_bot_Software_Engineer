import imp
import random
from Chat_bot_Software_Engineer.api.settings import contact_info

#Long response
customer_service = f"I'm affraid im not as smart as I though but surely one of our customer service employees is it.\nHere is their contact info {contact_info} they will be happy to support you. "



def unknown():
    response = ["I'm affraid I did not understand your message.\nCould you re-phrase that, please? ",
                "Could you be more specific with your request?",
                "Could you give me only key words that define your problem?"][random.randrange(3)]

    return response
