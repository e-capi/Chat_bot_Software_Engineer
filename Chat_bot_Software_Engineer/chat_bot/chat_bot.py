import re
from Chat_bot_Software_Engineer.chat_bot.chat_tools import  responses_pipeline, send_response, response_api_status
from Chat_bot_Software_Engineer.chat_bot import long_responses as long
import string



def message_probability(user_message, recognised_words, single_response=False, required_words=[]):

    message_certainty = 0
    has_required_words = True

    # count the words per message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    #calculate the percentage of words that are recognised
    percentage = float(message_certainty) / float(len(recognised_words))

    #check that words are in string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response = False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

#-----------------------------------Responses--------------------------------
    #Basic responses
    response('Greetings!', ['hello','hi','hola', 'oi', 'greetings','hey'], single_response=True) #first answer to the message
    response("I'm doing fine, and you?", ['how', 'are', 'you', 'doing'], required_words=['how'])

    #Long responses
    response(long.customer_service, ['customer', 'service', 'human', 'help', 'advice', 'contact', 'info'], required_words=[])

    #--Coded responses delivery reponse missing merchant id--
    response(long.delivery_response(merchant_id), ['delivery', 'forecast', 'late', 'check', 'address'], required_words=['delivery'])
    response(long.receipt_response(merchant_id), ['bank', 'account', 'receipt', 'problem'], required_words=['receipt'])
    response(long.connection_response(merchant_id), ['connection', 'problem'], required_words=['connection'])


    best_match = max(highest_prob_list, key=highest_prob_list.get)

    #Debugging
    #print(highest_prob_list)
    #print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')
    #print(message)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


#Clean the user input and create a list of words
def get_response(user_input):

    #with regex:
    #split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    #response = check_all_messages(split_message)

    #without regex:
    message_remove_punctuantion = user_input.translate(str.maketrans("","", string.punctuation))
    list_of_words_to_analyze = message_remove_punctuantion.split()

    response = check_all_messages(list_of_words_to_analyze)
    return response



#generate all the active conversations that need a response
list_of_all_active_messages = responses_pipeline()


#list_of_responses_info = [] uncomment when a valid bot email and support email is added to the settings variables


#For every single conversation answer all the user message, when finish go to next conversation
for message in list_of_all_active_messages:

    merchant_id = message.get('merchant_id')
    subject = message.get('subject')
    conversation_id = message.get('conversation_id')

    #final response sent to the API
    final_response = send_response(conversation_id, get_response(subject))

    #---- TB uncommented along with list_of_responses_info
    #This function sends and email to our IT team if there's a problem when sending the final_response to the API
    #function is comment due to the lack of an email to do this with. Yet its a functional function
    #response_api_status(list_of_responses_info)
    #----

    print(final_response)

#Use to test normal bot answers such as: Hello, how are you ?
while True:
    print('Bot: ' + get_response(input('You: ')))
