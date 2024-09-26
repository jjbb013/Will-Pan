# - * - coding: utf - 8 -*-
import json
import requests
import pandas as pd
#1，根据CSV文件种的行列索引名称查找对应产品的链接，参数为设备种类，App，和酒的名称。
def get_links_from_csv(device,app,goods):
    df = pd.read_csv(f'{device}_links.csv',index_col=device)
    result = df.loc[[goods],[app]]
    link = result.to_json(orient="split",force_ascii=False)
    link = json.loads(link)
    link = link['data'][0][0]
    return link
#2,根据信息内容包含的关键词来确定提供哪个链接，参数为原始信息，返回正确的链接。
def get_good_link(message):
    device = ['iOS','安卓']
    app_list = ['京东','淘宝','国美']
    goods_list = ['飞天','虎年']
    for goods in goods_list:
        if goods in message:
            for app in app_list:
                if goods and app in message:
                    link = get_links_from_csv(device, app, goods)
                    if link:
                        return link

if __name__ == '__main__':
    message = '淘宝自营 茅台53度虎年生肖酱香型白酒500ml'
    link = get_good_link(message)
    print(link)
    a = requests.get(url='https://api2.pushdeer.com/message/push?pushkey=PDU12755Tu0SDBH9FWXziMYXB6idL4F8RTNeJbQcq&text='+link)
    print(a)