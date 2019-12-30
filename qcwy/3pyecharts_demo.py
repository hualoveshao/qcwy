
# coding: utf-8

# In[47]:

from pyecharts import *
from snapshot_phantomjs import snapshot as driver
import pandas as pd
import numpy as np


# In[48]:

data = pd.read_csv("last_all_data.tsv",sep='\t')


# In[49]:

#根据需求绘制图形并保存
#功能1：一二三线城市物联网专业招聘数量
#一线城市5个：北京、上海、广州、深圳
bj_num = len(data[data["city"]=="北京"])
sh_num = len(data[data["city"]=="上海"])
gz_num = len(data[data["city"]=="广州"])
sz_num = len(data[data["city"]=="深圳"])
print(bj_num,sh_num,gz_num,sz_num)

columns = ["深圳","上海","广州","北京"] 
data1 = [sz_num,sh_num,gz_num,bj_num] 

bar = Bar("柱状图", "一线城市物联网专业招聘数量")
bar.add("职位数量", columns, data1, mark_line=["average"], mark_point=["max", "min"]) 
# make_snapshot(driver, bar.render(), "bar.html")
bar.render(path='./picture/one_city_positoin_num.html')

bar.render()

#二线发达城市：杭州、南京、济南、青岛
hz_num = len(data[data["city"]=="杭州"])
nj_num = len(data[data["city"]=="南京"])
jn_num = len(data[data["city"]=="济南"])
qd_num = len(data[data["city"]=="青岛"])
print(hz_num,nj_num,jn_num,qd_num)


columns = ["杭州","南京","济南","青岛"] 
data1 = [hz_num,nj_num,jn_num,qd_num] 
bar = Bar("柱状图", "二线城市物联网专业招聘数量")
bar.add("职位数量", columns, data1, mark_line=["average"], mark_point=["max", "min"]) 
# make_snapshot(driver, bar.render(), "bar.html")
bar.render(path='./picture/two_city_positoin_num.html') 

#三线城市：乌鲁木齐、贵阳、海口、兰州
wlmq_num = len(data[data["city"]=="乌鲁木齐"])
gy_num = len(data[data["city"]=="贵阳"])
hk_num = len(data[data["city"]=="海口"])
lz_num = len(data[data["city"]=="兰州"])
print(wlmq_num,gy_num,hk_num,lz_num)

columns = ["乌鲁木齐","贵阳","海口","兰州"] 
data1 = [wlmq_num,gy_num,hk_num,lz_num] 
bar = Bar("柱状图", "三线城市物联网专业招聘数量")
bar.add("职位数量", columns, data1, mark_line=["average"], mark_point=["max", "min"]) 
# make_snapshot(driver, bar.render(), "bar.html")
bar.render(path='./picture/three_city_positoin_num.html') 


# In[50]:

#功能2 全国，最低和最高薪资分析

def min_max_salary(pic_name,info,tmp_data=data,city="全国",education="所有学历"):
    if(city!="全国"):
        tmp_data = tmp_data[tmp_data["city"]==city]
        
    if(education!="所有学历"):
        tmp_data = tmp_data[tmp_data['education']==education]

    min_salary = tmp_data['min_salary']
    max_salary = tmp_data['max_salary']

    min_salary_map = {"三千以下":0,"三千到五千":0,"五千到八千":0,"八千到一万":0,"一万到两万":0,"两万以上":0}
    max_salary_map = {"三千以下":0,"三千到五千":0,"五千到八千":0,"八千到一万":0,"一万到两万":0,"两万以上":0}

    for item in min_salary:
        if(item<3000):
            min_salary_map["三千以下"] = min_salary_map["三千以下"]+1
        elif(item<5000):
            min_salary_map["三千到五千"] = min_salary_map["三千到五千"]+1
        elif(item<8000):
            min_salary_map["五千到八千"] = min_salary_map["五千到八千"]+1
        elif(item<10000):
            min_salary_map["八千到一万"] = min_salary_map["八千到一万"]+1
        elif(item<20000):
            min_salary_map["一万到两万"] = min_salary_map["一万到两万"]+1
        else:
            min_salary_map["两万以上"] = min_salary_map["两万以上"]+1

    for item in max_salary:
        if(item<3000):
            max_salary_map["三千以下"] = max_salary_map["三千以下"]+1
        elif(item<5000):
            max_salary_map["三千到五千"] = max_salary_map["三千到五千"]+1
        elif(item<8000):
            max_salary_map["五千到八千"] = max_salary_map["五千到八千"]+1
        elif(item<10000):
            max_salary_map["八千到一万"] = max_salary_map["八千到一万"]+1
        elif(item<20000):
            max_salary_map["一万到两万"] = max_salary_map["一万到两万"]+1
        else:
            max_salary_map["两万以上"] = max_salary_map["两万以上"]+1

    columns = ["三千以下","三千到五千","五千到八千","八千到一万","一万到两万","两万以上"] 
    data1 = [min_salary_map[item] for item in columns]
    data2 = [max_salary_map[item] for item in columns]

    bar = Bar("柱状图", info+"薪资情况")
    bar.add(info+"最低薪资数量", columns, data1, mark_line=["average"], mark_point=["max", "min"]) 
    # make_snapshot(driver, bar.render(), "bar.html")
    bar.render(path='./picture/'+pic_name+'_min_salary.html') 

    bar = Bar("柱状图", info+"薪资情况")
    bar.add(info+"最高薪资数量", columns, data2, mark_line=["average"], mark_point=["max", "min"]) 
    # make_snapshot(driver, bar.render(), "bar.html")
    bar.render(path='./picture/'+pic_name+'_max_salary.html') 
    
min_max_salary("nationwide","全国")


# In[51]:

#功能3 全国工作经验要求
experience_list = data['experience'].unique()
experience_list_num = [len(data[data["experience"]==item]) for item in experience_list]
# print(experience_list,experience_list_num)
#饼图

pie = Pie("经验要求")
pie.add(
    "",
    experience_list,
    experience_list_num,
    is_label_show=True,
    is_more_utils=True,
    legend_orient="vertical",
    legend_pos="right",
)
pie.render(path='./picture/nationwide_experience.html') 


# In[52]:

#功能4 全国学历要求
education_list = data['education'].unique()
education_list_num = [len(data[data["education"]==item]) for item in education_list]
# print(experience_list,experience_list_num)
#饼图

pie = Funnel("学历要求")
pie.add(
    "",
    education_list,
    education_list_num,
    is_label_show=True,
    is_more_utils=True,
    legend_orient="vertical",
    legend_pos="right",
)
pie.render(path='./picture/nationwide_education.html') 


# In[53]:

#功能5 全国公司规模
experience_list = data['company_proportion'].unique()
experience_list_num = [len(data[data["company_proportion"]==item]) for item in experience_list]
# print(experience_list,experience_list_num)
#饼图

pie = Pie("全国公司规模")
pie.add(
    "",
    experience_list,
    experience_list_num,
    is_label_show=True,
    is_more_utils=True
)
pie.render(path='./picture/nationwide_company_proportion.html') 


# In[ ]:

#功能6 全国公司类型
experience_list = data['company_type'].unique()
experience_list_num = [len(data[data["company_type"]==item]) for item in experience_list]
# print(experience_list,experience_list_num)
#饼图

pie = Pie("全国公司类型")
pie.add(
    "",
    experience_list,
    experience_list_num,
    is_label_show=True,
    is_more_utils=True,
    legend_orient="vertical",
    legend_pos="right",
)
pie.render(path='./picture/nationwide_company_type.html') 


# In[ ]:

#功能7 以全国为例面向大专生薪资范围
min_max_salary("nationwide_college_student","全国大专生",data,"全国","大专")


#以全国为例 面向本科生薪资范围
min_max_salary("nationwide_undergraduate","全国本科生",data,"全国","本科")


# In[ ]:

#功能8 苏州大专和本科薪资
min_max_salary("suzhou_college_student","苏州大专生",data,"苏州","大专")


#以全国为例 面向本科生薪资范围
min_max_salary("suzhou_undergraduate","苏州本科生",data,"苏州","本科")


# In[ ]:

#功能9 苏州工作经验要求
suzhou_data = data[data['city']=="苏州"]
experience_list = suzhou_data['experience'].unique()
experience_list_num = [len(suzhou_data[suzhou_data["experience"]==item]) for item in experience_list]

radar = Radar("雷达图", "苏州工作经验要求") 
print(experience_list)
print(experience_list_num)
experience_list = [(item,80) for item in experience_list]
print(experience_list)

radar.config(experience_list) 
radar.add("苏州工作经验",[experience_list_num]) 
radar.render(path='./picture/suzhou_experience.html') 


# In[ ]:

#功能10 苏州薪资分析 
suzhou_data = data[data['city']=="苏州"]
min_salary = suzhou_data['min_salary']
max_salary = suzhou_data['max_salary']

min_salary_map = {"三千以下":0,"三千到五千":0,"五千到八千":0,"八千到一万":0,"一万到两万":0,"两万以上":0}
max_salary_map = {"三千以下":0,"三千到五千":0,"五千到八千":0,"八千到一万":0,"一万到两万":0,"两万以上":0}

for item in min_salary:
    if(item<3000):
        min_salary_map["三千以下"] = min_salary_map["三千以下"]+1
    elif(item<5000):
        min_salary_map["三千到五千"] = min_salary_map["三千到五千"]+1
    elif(item<8000):
        min_salary_map["五千到八千"] = min_salary_map["五千到八千"]+1
    elif(item<10000):
        min_salary_map["八千到一万"] = min_salary_map["八千到一万"]+1
    elif(item<20000):
        min_salary_map["一万到两万"] = min_salary_map["一万到两万"]+1
    else:
        min_salary_map["两万以上"] = min_salary_map["两万以上"]+1

for item in max_salary:
    if(item<3000):
        max_salary_map["三千以下"] = max_salary_map["三千以下"]+1
    elif(item<5000):
        max_salary_map["三千到五千"] = max_salary_map["三千到五千"]+1
    elif(item<8000):
        max_salary_map["五千到八千"] = max_salary_map["五千到八千"]+1
    elif(item<10000):
        max_salary_map["八千到一万"] = max_salary_map["八千到一万"]+1
    elif(item<20000):
        max_salary_map["一万到两万"] = max_salary_map["一万到两万"]+1
    else:
        max_salary_map["两万以上"] = max_salary_map["两万以上"]+1

columns = ["三千以下","三千到五千","五千到八千","八千到一万","一万到两万","两万以上"] 
data1 = [min_salary_map[item] for item in columns]
data2 = [max_salary_map[item] for item in columns]

# 普通折线图
 
line = Line('苏州薪资折线图')
line.add('最小薪资', columns, data1, mark_point=['min'])
line.add('最大薪资', columns, data2, mark_point=['max'], is_smooth=True)
line.render(path='./picture/suzhou_salary.html')


# In[ ]:

#功能11 苏州学历分析
suzhou_data = data[data['city']=="苏州"]
education_list = suzhou_data['education'].unique()
education_list_num = [len(suzhou_data[suzhou_data["education"]==item]) for item in education_list]

pie2 = Funnel("苏州学历分析", title_pos='center', width=900)
pie2.add("学历要求", education_list, education_list_num,  is_random=True, radius=[25, 60], rosetype='area', is_legend_show=False, is_label_show=True)
pie2.render(path='./picture/suzhou_education.html')


# In[ ]:

#功能12
welfare = list(data['welfare'])
welfare_list = list()
welfare_map = {}
for item in welfare:
    if(len(item)>0 and " " in item):
        item_list = item.split(" ")
        welfare_list+=item_list
    
for item in welfare_list:
    welfare_map[item] = welfare_map.get(item,0)+1
welfare = welfare_map.keys()
welfare_num = [welfare_map[item] for item in welfare]
        

city = data['city'].unique()
city_num = [len(data[data["city"]==item]) for item in city]

wordcloud = WordCloud("薪资待遇词云",width=1300, height=620)
wordcloud.add("薪资待遇词云", welfare, welfare_num, word_size_range=[20, 100])
wordcloud.render(path='./picture/salary_wordcloud.html')

wordcloud = WordCloud("城市分布词云",width=1300, height=620)
wordcloud.add("城市分布词云", city, city_num, word_size_range=[20, 100])
wordcloud.render(path='./picture/city_wordcoud.html')


# In[ ]:

#功能13 不同城市职位数量，地图
city_list = data['city'].unique()
city_list_num = [len(data[data["city"]==item]) for item in city_list]

print(city_list)
print(city_list_num)

city_name = list()
value_list = list()
for i,j in zip(city_list,city_list_num):
    if("省" not in i and i!="池州" and i!="宣城" and "区" not in i and j>5):
        city_name.append(i)
        value_list.append(j)
print(city_name)
print(value_list)
map = Geo("中国地图",'中国地图', width=1200, height=600)
map.add("", city_name, value_list, visual_range=[2, 3000],  maptype='china', is_visualmap=True,
    visual_text_color='#000')
map.render(path='./picture/map_position.html') 


# In[ ]:

#功能14 职位词频词云展示
import jieba
position_name = list(data['position_name'])
position_name_list = []
position_name_map = {}
for item in position_name:
    item = jieba.cut(item)
    position_name_list+=item
    
for item in position_name_list:
    position_name_map[item] = position_name_map.get(item,0)+1
position_name = position_name_map.keys()
position_name_num = [position_name_map[item] for item in position_name]

wordcloud = WordCloud("职位名称词云",width=1300, height=620)
wordcloud.add("职位名称词云", position_name, position_name_num, word_size_range=[20, 100])
wordcloud.render(path='./picture/position_name_wordcloud.html')

#面向大专的
import jieba
college_student_data = data[data['education']=='大专']
position_name = list(college_student_data['position_name'])
position_name_list = []
position_name_map = {}
for item in position_name:
    item = jieba.cut(item)
    position_name_list+=item
    
for item in position_name_list:
    position_name_map[item] = position_name_map.get(item,0)+1
position_name = position_name_map.keys()
position_name_num = [position_name_map[item] for item in position_name]

wordcloud = WordCloud("大专职位名称词云", width=1300, height=620)
wordcloud.add("大专职位名称词云", position_name, position_name_num, word_size_range=[20, 100])
wordcloud.render(path='./picture/college_student_position_name_wordcloud.html')

#面向本科的

import jieba
graduate_student_data = data[data['education']=='大专']
position_name = list(graduate_student_data['position_name'])
position_name_list = []
position_name_map = {}
for item in position_name:
    item = jieba.cut(item)
    position_name_list+=item
    
for item in position_name_list:
    position_name_map[item] = position_name_map.get(item,0)+1
position_name = position_name_map.keys()
position_name_num = [position_name_map[item] for item in position_name]

wordcloud = WordCloud("本科职位名称词云",width=1300, height=620)
wordcloud.add("本科职位名称词云", position_name, position_name_num, word_size_range=[20, 100])
wordcloud.render(path='./picture/graduate_position_name_wordcloud.html')


# In[ ]:

#功能15 大专本科职位数量前十城市分布图
#大专
college_student_data = data[data['education']=='大专']
college_city = college_student_data["city"].unique()
college_city_num = [len(college_student_data[college_student_data['city']==item]) for item in college_city]
college_student_data = [(i1,i2) for i1,i2 in zip(college_city,college_city_num)]
college_student_data = sorted(college_student_data,key=lambda x:x[1],reverse=True)
college_student_data = college_student_data[:10]
# print(college_student_data)
college_student_data = np.array(college_student_data)

#本科
graduate_student_data = data[data['education']=='本科']
graduate_city = graduate_student_data["city"].unique()
graduate_city_num = [len(graduate_student_data[graduate_student_data['city']==item]) for item in graduate_city]
graduate_student_data = [(i1,i2) for i1,i2 in zip(graduate_city,graduate_city_num)]
graduate_student_data = sorted(graduate_student_data,key=lambda x:x[1],reverse=True)
graduate_student_data = graduate_student_data[:10]
# print(graduate_student_data)
graduate_student_data = np.array(graduate_student_data)
# print(graduate_student_data)
pie = Pie("大专职位数量前十城市")
pie.add(
    "",
    college_student_data[:,0], 
    college_student_data[:,1],
    radius=[40, 75],
    label_text_color=None,
    is_label_show=True,
    is_more_utils=True,
    legend_orient="vertical",
    legend_pos="right",
)
pie.render(path='./picture/college_student_top_ten_city.html') 

# polar =Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
# polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barRadius', is_stack=True)

# c = (
#         Pie()
#         .add(
#             "",
#             [list(z) for z in zip(l1, num)],
#             radius=["40%", "75%"],   # 圆环的粗细和大小
#         )
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title="Pie-Radius"),
#             legend_opts=opts.LegendOpts(
#                 orient="vertical", pos_top="5%", pos_left="2%"  # 左面比例尺
#             ),
#         )
#         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#     )
# c.render_notebook()



pie = Pie("本科职位数量前十城市")
pie.add(
    "",
    graduate_student_data[:,0],
    graduate_student_data[:,1],
    radius=[40, 75],
    label_text_color=None,
    is_label_show=True,
    is_more_utils=True,
    legend_orient="vertical",
    legend_pos="right",
)
pie.render(path='./picture/graduate_student_top_ten_city.html')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



