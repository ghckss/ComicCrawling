import time, datetime
from Naver_crawl import Naver_crawl
import schedule

platform = "Naver"

def initialize():
    crawl = Naver_crawl()
    for i in range(1, 9):
        crawl.checkDayEntry(i)
    crawl.initRoop()

def routine():

    #엔트리 검사
    print("rountine이 실행됩니다.")
    print(time.ctime())
    now = datetime.datetime.now()
    day = now.weekday()+1
    crawl = Naver_crawl()
    crawl.checkDayEntry(day)
    print("rountine이 종료되었습니다. %s" %str(time.ctime()))

def job():
    routine()

    print("JOB이 실행됩니다~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(time.ctime())
    #완결 entry검사
    #완결 갯수 검사
    #완결 길이 다르면 추가 아니면 끝

    crawl = Naver_crawl()
    while(True) :
        if crawl.roopNaverCrawllist() == 0:
            break
        elif time.localtime().tm_hour > 20:
            break

    print("job 종료@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

initialize()
schedule.every().day.at("15:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

