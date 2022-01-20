# 🤖Chat_bot_Software_Engineer
- **Description:** Chat bot that analysis the user input and retrieve relevant information from different **API's/SQL database** to propose an  accurate solution to the user demand
- **Data Source:** API's & SQL database

# About the project
There are several chatbots out there. Some of them, very smart due to the usage of *RNN* and *BRNN* machine learning algorithms that enhance the learnig curve of the chat-bot thanks to their interactions with users on a daily basis, making them smarter in time. But also, we can find chat-bots less smart than that: default answers and not knowing how to interact in many cases are some of their characteristics.

Here you will find a usefull chat-bot that brings the best of both worlds for those developpers that aren't experience enough yet, to deal with all of those data science libraries.

A smart enough bot that will deal with your users demands on an accurate way.

Last but not least this chat-bot is designed for those who have their user information stored in a SQL database and/or an API('s).

# 👨‍💻Project Description

*Listed below the main components of this project and their description:*

## chat_bot
- **chat_bot.py:** *chat_bot* bring together all the components of this project to analyze the user request and propose an accurate response to the user.
- **chat_tools.py:** Holds the functions needed to handle multiple users and demands at a time with a conversation + message pipeline approach.
- **long_responses.py:** This section store the functions that can be use to generate a response to the user depending on the text analyzed on *chat_bot*. For this particular use case there are 3 main answer types:
    - **Connection problem**
    - **Delivery problem**
    - **Receipt problem**

In addition there is a **unknown()** function which is used to ask for reformulated question when the bot didn't understand the user need.

## API
- **settings.py:** Stores the API's urls, HTTPS requests and support e-mails of your organization.
- **api_tools.py:** Have all the functions related with your API's in order to retrieve the necessary information to fill the responses functions on <code>/chat_bot.chat_tools.</code>

## SQL
- **SQL_tools.py:** Functions to retrieve from a SQL database users information. This section is dependant from the *api_tools*.

## Data
- **simulation-db:** stores the SQL database *(alter solution is to store it in GCP)*.

# 🚀 Startup the project


# Install

Go to `https://github.com/e-capi/Chat_bot_Software_Engineer` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:e-capi/Chat_bot_Software_Engineer.git
cd Chat_bot_Software_Engineer
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
Chat_bot_Software_Engineer-run
```
