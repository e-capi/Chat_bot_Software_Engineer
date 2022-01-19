from Chat_bot_Software_Engineer.api.api_tools import *
import smtplib

def responses_pipeline():
    active_chats = generate_act_convs_list()
    list_of_problems = []

    for conversation_id in list(active_chats):

        #give info for every all messages
        messages = generate_info_of_conv(conversation_id, 'messages') #messages of one conversation

        for message in list(messages):


            merchant_id = generate_info_of_conv(conversation_id,'merchant_id')
            subject = generate_info_of_conv(conversation_id, 'subject')

            features_pipeline = {'conversation_id': conversation_id, 'merchant_id': merchant_id, 'subject': subject}

            #create a list to parse on chatbot.py
            list_of_problems.append(features_pipeline)
            messages.remove(message)

        # {'conversation_id': chat_id, 'merchant_id':}
    return list_of_problems


#send response to API

def send_response(conversation_id, response_message):
    send_email_to_IT_team_Airflow = 'Place Holder of function Send_response API unreachable'

    try:
        response_to_client = send_response_api(conversation_id, response_message)
    except:
        return send_email_to_IT_team_Airflow

    return response_to_client

#Functions for sending email to IT support team when responses can't be send through the send_response API

def email_support(email_content):

    sender_email = bot_email
    rec_email = support_email
    password = 'bot_pass123'
    message = email_content

    #Login to bot email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email,password)

    #send message
    server.sendmail(sender_email, rec_email, message)
    return f'Email has been sent to {rec_email}'


def response_api_status(list_of_responses):
    email_sent = []
    for response_info in list_of_responses:
        sent = response_info.get('sent')
        description = response_info.get('description')

        if sent != 'true' or description != 'OK':
            email_support(email_content=response_info)
            email_sent.append(response_info.get('conversation_id'))

    if len(email_sent) < 1:
        return "No errors encountered, no emails where sent"
    else:
        return f"emails where sent to {email_sent}"
