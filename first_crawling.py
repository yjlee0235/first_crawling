from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#종정시 아이디/비밀번호 입력
id_text = ''
pw_text = ''

chrome = webdriver.Chrome()
URL = 'https://info.hansung.ac.kr/'
chrome.get(URL)
id_input = chrome.find_element_by_css_selector('#id')
pw_input = chrome.find_element_by_css_selector('#passwd')

time.sleep(0.5)
#로그인 부분
id_input.send_keys(id_text)
pw_input.send_keys(pw_text)
time.sleep(0.5)
pw_input.send_keys(Keys.ENTER)

#시간표 사이트 열기
time.sleep(0.5)
timetableURL = 'https://info.hansung.ac.kr/jsp/haksa/siganpyo.jsp'
chrome.get(timetableURL)

#BeautifulSoup 사용해 시간표 크롤링 -> selenium은 하위 속성을 잘못가져옴
time.sleep(3)
html = chrome.page_source
soup = BeautifulSoup(html, 'html.parser')

tableDatas = soup.select('tr.jqgrow.ui-row-ltr.ui-widget-content')

#크롬 종료
chrome.quit()

#크롤링해 온 결과를 crawlingRes에 list로 추가
crawlingRes = []
for tableData in tableDatas:
    tmp = []
    for tableDataText in tableData:
        tmp.append(tableDataText.text)
    crawlingRes.append(tmp)

#crawlingRes에 있는 불필요한 자료를 제거
Res = []
for semiRes in crawlingRes:
    Res.append(semiRes[1:5] + semiRes[6:12])


#결과를 출력
#for data in Res:
#    print(data)

"""
Res[0] ~ Res[9] 데이터

Res[0]     Res[1]  Res[2]   Res[3]    Res[4]  Res[5]  Res[6]  Res[7]  Res[8]       Res[9]
과목코드    과목명   구분    과목구분    학점    주야     분반    학년     교수      강의실 및 교시

"""

#파일에 크롤링한 데이터 저장
file_name = 'subjects-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.txt'

with open(file_name, "w") as f:
    for data in Res:
        f.write(' '.join(data) + '\n')
