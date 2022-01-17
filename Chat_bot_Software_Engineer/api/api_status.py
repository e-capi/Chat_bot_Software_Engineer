from Chat_bot_Software_Engineer.api.api_tools import *

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
