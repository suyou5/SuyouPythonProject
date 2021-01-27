"""
格力机器人
"""
from GreeMessage import GreeMessage
from BaiduTran import translation
import time


class GreeBot(object):
    """
    格力机器人
    """

    def __init__(self):
        self.message = GreeMessage()

    def run(self):
        """
        循环
        :return:
        """
        _, last_msgId = self.message.get_message()
        while True:
            content, msgId = self.message.get_message()
            if msgId != last_msgId:
                time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print(time_str + content)
                last_msgId = msgId
                if ':tr' in content:
                    dst = translation(content[3:])
                    print(dst)
                    last_msgId = self.message.send_message(dst)

            time.sleep(1)


bot = GreeBot()
bot.run()
