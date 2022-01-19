#API root and auth
sale_id_api = 'https://logistics-api-dot-active-thunder-329100.rj.r.appspot.com'
chip_api = 'https://telecom-api-dot-active-thunder-329100.rj.r.appspot.com'
conversations_api = 'https://chats-api-dot-active-thunder-329100.rj.r.appspot.com'
header = {'authorization': 'teste'} #auth code

#HTTP Requests
#   Sale API
HTTP_request_sale_track = '/tracking'
HTTP_request_sale_zip = '/zip_code'
#   Chip Api
HTTP_request_chip = '/chip_status'
#   Conversation API
HTTP_request_conversation = '/conversations'
HTTP_request_conversation_info = '/conversation_info'
    #send response
HTTP_send_conversation = '/send_message'

#Customer contact info
contact_info = 'customer_service@help.br'

#e_mail generation info
    #TB swaped for valable emails then uncomment the function on chat_bot.py
bot_email= 'e-capi_bot@email.com'
support_email = 'IT_support@team.com'
