import json
import requests
import pandas as pd
import pprint
#1，根据CSV文件种的行列索引名称查找对应产品的链接，参数为设备种类，App，和酒的名称。
df = pd.read_excel('userlist.xlsx','userlist',index_col='name')
pd.set_option('display.width', 280) # 设置打印宽度(**重要**)

def get_city_list():
    city_info = df['i茅台']
    city_list = city_info.to_list()
    for num,item in enumerate(city_list):
        if isinstance(item,str):
            if item.__contains__(','):
                del city_list[num]
                new = item.split(',')
                city_list.extend(new)
        else:
            del city_list[num]
    city_list = list(set(city_list))
    return city_list


def get_push_dict(app,city):
    push_info = df.loc[df[app] == city, ['bark','pushdeer','wxpusher']]
    push_dict = json.loads(push_info.to_json(orient="records",force_ascii=False))
    print(push_info.to_string())
    return push_dict


message = '上海市黄浦区中华路贵州茅台自营店'
city_list = get_city_list()[1:]
print(city_list)

for city in city_list:
    if message.__contains__(city):
        print(get_push_dict('i茅台',city))

# json_list = df.to_json(orient="records",force_ascii=False)
# a = json.loads(json_list)[-16]['area']
# print(a)
# list = []
# a = a.split(',')
# print(a)
