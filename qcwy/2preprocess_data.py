
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import os
from tqdm import tqdm


# In[2]:

#合并所有文件
input_base_path = "./data/"
outputfile = "all_data.tsv"
data_columns = ""
for inputfile in tqdm(os.listdir(input_base_path)):
    data = pd.read_csv(input_base_path+inputfile, sep='\t')
    data_columns = data.columns
    data.to_csv(outputfile, sep='\t',mode='a', index=False, header=False)

data = pd.read_csv(outputfile,sep='\t')
data.columns = data_columns
data.to_csv(outputfile, sep='\t',index=False)


# In[3]:

#对数据进行处理
#删除空行
print(len(data))
data = data.dropna(axis=0)
print(len(data))

#把none的位置补为无
data = data.fillna("无")


# In[4]:

outputfile = "all_data.tsv"
data = pd.read_csv(outputfile,sep='\t')
#根据需求进行统计并绘图
print(len(data))
data = data.dropna(axis=0)
print(len(data))

#把none的位置补为无
data = data.fillna("无")


# In[5]:

#一线城市5个：北京、上海、广州、深圳
bj_num = len(data[data["city"]=="北京"])
sh_num = len(data[data["city"]=="上海"])
gz_num = len(data[data["city"]=="广州"])
sz_num = len(data[data["city"]=="深圳"])
print(bj_num,sh_num,gz_num,sz_num)

#二线发达城市8个：杭州、南京、济南、青岛
hz_num = len(data[data["city"]=="杭州"])
nj_num = len(data[data["city"]=="南京"])
jn_num = len(data[data["city"]=="济南"])
qd_num = len(data[data["city"]=="青岛"])
print(hz_num,nj_num,jn_num,qd_num)

#三线城市：乌鲁木齐、贵阳、海口、兰州
wlmq_num = len(data[data["city"]=="乌鲁木齐"])
gy_num = len(data[data["city"]=="贵阳"])
hk_num = len(data[data["city"]=="海口"])
lz_num = len(data[data["city"]=="兰州"])
print(wlmq_num,gy_num,hk_num,lz_num)


# In[6]:

'''
一线城市5个：北京、上海、广州、深圳、天津

二线城市：杭州、南京、济南、重庆、青岛、大连、宁波、厦门、成都、武汉、哈尔滨、沈阳、西安、长春、长沙、福州、郑州、石家庄、苏州、佛山、东莞、无锡、烟台、太原、合肥、南昌、南宁、昆明、温州、淄博、唐山

三线城市：乌鲁木齐、贵阳、海口、兰州、银川、西宁、呼和浩特、泉州、包头、南通、大庆、徐州、潍坊、常州、鄂尔多斯、绍兴、济宁、盐城、邯郸、临沂、洛阳、东营、扬州、台州、嘉兴、沧州、榆林、泰州、镇江、昆山、江阴、张家港、义乌、金华、保定、吉林、鞍山、泰安、宜昌、襄阳、中山、惠州、南阳、威海、德州、岳阳、聊城、常德、漳州、滨州、茂名、淮安、江门、芜湖、湛江、廊坊、菏泽、柳州、宝鸡、珠海、绵阳
横坐标是职位，纵坐标是职位的数量
'''

one_city = "北京、上海、广州、深圳、天津".split("、")
two_city = "杭州、南京、济南、重庆、青岛、大连、宁波、厦门、成都、武汉、哈尔滨、沈阳、西安、长春、长沙、福州、郑州、石家庄、苏州、佛山、东莞、无锡、烟台、太原、合肥、南昌、南宁、昆明、温州、淄博、唐山".split("、")
three_city = "乌鲁木齐、贵阳、海口、兰州、银川、西宁、呼和浩特、泉州、包头、南通、大庆、徐州、潍坊、常州、鄂尔多斯、绍兴、济宁、盐城、邯郸、临沂、洛阳、东营、扬州、台州、嘉兴、沧州、榆林、泰州、镇江、昆山、江阴、张家港、义乌、金华、保定、吉林、鞍山、泰安、宜昌、襄阳、中山、惠州、南阳、威海、德州、岳阳、聊城、常德、漳州、滨州、茂名、淮安、江门、芜湖、湛江、廊坊、菏泽、柳州、宝鸡、珠海、绵阳".split("、")

print("一二三线城市对应的数量：",len(one_city),len(two_city),len(three_city))

one_city_data = data[data['city'].isin(one_city)]
two_city_data = data[data['city'].isin(two_city)]
three_city_data = data[data['city'].isin(three_city)]

print("根据一二三线城市名字筛选的数据",len(one_city_data),len(two_city_data),len(three_city_data))
#对职位和数量进行筛选，首先获得所有的职位，然后获取职位对应的数量
one_position_name_list = list(one_city_data['position_name'].unique())
two_position_name_list = list(two_city_data['position_name'].unique())
three_position_name_list = list(three_city_data['position_name'].unique())

print("职位数量：",len(one_position_name_list),len(two_position_name_list),len(three_position_name_list))

one_position_name_num = list()
for item in one_position_name_list:
    num = len(one_city_data[one_city_data["position_name"]==item])
    one_position_name_num.append(num)
    
two_position_name_num = list()
for item in two_position_name_list:
    num = len(two_city_data[two_city_data["position_name"]==item])
    two_position_name_num.append(num)
    
three_position_name_num = list()
for item in three_position_name_list:
    num = len(three_city_data[three_city_data["position_name"]==item])
    three_position_name_num.append(num)
    
print("职位对应数量:",len(one_position_name_num),len(two_position_name_num),len(three_position_name_num))


# In[8]:

#输入一个字符串，返回一个两个值
def transfer_salary(item):
    if("千" in item):
        item_list = item.split("千")
        if('-' in item_list[0]):
            money = item_list[0].split("-")
            return float(money[0])*1000,float(money[1])*1000
        else:
            money = item_list[0]
            return float(money)*1000,float(money)*1000
    if("万" in item):
        item_list = item.split("万")
        if('-' in item_list[0]):
            money = item_list[0].split("-")
            if("年" in item_list[1]):
                return float(money[0])*10000/12,float(money[1])*10000/12
            else:
                return float(money[0])*10000,float(money[1])*10000
        else:
            money = item_list[0]
            if("年" in item_list[1]):
                return float(money)*10000/12,float(money)*10000/12
            else:
                return float(money)*10000,float(money)*10000
        
    if("元" in item):
        item_list = item.split("元")
        money = item_list[0]
        if("天" in item_list[1]):
            return float(money)*24,float(money)*24
        else:
            return float(money)*8*24,float(money)*8*24
    return 3000,3000
        


# In[ ]:




# In[9]:

#全国信息分析
#薪资归并
salary = data['salary']
min_salary = list()
max_salary = list()
for item in salary:
    min_d,max_d = transfer_salary(item)
    min_salary.append(min_d)
    max_salary.append(max_d)
data['min_salary'] = min_salary
data['max_salary'] = max_salary

#工作经验归并
print(data['experience'].unique())

#学历归并
education_list = list()
for item in data['education']:
    if("人" in item):
        education_list.append("不限")
    else:
        education_list.append(item)
data['education'] = education_list
print(data['education'].unique())
#公司规模归并
print(data["company_proportion"].unique())

#公司类型
print(data["company_type"].unique())



# In[10]:

#保存归并后的文件
data.to_csv("last_all_data.tsv",sep='\t',index = False)


# In[ ]:



