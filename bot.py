import asyncio

from graia.application import GraiaMiraiApplication, Session
from graia.application.friend import Friend
from graia.application.group import Group
from graia.application.message.chain import MessageChain
from graia.application.message.elements.internal import Plain
from graia.broadcast import Broadcast

from BaiduOCRApi import pic_to_word
from BaiduTran import translation
from Forecast import forecast

loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://localhost:8080",  # 填入 http api 服务运行的地址
        authKey="graia-mirai-api-http-authkey",  # 填入 authKey
        account=349093405,  # 你的机器人的 qq 号
        websocket=True  # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)


@bcc.receiver("FriendMessage")
async def friend_message_listener(app: GraiaMiraiApplication, friend: Friend):
    print(friend)
    await app.sendFriendMessage(friend, MessageChain.create([
        Plain("Hello, World!")
    ]))


@bcc.receiver("GroupMessage")
async def friend_message_listener(message: MessageChain, app: GraiaMiraiApplication, group: Group):
    print(message.__root__)  # 字符串在[1], 时间信息在[0], 图像在[2], 如果只有图像没有图片,则图像在[1]
    if ':tr' in message.__root__[1].asDisplay():
        dst = translation(message.__root__[1].asDisplay()[3:])
        print(dst)
        await app.sendGroupMessage(group, MessageChain.create([Plain(dst)]))
    elif ':ocr' in message.__root__[1].asDisplay():
        url = message.__root__[2].url
        dst = pic_to_word(url)
        print(dst)
        await app.sendGroupMessage(group, MessageChain.create([Plain(dst)]))
    elif ':weather' in message.__root__[1].asDisplay():
        weather_info = forecast(message.__root__[1].asDisplay()[8:])
        print(weather_info)
        await app.sendGroupMessage(group, MessageChain.create([Plain(weather_info)]))
    elif message.__root__[1].asDisplay() == '晚安':
        await app.sendGroupMessage(group, MessageChain.create([Plain("晚安 小可爱")]))


app.launch_blocking()
