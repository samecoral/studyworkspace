import requests
from bs4 import BeautifulSoup


#存放所有的url
list_url = []
#存放所有的公司名称
list_company_name = []
#存放所有的薪资
list_salary = []
#存放所有的职位名称
list_position = []
#存放工作经验
list_experience = []
list_education = []
#步骤：构造url  抓取url得到数据   根据得到的数据进行抽取
print(" 需要查找的工作类型是，例如python，java")
search_job = input();
URL = "https://www.jobui.com/jobs?cityKw=%E5%8C%97%E4%BA%AC&jobKw={}".format(search_job)
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
          "Cookie":"jobui_area=%25E5%258C%2597%25E4%25BA%25AC; jobui_p=1575018798954_48719284; jobui_user_passport=yk157501880297088; jobui_user_searchURL=http%3A%2F%2Fm.jobui.com%2Fjobs%3FjobKw%3Djava%26cityKw%3D%25E5%258C%2597%25E4%25BA%25AC%26sortField%3Dlast; job-subscribe-guide=1; PHPSESSID=eeiletb4u8rqqh1v4la9qh4n40; Hm_lvt_8b3e2b14eff57d444737b5e71d065e72=1575018798,1575097008,1575112913,1575117381; Hm_lpvt_8b3e2b14eff57d444737b5e71d065e72=1575117401; "}
responsedata = requests.get(URL, headers=header)
print(responsedata.content)
print(responsedata)
soup = BeautifulSoup(responsedata.content, "lxml")
print(soup)
select = soup.select(".job-segmetation>.job-name>h3")
for jobname in select:
    # print(jobname.get_text())
    list_position.append(jobname.get_text())

job_descs = soup.select(".job-segmetation > div.job-desc")
for job_des in job_descs:
    split = job_des.get_text().split("|")

    list_experience.append(split[0].strip())
    list_education.append(split[1].strip())
    list_salary.append(split[2].strip())


for position, salary,eduction,exprience in zip(list_position,list_salary,list_education,list_experience):
    All_Data = {
        "职位":position,
        "薪资":salary,
        "学历要求":eduction,
        "工作经验要求":exprience
    }
    print(All_Data)