"""
通用文字识别
"""
import requests


def pic_to_word(urls):
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=XMntwgKcwzsuuLUIqhBWw9uZ' \
           '&client_secret=iWESOZKlmB5vw3hL5T3MniNTdZCfAgL4 '
    response = requests.get(host)
    access_token = response.json()['access_token']

    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"

    params = {"url": urls}

    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)

    text = response.json()
    str_num = ''
    for i in range(0, text['words_result_num']):
        str_num = str_num + str(text['words_result'][i]['words']) + '\n'
    return str_num


if __name__ == '__main__':
    url = r'http://gchat.qpic.cn/gchatpic_new/467162434/3979142650-2310638436-9E131913C2010DF26960DF711C8F42BE/0?term=2'
    pic_to_word(url)
