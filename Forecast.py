"""
天气预报模块
"""
import requests
import json
import time


def forecast(city):
    url = r'http://apis.juhe.cn/simpleWeather/query'
    key = '61c76a1ea1989045573b9dc0f4a352dc'

    url = url + '?city=' + city + '&key=' + key

    r = requests.get(url)
    response = json.loads(r.text)
    temperature = response['result']['realtime']['temperature']
    humidity = response['result']['realtime']['humidity']
    info = response['result']['realtime']['info']
    api = response['result']['realtime']['aqi']
    time_info = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    forecast_info = '现在时间是:' + time_info + '\n' \
                    + city + '今日的天气' + info + '\n' \
                    + '温度为' + temperature + '\n'\
                    + '湿度为' + humidity + '\n' \
                    + '空气质量指数为' + api
    return forecast_info


if __name__ == "__main__":
    print(forecast('珠海'))
