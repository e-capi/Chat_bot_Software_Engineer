from api.api_tools import generate_act_conv_info

#TBU when the bot can treat severall requests simoultaneously
active_chats_list = generate_act_conv_info()
number_of_active_chats = len(active_chats_list)
