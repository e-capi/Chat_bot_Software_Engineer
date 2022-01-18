from Chat_bot_Software_Engineer.api.api_tools import *

#TBU when the bot can treat severall requests simoultaneously

def responses_pipeline():
    active_chats = generate_act_convs_list()
    subject_list = []
#     while len(active_chats) > 0:
    for chat in list(active_chats): #parse all the active chats
        #parse all the active messages in a conversation
        messages = generate_info_of_conv(chat, 'messages')
        for message in list(messages):

            #generate the subject of the problem and give it to the bot AI
            subject = generate_info_of_conv(chat,'subject')
            subject_list.append(subject)
            messages.remove(message)


        active_chats.remove(chat)
    return subject_list

#on Develop

def responses_pipeline_v2():
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
