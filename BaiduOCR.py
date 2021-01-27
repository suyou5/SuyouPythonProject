# encoding:utf-8

from aip import AipOcr


def pic_to_word(urls):
    APP_ID = '16459310'
    API_KEY = 'XMntwgKcwzsuuLUIqhBWw9uZ'
    SECRET_KEY = 'iWESOZKlmB5vw3hL5T3MniNTdZCfAgL4'

    # options = {"language_type": type}
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    """ 带参数调用通用文字识别, 图片参数为远程url图片 """
    text = client.basicGeneralUrl(urls)
    print(text)
    str_num = ''
    for i in range(0, text['words_result_num']):
        str_num = str_num + str(text['words_result'][i]['words']) + '\n'
    return str_num


if __name__ == '__main__':
    url = r'http://gchat.qpic.cn/gchatpic_new/467162434/3979142650-3143846778-4A4C5359B3070EC644D2F8E6D634D8C8/0?term=2'
    pic_to_word(url)
