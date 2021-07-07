from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage ,StickerSendMessage ,FollowEvent ,UnfollowEvent
)
app = Flask(__name__)
channel_token = "n0uv+rM5NDYaHqxixZQ/jAJ00RAzIQDf6I6KBNodbaXNX1xC17gxtKmfsZyVe/FVhFbLiSqKzuiClDdrJGbiggFad7tHP77dLj2n91oGpFHjTreFx71fQgzcG2voeNhoWP0jQBKffE0PzoRyPFvPJgdB04t89/1O/w1cDnyilFU="
channel_secret = '2041b308a40dd1e7d24bb7e457c6cf58'
line_bot_api = LineBotApi(channel_token)
handler = WebhookHandler(channel_secret)

@app.route("/callback",method=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    ## handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage) #當收到信息事件(文字訊息)
def handle_message(event):
    #line_bot_api.reply_message(event.reply_token,text= event.message.text) #重複訊息
    message_text = str(event.message.text).lower() #將回應訊息轉成小寫str
    if message_text in ['i am ready to order.', 'add']: #如果有得到訊息
        message = TextSendMessage(text='list products') #將想傳的訊息存到message
    if message:   #如果有收到，回應出去
        line_bot_api.reply_message(
            event.reply_token,
            message)
if __name__=="__main__":
    app.run()