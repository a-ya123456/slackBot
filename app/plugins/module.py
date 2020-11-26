from slackbot.bot import listen_to
from slackbot.bot import respond_to
from plugins import filewriter


target_users = ['c0118010b9']
target_channels = ['bot作成']

@listen_to('^(.*)$')
def comment_log(message,text):
    real_name = message.user['real_name']
    display_name = message.user['profile']['display_name']
    channel = message.channel._body['name']
    if real_name not in target_users:
        return
    if channel not in target_channels:
        return
    f = filewriter.FileReadWrite()
    action = f.file_write("./logs/test.txt", text)
    message.react(action)
    message.send(text)


@respond_to('^(.*)$')
def comment_log2(message,text,):
    message.send(text)