from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
from collections import OrderedDict
import datetime

options = webdriver.ChromeOptions()

# headless 옵션 설정
options.add_argument('headless')
options.add_argument("no-sandbox")

# 브라우저 윈도우 사이즈
options.add_argument('window-size=1920x1080')

# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")  # 가속 사용 x
options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

# 드라이버 위치 경로 입력
driver = webdriver.Chrome(options=options)

# url을 이용하여 브라우저로 접속
driver.get("https://edu.ssafy.com/comm/login/SecurityLoginForm.do")

driver.implicitly_wait(2)

# 아이디/비밀번호를 입력해준다.
client_info = open('.client', 'r')
id = client_info.readline().rstrip()
pwd = client_info.readline().rstrip()
driver.find_element(by=By.NAME, value='userId').send_keys(id)
driver.find_element(by=By.NAME, value='userPwd').send_keys(pwd)
client_info.close()

# 로그인 버튼을 누르기
driver.find_element(by=By.XPATH, value='//*[@id="wrap"]/div/div/div[2]/form/div/div[2]/div[3]/a').click()

# 커리큘럼 화면으로 이동
driver.get("https://edu.ssafy.com/edu/lectureroom/curriculumn/curriculumnWeeklyList.do")
driver.implicitly_wait(2)


n_week = len(driver.find_elements(by=By.CLASS_NAME, value='unit-scroll > div'))


# 제일 첫 주차로 이동
active_week = driver.find_element(by=By.CLASS_NAME, value='unit.active > .txt-sm').get_attribute('data-week')
btn_prev = driver.find_element(by=By.CLASS_NAME, value='btn-prev')
while active_week != '1':
    btn_prev.click()
    driver.implicitly_wait(0.5)
    active_week = driver.find_element(by=By.CLASS_NAME, value='unit.active > .txt-sm').get_attribute('data-week')

file_data = OrderedDict()
now = datetime.datetime.now()
file_data['update_time'] = [now.year, now.month, now.day, now.hour, now.minute, now.second]

for week in range(n_week):
    print("%02d week"%(week+1))
    n_date = len(driver.find_elements(by=By.CLASS_NAME, value='course > li'))
    day = driver.find_elements(by=By.CLASS_NAME, value='course > li > span.date')
    time = driver.find_elements(by=By.CLASS_NAME, value='course > li > dl > dt')
    dict_w = {}

    for i in range(n_date):
        ymd_str = day[i].text
        ymd = list(map(int, ymd_str[0:-3].split(".")))

        lec_times = driver.find_elements(by=By.CLASS_NAME, value='course > li:nth-child(%d) > dl > dt' % (i + 2))
        lec_texts = driver.find_elements(by=By.CLASS_NAME, value='course > li:nth-child(%d) > dl > dd > div.info' % (i + 2))
        lec_btns = driver.find_elements(by=By.CLASS_NAME, value='course > li:nth-child(%d) > dl > dd > div.btns > button.btn.btn-sm-green.liveDirect' % (i + 2))

        data_lec = []
        for j in range(len(lec_times)):
            t_st, t_ed = map(str, lec_times[j].text.split("~"))
            lecture_time = [list(map(int, t_st.split(":"))), list(map(int, t_ed.split(":")))]
            lecture_text = lec_texts[j].text
            title, abstract, _ = list(map(str, lecture_text.split("\n")))
            href, btn_name = '', ''
            if lec_btns:
                href = lec_btns[0].get_attribute('data-req')
                btn_name = lec_btns[0].text
            sub_data = {'title' : title,
                        'time' : lecture_time,
                        'abstract' : abstract,
                        'btn' : btn_name,
                        'href' : href
            }
            data_lec.append(sub_data)
            #print(title)
            #print(lecture_time)
            #print(abstract)
            #print(btn_name, href)
            #print("-----")



        dict_w[i] = {'date':ymd,
                    'lectures':data_lec}
    file_data['week%02d'%(week+1)] = dict_w

    btn_next = driver.find_element(by=By.CLASS_NAME, value='btn-next')
    btn_next.click()
    driver.implicitly_wait(0.5)
with open('ssafy_schedule.json', 'w', encoding='utf-8') as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")


# driver.get_screenshot_as_file('./capture.png')
