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
