"""
给G平台发消息
"""
import requests
import json


class GreeMessage(object):
    """
    格力G平台收发消息
    """

    def __init__(self):
        self.header = {
            'Host': 'yun1.gree.com',
            'Connection': 'keep-alive',
            'Content-Length': '178',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.48',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://yun1.gree.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://yun1.gree.com/im/xiaoxi',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cookie': 'JSESSIONID=1ppnznzisu60g1jysqzg9kr26k; rHxW_6157__did_=49B9233DADBB6AA0466FB380D46B510E; '
                      '_ga=GA1.2.1986805778.1600915411; '
                      'rm'
                      '=ODMzYTk3NjctZDBiNS0xMWVhLThiM2ItMDA1MDU2YWY0NDJkOmY1NzM0NTA3ZGFkZDczZmE0NWQ0Zjc2NjgyMjBhOTYx; '
                      'at=aaee155a-05ee-48fc-9492-a5cc78e03621; cu=833a9767-d0b5-11ea-8b3b-005056af442d; '
                      'webLappToken=\"RTXcirUwxXfTZ8dMGKeE%2B9VREXlmeLaq2rwxTnRUKaeYKlzmZM0BUvtQFRpcMKY4HlJ%2FULry'
                      '%2BsbDFbpkKUTXDdM%2FJfa6duBK\"; cd=yun1.gree.com; cn=102; sync_networkid=102; '
                      'sync_userid=833a9767-d0b5-11ea-8b3b-005056af442d '
        }

    def send_message(self, content):
        """
        给G平台上的文件传输助手发送消息
        :param content:
        :return:
        """
        sendMessageUrl = r'https://yun1.gree.com/im/web/sendMessage.do'
        sendMessageForm = {
            'groupId': '',
            'toUserId': 'XT-0060b6fb-b5e9-4764-a36d-e3be66276586',
            'msgType': '2',
            'content': content,
            'msgLen': 4,
            'param': '{\"notifyType\": 1, \"notifyTo": [], \"notifyToAll\": false}',
        }
        r = requests.post(sendMessageUrl, data=sendMessageForm, headers=self.header, verify=True)

        return r.text

    def get_message(self):
        """
        获取格力G平台上文件传输助手的最后一条消息
        :return:
        """
        listMessageUrl = r'https://yun1.gree.com/im/web/listMessage.do'

        getMessageForm = {
            'groupId': '833a43fb-d0b5-11ea-8b3b-005056af442d-XT-0060b6fb-b5e9-4764-a36d-e3be66276586',
            'type': 'new',
            'count': '1',
            'msgId': '',
        }

        r = requests.post(listMessageUrl, data=getMessageForm, headers=self.header, verify=True)
        response = json.loads(r.text)
        try:
            content = response['data']['list'][0]['content']
            msgId = response['data']['list'][0]['msgId']
        except TypeError:
            print(r.text)
            return "接收信息发生了错误", "0"
        return content, msgId


if __name__ == '__main__':
    msg = GreeMessage()
    text = msg.send_message("6666")
    print(text)
    text2 = msg.get_message()
    print(text)
