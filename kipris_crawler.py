from selenium import webdriver
from bs4 import BeautifulSoup
import time
import time, os
from datetime import datetime
import pandas as pd



#kipris search link
link = 'http://beginner.kipris.or.kr/beginner/search/headerSearch.do?#page1'
driver = webdriver.Chrome('chromedriver.exe')
driver.get(link)
time.sleep(1)


# # download chrome driver https://sites.google.com/a/chromium.org/chromedriver/home

os.makedirs('result', exist_ok=True)

df = pd.DataFrame(columns=['특허명', '출원번호', '출원일', '출원인', '발명자', '대리인', '특허상태', '특허요약'])#데이터프레임 설정
Patentname = list()
Application_number = list()
Application_number_date = list()
Applicant = list()
State = list()
Inventor = list()
Agent = list()
Summary = list()



#Searching for human lives
hum = driver.find_element_by_xpath('//*[@id="searchTypeSelectDiv"]/span[3]/a/img')
hum.click()
#input search keword
time.sleep(0.5)
driver.find_element_by_name('searchKeyword').send_keys('"인천대학교 산학협력단"')
driver.maximize_window()
time.sleep(1)

#click search botton
searchbutton = driver.find_element_by_xpath('//*[@id="personSearchBtn"]')
searchbutton.click()
time.sleep(1)

#more Patent
morepatent = driver.find_element_by_xpath('//*[@id="morePatentBtn"]/a')
morepatent.click()
time.sleep(2)

#page 1~35
for p in range(3):
    #next page
        for k in range(10):
            k = k+1
            nextpage = driver.find_element_by_xpath(f'//*[@id="patentSearchResultPaging"]/li[2]/a[{k}]')
            nextpage.click()
            time.sleep(2)
        # infor patent
            for i in range(30):
                Patentname = driver.find_element_by_xpath(f'// *[ @ id = "patentResultList"] / article[{i+1}] / div[2] / div[1] / h1 / a[2]').text
                Application_number1 = driver.find_element_by_xpath(f'//*[@id="patentResultList"]/article[{i+1}]/div[2]/div[2]/ul/li[1]/a/span').text
                Application_number = Application_number1[0:13]
                Application_number_date = Application_number1[14:24]
                Applicant = driver.find_element_by_xpath(f'//*[@id="patentResultList"]/article[{i+1}]/div[2]/div[2]/ul/li[2]/font').text
                Inventor = driver.find_element_by_xpath(f'//*[@id="patentResultList"]/article[{i+1}]/div[2]/div[2]/ul/li[4]/font').text
                State = driver.find_element_by_xpath(f'//*[@id="patentResultList"]/article[{i+1}]/div[2]/div[1]/h1/a[1]/span').text
                Agent = driver.find_element_by_xpath(f'//*[@id="patentResultList"]/article[{i+1}]/div[2]/div[2]/ul/li[3]/font').text
                Summary = driver.find_element_by_xpath(f'//*[@id="patentResultList"]/article[{i+1}]/div[2]/div[2]/div/span[2]').text

                # append to dataframe
                df = df.append({
                    '특허명': Patentname,
                    '출원번호': Application_number,
                    '출원일': Application_number_date,
                    '출원인': Applicant,
                    '발명자': Inventor,
                    '대리인': Agent,
                    '특허상태': State,
                    '특허요약': Summary
                }, ignore_index=True)
        plustenpage = driver.find_element_by_xpath('// *[ @ id = "patentSearchResultPaging"] / li[3] / a')
        plustenpage.click()
        time.sleep(2)

#page 31~35
for k in range(5):
    k = k + 1
    nextpage = driver.find_element_by_xpath(f'//*[@id="patentSearchResultPaging"]/li[2]/a[{k}]')
    nextpage.click()
    time.sleep(2)
    # infor patent
    for i in range(30):
        Patentname = driver.find_element_by_xpath(
            f'// *[ @ id = "patentResultList"] / article[{i + 1}] / div[2] / div[1] / h1 / a[2]').text
        Application_number1 = driver.find_element_by_xpath(
            f'//*[@id="patentResultList"]/article[{i + 1}]/div[2]/div[2]/ul/li[1]/a/span').text
        Application_number = Application_number1[0:13]
        Application_number_date = Application_number1[14:24]
        Applicant = driver.find_element_by_xpath(
            f'//*[@id="patentResultList"]/article[{i + 1}]/div[2]/div[2]/ul/li[2]/font').text
        Inventor = driver.find_element_by_xpath(
            f'//*[@id="patentResultList"]/article[{i + 1}]/div[2]/div[2]/ul/li[4]/font').text
        State = driver.find_element_by_xpath(
            f'//*[@id="patentResultList"]/article[{i + 1}]/div[2]/div[1]/h1/a[1]/span').text
        Agent = driver.find_element_by_xpath(
            f'//*[@id="patentResultList"]/article[{i + 1}]/div[2]/div[2]/ul/li[3]/font').text
        Summary = driver.find_element_by_xpath(
            f'//*[@id="patentResultList"]/article[{i + 1}]/div[2]/div[2]/div/span[2]').text
        # append to dataframe
        df = df.append({
            '특허명': Patentname,
            '출원번호': Application_number,
            '출원일': Application_number_date,
            '출원인': Applicant,
            '발명자': Inventor,
            '대리인': Agent,
            '특허상태': State,
            '특허요약': Summary
        }, ignore_index=True)

nextpage = driver.find_element_by_xpath('//*[@id="patentSearchResultPaging"]/li[2]/a[6]')
nextpage.click()
time.sleep(2)

#page36
for i in range(1):
    Patentname = driver.find_element_by_xpath(
        f'// *[ @ id = "patentResultList"] / article[{i + 1}] / div[2] / div[1] / h1 / a[2]').text
    Application_number1 = driver.find_element_by_xpath(
        f'//*[@id="patentResultList"]/article[{i + 1}]/div[2]/div[2]/ul/li[1]/a/span').text
    Application_number = Application_number1[0:13]
    Application_number_date = Application_number1[14:24]
    Applicant = driver.find_element_by_xpath(
        f'//*[@id="patentResultList"]/article[{i + 1}]/div[2]/div[2]/ul/li[2]/font').text
    Inventor = driver.find_element_by_xpath(
        f'//*[@id="patentResultList"]/article[{i + 1}]/div[2]/div[2]/ul/li[4]/font').text
    State = driver.find_element_by_xpath(
        f'//*[@id="patentResultList"]/article[{i + 1}]/div[2]/div[1]/h1/a[1]/span').text
    Agent = driver.find_element_by_xpath(
        f'//*[@id="patentResultList"]/article[{i + 1}]/div[2]/div[2]/ul/li[3]/font').text
    Summary = driver.find_element_by_xpath(
        f'//*[@id="patentResultList"]/article[{i + 1}]/div[2]/div[2]/div/span[2]').text
    # append to dataframe
    df = df.append({
        '특허명': Patentname,
        '출원번호': Application_number,
        '출원일': Application_number_date,
        '출원인': Applicant,
        '발명자': Inventor,
        '대리인': Agent,
        '특허상태': State,
        '특허요약': Summary
    }, ignore_index=True)


# finally save the dataframe into csv file
filename = datetime.now().strftime('result/%Y-%m-%d_%H-%M-%S.csv')
df.to_csv(filename, encoding='utf-8-sig', index=False)
driver.stop_client()

print('Done!')

