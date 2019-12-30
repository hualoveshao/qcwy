
# coding: utf-8

# In[14]:

import requests
from lxml import etree
import pandas as pd
import numpy as np
import time
from tqdm import tqdm


# In[11]:

# 获取网页源代码
def get_page(url):
    # 构造请求头部
    headers = {
        'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    # 发送请求，获得响应
    
    response = requests.get(url=url,headers=headers)
    # 获得网页源代码
    content = response.content
   
    html  = content.decode('gbk','ignore')
    return html
    
    
#获取每个页面的职位相信信息链接
def get_position_url(url):
    html  = get_page(url)
    html_elem = etree.HTML(html)
    position_url = html_elem.xpath("//p[contains(@class,'t1')]//@href")
    return position_url

#获取每个页面职位详细信息
def get_position_info(html):
    html_elem = etree.HTML(html)
    city = ""
    msg_data = []
    try:
        msg_data = html_elem.xpath("//p[contains(@class,'msg')]/text()")
        #城市
        city = msg_data[0].replace("\xa0","")
        if("-" in city):
            city = city.split("-")[0]
    except:
        pass
    
    #职位名称
    position_name = ""
    try:
        position_name = html_elem.xpath("//div[@class='cn']/h1/text()")[0]
    except:
        pass
    
    #公司名称
    company_name = ""
    try:
        company_name = html_elem.xpath("//a[contains(@class,'com_name')]/p/text()")[0]
    except:
        pass
    
    #公司规模
    company_proportion = ""
    try:
        company_proportion = html_elem.xpath("//div[@class='com_tag']/p/@title")[1]
    except:
        pass
    
    #公司类型
    company_type = ""
    try:
        company_type = html_elem.xpath("//div[@class='com_tag']/p/@title")[0]
    except:
        pass
    
    
    #经验要求
    experience = ""
    try:
        experience = msg_data[1].replace("\xa0","") 
    except:
        pass
    
    #学历要求
    education = ""
    try:
        education = msg_data[2].replace("\xa0","")
    except:
        pass
    
    #专业要求
    profession = ""
    try:
        profession = html_elem.xpath("//div[@class='tCompany_main']/div[@class='tBorderTop_box']")[0]
        profession = profession.xpath('string(.)').replace("\xa0","").replace(" ","").replace("\r","").replace("\n","")
    except:
        pass
    
    #福利待遇
    salary = ""
    try:
        salary = html_elem.xpath("//div[@class='cn']/strong/text()")[0]
    except:
        pass
    
    #所属行业
    industry = ""
    try:
        industry = html_elem.xpath("//div[@class='com_tag']/p/@title")[2]
    except:
        pass
    
    #福利待遇
    welfare = ""
    try:
        welfare = html_elem.xpath("//span[@class='sp4']/text()")
        welfare = " ".join(welfare)
    except:
        pass
    
    #发布时间
    post_time = ""
    try:
        post_time = msg_data[4].replace("\xa0","")
    except:
        pass
    
    return [city,position_name,company_name,company_proportion,company_type,experience,education,profession,salary,industry,welfare,post_time]

#获取一个岗位的详细信息
def get_detail_position_info(url):
    html = get_page(url)
    result = get_position_info(html)
    return result

#获取一页的岗位详细信息
def get_info_by_page_num(page_num):
    print("获取第 ",page_num," 页信息")
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99,%E7%89%A9%E8%81%94%E7%BD%91,2,"+str(page_num)+".html"
    info = []
    #获取一页内所有的职位URL
    position_urls = get_position_url(url)
    #通过每页的链接获取页面内需要的数据信息
    for position_url in position_urls:
        result = get_detail_position_info(position_url)
        info.append(result)
    return info

#保存一页信息到tsv文件中
def save_file_by_page_num(page_num,info):
    #50行 11列
    print(print("保存第 ",page_num," 页信息"))
    data = pd.DataFrame(info)
    data.columns = ["city","position_name","company_name","company_proportion","company_type","experience","education","profession","salary","industry","welfare","post_time"]
    data.to_csv("./data/"+str(page_num)+'.tsv',sep = "\t", index = False)
    


# In[18]:

#获取一页信息
page_num = 1
while page_num<340:
    try:
        info = get_info_by_page_num(page_num)
        #保存一页信息
        save_file_by_page_num(page_num,info)
        time.sleep(1)
    except Exception as e:
        print("出现问题，重新爬取该页",e)
        time.sleep(5)
        continue
    page_num+=1


# In[ ]:




# In[ ]:




# In[ ]:



