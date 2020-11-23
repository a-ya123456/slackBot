from slackbot.bot import listen_to
from slackbot.bot import respond_to

target_users = ['c0118010b9']

@listen_to('^(.*)$')
def comment_log(message,text):
    real_name = message.user['real_name']
    display_name = message.user['profile']['display_name']
    if real_name not in target_users :
        return
    message.send(text)
    message.react('ok')


@respond_to('^(.*)$')
def comment_log2(message,text,):
    message.send(text)