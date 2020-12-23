from slackbot.bot import listen_to
from slackbot.bot import respond_to
from plugins import filewriter


target_users = ['c0118010b9']
target_channels = ['bot作成']

#@listen_to('^[\s\S]*.$')
@default_reply()
def comment_log(message):
    #messageから抜き出して変数へ格納
    real_name = message.user['real_name']
    display_name = message.user['profile']['display_name']
    channel = message.channel._body['name']
    text = message.body['text']
    #target以外は記録しない
    if real_name not in target_users:
        return
    if channel not in target_channels:
        return

    f = filewriter.FileReadWrite()
    action = f.file_write("./logs/test.txt", text)
    message.react(action)
    message.send(text)


@respond_to('^[\s\S]*.$')
def comment_log2(message):
    text = message.body['text']
    message.react('ok')
    print(text)
    message.send(text)