from selenium import webdriver
from bs4 import BeautifulSoup
import time
import time, os
from datetime import datetime
import pandas as pd

#INU research link
link = 'https://www.inu.ac.kr/com/cop/resPatentResSearch.do?id=inu_060402000000'
driver = webdriver.Chrome('chromedriver.exe')
driver.get(link)
time.sleep(2)

# download chrome driver https://sites.google.com/a/chromium.org/chromedriver/home

os.makedirs('result', exist_ok=True)

df = pd.DataFrame(columns=['name', 'univ', 'major', 'field', 'email'])#Data Frame Settings
inforlist = list()
name = list()
univ = list()
major = list()
field = list()
email = list()


#Enter Search Window
eng = driver.find_element_by_xpath(('//*[@id="txt1"]/option[2]'))#Enter Engineering Session
eng.click()
time.sleep(4)

#Press Search Button
searchbutton = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/form/div/div[1]/div/input')
searchbutton.click()
print('Page Entry Complete')
time.sleep(4)


#Save xpaths as boxes that point to the researchers on the page one by one
boxes = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')



for k in range(10):
    driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/div/a')[k].click()
    # Number of researchers on page
    print('There are %d researcher !' % len(boxes))
    print('Writing the data...')

    print('Complete entry to the next page')

    for i in range(10):
        infor = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')[i].text

        list_infor = infor.split()
        del list_infor[0]

        print(list_infor)
        inforlist.append(list_infor)


    time.sleep(3)

# Load page 11
elevenpage = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div/span[3]/a/img')#Specify arrows
elevenpage.click()
for k in range(3):
    driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/div/a')[k].click()
    # Number of researchers on page
    print('There are %d researcher !' % len(boxes))
    print('Writing the data...')

    print('Entry completed on the next page')

    for i in range(10):
        infor = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')[i].text
        print(infor)

        list_infor = infor.split()
        del list_infor[0]

        print(list_infor)
        inforlist.append(list_infor)

    time.sleep(3)

    #Entering the search window of the College of Agriculture and Fisheries
ocean = driver.find_element_by_xpath(('//*[@id="txt1"]/option[3]'))
ocean.click()
time.sleep(4)

    # Press Search Button
searchbutton = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/form/div/div[1]/div/input')
searchbutton.click()
print('Page Entry Completed')
time.sleep(4)

    # Save xpaths as boxes that point to the researchers on the page one by one
boxes = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')


for k in range(1):
    driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/div/a')[k].click()
        # Number of researchers on page
    print('There are %d researcher !' % len(boxes))
    print('Writing the data...')

    print('Page Entry Completed')

    time.sleep(3)

    for i in range(6):
        infor = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')[i].text
        print(infor)
        list_infor = infor.split()
        del list_infor[0]

        print(list_infor)
        inforlist.append(list_infor)

 #Entering the Search Window of the University of Composite Studies
compund = driver.find_element_by_xpath(('//*[@id="txt1"]/option[4]'))  # Entering a Composite Session
compund.click()
time.sleep(4)

    # Press Search Button
searchbutton = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/form/div/div[1]/div/input')
searchbutton.click()
print('Page Entry Completed')
time.sleep(4)

    # Save xpaths as boxes that point to the researchers on the page one by one
boxes = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')


for k in range(1):
    driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/div/a')[k].click()
        # Number of researchers on page
    print('There are %d researcher !' % len(boxes))
    print('Writing the data...')

    print('Page Entry Completed')

    time.sleep(3)

    for i in range(4):
        infor = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')[i].text
        print(infor)
        list_infor = infor.split()
        del list_infor[0]

        print(list_infor)
        inforlist.append(list_infor)


 #사회과학대
    # 검색창 진입
social = driver.find_element_by_xpath(('//*[@id="txt1"]/option[5]'))  #사회과학세션으로진입
social.click()
time.sleep(4)

    # Press Search Button
searchbutton = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/form/div/div[1]/div/input')
searchbutton.click()
print('Page Entry Completed')
time.sleep(4)

    # Save xpaths as boxes that point to the researchers on the page one by one
boxes = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')


for k in range(8):
    driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/div/a')[k].click()
        # Number of researchers on page
    print('There are %d researcher !' % len(boxes))
    print('Writing the data...')

    print('Entry completed on the next page')

    time.sleep(3)

    for i in range(10):
        infor = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')[i].text
        print(infor)
        list_infor = infor.split()
        del list_infor[0]

        print(list_infor)
        inforlist.append(list_infor)

ninepage = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div/span[4]/a/img')#Specify Arrow
ninepage.click()
for i in range(4):
    infor = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')[i].text
    print(infor)
    list_infor = infor.split()
    del list_infor[0]

    print(list_infor)
    inforlist.append(list_infor)

time.sleep(3)

#College of Fine Arts College
art = driver.find_element_by_xpath(('//*[@id="txt1"]/option[6]'))#Entering the College of Arts Session
art.click()
time.sleep(4)

#Press Search Button
searchbutton = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/form/div/div[1]/div/input')
searchbutton.click()
print('Page Entry Completed')
time.sleep(4)


#Save xpaths as boxes that point to the researchers on the page one by one
boxes = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')



for k in range(2):
    driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/div/a')[k].click()
    # Number of researchers on page
    print('There are %d researcher !' % len(boxes))
    print('Writing the data...')

    print('Page Entry Completed')

    for i in range(10):
        infor = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')[i].text

        print(infor)
        list_infor = infor.split()
        del list_infor[0]

        print(list_infor)
        inforlist.append(list_infor)

    time.sleep(3)

threepage = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div/span[4]/a/img')#Specify Arrow
threepage.click()
for k in range(1):
    driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/div/a')[k].click()
    # Number of researchers on page
    print('There are %d researcher !' % len(boxes))
    print('Writing the data...')

    print('Page Entry Completed')

    for i in range(6):
        infor = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')[i].text
        print(infor)
        list_infor = infor.split()
        del list_infor[0]

        print(list_infor)
        inforlist.append(list_infor)

    time.sleep(3)


#medical science
medic = driver.find_element_by_xpath(('//*[@id="txt1"]/option[7]'))#Entering the College of Medicine session
medic.click()
time.sleep(4)

#Press Search Button
searchbutton = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/form/div/div[1]/div/input')
searchbutton.click()
print('Page Entry Completed')
time.sleep(4)


#Save xpaths as boxes that point to the researchers on the page one by one
boxes = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')



for k in range(1):
    driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/div/a')[k].click()
    #Number of researchers on page
    print('There are %d researcher !' % len(boxes))
    print('Writing the data...')

    print('Page Entry Completed')

    for i in range(4):
        infor = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')[i].text

        print(infor)
        list_infor = infor.split()
        del list_infor[0]

        print(list_infor)
        inforlist.append(list_infor)

    time.sleep(3)


#Humanities
people = driver.find_element_by_xpath(('//*[@id="txt1"]/option[8]'))#Entering the College of Humanities College Session
people.click()
time.sleep(4)

#Press Search Button
searchbutton = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/form/div/div[1]/div/input')
searchbutton.click()
print('Page Entry Completed')
time.sleep(4)


#Save xpaths as boxes that point to the researchers on the page one by one
boxes = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')



for k in range(4):
    driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/div/a')[k].click()
    # Number of researchers on page
    print('There are %d researcher !' % len(boxes))
    print('Writing the data...')

    print('Page Entry Completed')

    for i in range(10):
        infor = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')[i].text

        print(infor)
        list_infor = infor.split()
        del list_infor[0]

        print(list_infor)
        inforlist.append(list_infor)

    time.sleep(3)

fivepage = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div/span[4]/a/img')#Specify Arrow
fivepage.click()
for k in range(1):
    driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/div/a')[k].click()
    #Number of researchers on page
    print('There are %d researcher !' % len(boxes))
    print('Writing the data...')

    print('Page Entry Completed')

    for i in range(7):
        infor = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')[i].text
        print(infor)
        list_infor = infor.split()
        del list_infor[0]

        print(list_infor)
        inforlist.append(list_infor)

    time.sleep(3)


#Natural science
nature = driver.find_element_by_xpath(('//*[@id="txt1"]/option[9]'))#Entering the College of Natural Sciences
nature.click()
time.sleep(4)

#Press Search Button
searchbutton = driver.find_element_by_xpath('//*[@id="contents"]/div[1]/form/div/div[1]/div/input')
searchbutton.click()
print('Page Entry Completed')
time.sleep(4)


#Save xpaths as boxes that point to the researchers on the page one by one
boxes = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')



for k in range(5):
    driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/div/a')[k].click()
    #Number of researchers on page
    print('There are %d researcher !' % len(boxes))
    print('Writing the data...')

    print('Page Entry Completed')

    for i in range(10):
        infor = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/form/div/div[2]/div/table/tbody/tr')[i].text

        print(infor)
        list_infor = infor.split()
        del list_infor[0]

        print(list_infor)
        inforlist.append(list_infor)

    time.sleep(3)

print(inforlist)
print(len(inforlist))
#len = 351
p = 0
for p in range(351):
    name.append(inforlist[p][0])
    univ.append(inforlist[p][1])
    major.append(inforlist[p][2])
    email.append(inforlist[p][-1])
    del inforlist[p][0]
    del inforlist[p][0]
    del inforlist[p][0]
    del inforlist[p][-1]
    field.append(inforlist)

print(len(name))
print(len(univ))
print(len(field))
print(len(major))
print(len(email))

w = field.pop(0)


for a in range(351):
    n = name.pop(0)
    u = univ.pop(0)
    m = major.pop(0)
    f = w.pop(0)
    ff = "/".join(f)

    e = email.pop(0)  # append to dataframe
    df = df.append({
        'name': n,
        'univ': u,
        'major': m,
        'field': ff,
        'email': e,
      }, ignore_index=True)

# finally save the dataframe into csv file
filename = datetime.now().strftime('result/%Y-%m-%d_%H-%M-%S.csv')
df.to_csv(filename, encoding='utf-8-sig', index=False)
driver.stop_client()

print('Done!')