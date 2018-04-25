from selenium import webdriver
from Crawl_util import Util
from ControlToonVO import *
import CrawlDAO
from selenium.common.exceptions import NoSuchElementException
import time, datetime
import ImageDownload

chrome_path = r"C:/Users/HHC/Desktop/chromedriver.exe"
phantom_path = r"C:/Users/sdfasd/Desktop/phantomjs.exe"
#driver = webdriver.Chrome(chrome_path)
driver = webdriver.PhantomJS(phantom_path)
driver.get("http://comic.naver.com/webtoon/weekday.nhn")

class Naver_crawl:

    day = 0
    util = Util()
    wb_platform = "Naver"
    finish_day = "8"
    webtoonId = ""
    webtoonVO = None
    episodeVO = None

    #해당 날짜의 모든 웹툰에 접근how
    def accessDayWebToon(self, day):
        position = 0
        print("@@@@ ACESS DAY-WEBTOON @@@@")

        intergerDay = day
        real_webtoonList = []
        daylist2 = [None, 2, 3, 4, 5, 6, 7, 8, 7]
        daylist1 = [None, "content", "content", "content", "content", "content", "content", "content", "submenu"]

        day1 = daylist1[day]
        day2 = daylist2[day]
        driver.get("http://comic.naver.com/webtoon/weekday.nhn")
        path = """//*[@id="%s"]/ul/li[%d]/a""" % (day1, day2)
        driver.find_element_by_xpath(path).click()

        count = driver.find_elements_by_css_selector("#content > div.list_area > ul > li")

        for i in range(1, len(count)+1, 1):
            position += 40

            webtoon_selector = "#content > div.list_area > ul > li:nth-child(%d) > dl > dt > a" % i
            driver.find_element_by_css_selector(webtoon_selector).click()

            real_webtoonList.append(self.getInWebToon(intergerDay))
            print("@accessDayWebToon " + real_webtoonList[i-1].webtoonName + "를 추가하였습니다.")

            driver.back()
            driver.execute_script("window.scrollTo(0, "+str(position)+");")
        driver.execute_script("window.scrollTo(0, 0);")
        return real_webtoonList

    #해당 날짜의 모든 웹툰 에피소드 들고오기
    def accessDayWebToonEpisode(self, day, WebtoonVO):
        real_episodeList = []
        self.day = day
        path = """//*[@id="comic-scheduled-tabs"]/div/div[%s]/button""" %day
        driver.find_element_by_xpath(path).click()

        count = driver.find_elements_by_css_selector("#comic-scheduled-day-%s > li" %day)

        for i in range(1, len(count)+1, 1):
        #for i in range(11, 12):
            webtoon_selector = "#comic-scheduled-day-%s > li:nth-child(%s) > a > div.homelist-thumb" %(day, i)
            driver.find_element_by_css_selector(webtoon_selector).click()

            real_episodeList = self.getWebToonEpisode(WebtoonVO)
            print("@accessDayWebToonEpisode " + str(len(real_episodeList)) + "개의 에피소드리스트를 받았습니다.")
            driver.back()

        return real_episodeList

    #특정 웹툰 에피소드 들고오기
    def findWebtoon(self, WebtoonVO):
        print("@@@@@@ FIND WEBTOON @@@@@@@@")
        real_episodeList = []
        temp_day = WebtoonVO.day.split(" ")
        integerDay = int(temp_day[0]) + 1

        print(temp_day[0])
        menu = "content"
        driver.get("http://comic.naver.com/webtoon/weekday.nhn")
        if integerDay == 10:
            menu = "submenu"
            integerDay = 7
        print("클릭직전 %s"%integerDay)
        path = """//*[@id="%s"]/ul/li[%d]/a""" % (menu, integerDay)
        driver.find_element_by_xpath(path).click()

        wb_name = driver.find_elements_by_css_selector("#content > div.list_area > ul > li > dl > dt > a")
        print(len(wb_name))

        for i in range(1, len(wb_name)+1):
            print("돌아라")
            if wb_name[i-1].get_attribute("title") == WebtoonVO.webtoonName:
                print("%d번째에서 %s을 찾았다." %(i, wb_name[i-1].get_attribute("title")))
                position = str(i*40)
                driver.execute_script("window.scrollTo(0, "+position+");")
                driver.find_element_by_css_selector("#content > div.list_area > ul > li:nth-child(%d) > dl > dt > a" % i).click()

                real_episodeList = self.getWebToonEpisode(WebtoonVO)
                driver.find_element_by_xpath(path).click()

                break

            elif wb_name[i-1].get_attribute("title") != WebtoonVO.webtoonName:
                print("다릅니다")
                print(wb_name[i-1].get_attribute("title") + "/" +WebtoonVO.webtoonName)
        return real_episodeList

    #특정 웹툰을 가져옮
    def getInWebToon(self, day):
        global thumbnail
        print("@@@@ GET IN WEBTOON @@@@")
        db_day = ""
        #ID
        self.webtoonId = self.util.makeUUID()
        #제목
        name_selector = "#content > div.comicinfo > div.detail > h2"

        #설명
        introduce_selector = "#content > div.comicinfo > div.detail > p"

        #썸네일
        thumbnail_selector = "#content > div.comicinfo > div.thumb > a > img"

        #작가
        writer_selector = "#content > div.comicinfo > div.detail > h2 > span.wrt_nm"
        mythumbnail = ""
        try:
            writer = driver.find_element_by_css_selector(writer_selector).text
            name = driver.find_element_by_css_selector(name_selector).text[:-(len(writer) + 1)].replace("컷툰", "").replace("휴재", "").replace("스마트툰", "")
            thumbnail = driver.find_element_by_css_selector(thumbnail_selector).get_attribute("src")
            genre = "미정"
            introduce = driver.find_element_by_css_selector(introduce_selector).text
            writer = writer.replace(" / ", " ")
            if not CrawlDAO.isWebtoonExist(self.wb_platform, name):
                mythumbnail = ImageDownload.download_img(thumbnail, "webtoon", self.webtoonId)
        except NoSuchElementException:
            print("아~ 못찻겠다 꾀꼬리 ")
            pass
        print(name)
        print(thumbnail)
        print(writer)
        print(introduce)
        if day == 8:
            day = 9

        return WebtoonVO(self.wb_platform, day, self.webtoonId, name, writer, thumbnail, introduce, genre, 0, "2010-01-02", mythumbnail)

    #에피소드를 긁기
    def getWebToonEpisode(self, WebtoonVO):

        print("웹툰의 에피소드를 읽습니다.")
        episodeList = []
        titles = []
        dates = []
        thumbnails = []
        links = []
        temp = 0
        indexNumber = []
        totalCount = 0
        number = 0
        mythumbnail = []
        db_lastEpisode = ""
        db_lastNumber = 0

        #다음 페이지
        next_button = driver.find_elements_by_css_selector("span.cnt_page")
        #DB 최신화
        if CrawlDAO.getLastEpisode(WebtoonVO.webtoonId) != [None]:
            db_lastEpisode = CrawlDAO.getLastEpisode(WebtoonVO.webtoonId)[0]
            db_lastNumber = CrawlDAO.getLastEpisode(WebtoonVO.webtoonId)[1]
        print(db_lastEpisode)
        while True:
            #에피소드이름
            ep_titles = driver.find_elements_by_css_selector("#content > table > tbody > tr > td.title > a")
            #날짜
            ep_dates = driver.find_elements_by_css_selector("#content > table > tbody > tr > td.num")
            # 썸네일
            ep_thumbnails = driver.find_elements_by_css_selector("#content > table > tbody > tr > td:nth-child(1) > a > img[title]")
            # 링크
            ep_links = driver.find_elements_by_css_selector("#content > table > tbody > tr > td.title > a")

            #에피소드, 날짜 초기화
            for i in range(1, len(ep_titles)+1):
                if db_lastEpisode == ep_links[i-1].get_attribute("href"):
                    temp = 1
                    break
                titles.append(ep_titles[i-1].get_attribute("text"))
                dates.append(ep_dates[i-1].text.replace(".", "-"))
                thumbnails.append(ep_thumbnails[i-1].get_attribute("src"))
                links.append(ep_links[i-1].get_attribute("href"))
                number = number - 1
                indexNumber.append(number)
                totalCount = totalCount + 1
            if len(next_button) == 0 or temp ==1:
                break
            if len(next_button) > 0:
                next_button[0].click()
            next_button = driver.find_elements_by_css_selector("a.next")

        for i in range(len(indexNumber)):
            indexNumber[i] += totalCount + 1 + db_lastNumber
        for i in range(len(indexNumber)):
            mythumbnail.append(ImageDownload.download_img(thumbnails[i], "episode", str(WebtoonVO.webtoonId) + "-" + str(indexNumber[i])))
        for i in range(len(titles)):
            episodeVO = EpisodeVO(indexNumber[i], WebtoonVO.webtoonId, titles[i], thumbnails[i], links[i], dates[i], "무료", mythumbnail[i])
            episodeList.append(episodeVO)
        return episodeList

    #Day엔트리 체크
    def checkDayEntry(self, day):
        print("@@@@ %d의 Entry를 검사합니다. @@@@"%day)

        real_webtoonList = self.accessDayWebToon(day)
        real_count = len(real_webtoonList)
        legacy_webtoonList = CrawlDAO.getWebtoonList(self.wb_platform, str(day))

        legacy_count = len(legacy_webtoonList)
        flag_list = [0 for _ in range(legacy_count)]

        if legacy_count > 0:
            #최근 엔트리가 DB엔트레 있는지 체크
            print("DB데이터 갯수 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print(legacy_count)
            for i in range(real_count):
                target = real_webtoonList[i]

                for j in range(legacy_count):
                    if target.webtoonName == legacy_webtoonList[j].webtoonName:
                        print("찾았다. @" + target.webtoonName + " / " + legacy_webtoonList[j].webtoonName)
                        flag_list[j] = 1

                        #DB에 같은 웹툰이 있었으니까 크로울 리스트에추가
                        #크로울 리스트에 똑같은 DB가 있으면 추가 x
                        if day == 8:
                            legacy_webtoonList[j].day = day + 1
                        elif day<8:
                            legacy_webtoonList[j].day = day
                        if CrawlDAO.isCrawlExist(legacy_webtoonList[j].webtoonId, legacy_webtoonList[j].day) == 0:
                            CrawlDAO.insertCrawlList(legacy_webtoonList[j])
                        break

                    elif target.webtoonName != legacy_webtoonList[j].webtoonName:
                        print("다르다. @"+target.webtoonName + "/" + legacy_webtoonList[j].webtoonName)
                        #웹툰을 DB에 추가하고 CrawlList에 추가

                        #검색중인 웹툰이 존재하지 않으면
                        if CrawlDAO.isWebtoonExist(self.wb_platform, target.webtoonName) is not True:
                            CrawlDAO.insertWebtoon(target)
                            print("신작 %s을 추가합니다." %target.webtoonName)

                            if day == 8:
                                legacy_webtoonList[j].day = day + 1
                            elif day < 8:
                                legacy_webtoonList[j].day = day
                            if CrawlDAO.isCrawlExist(legacy_webtoonList[j].webtoonId, legacy_webtoonList[j].day) == 0:
                                CrawlDAO.insertCrawlList(legacy_webtoonList[j])
                                break

                        #검색중인 웹툰이 존재하면
                        else:
                            vo = CrawlDAO.getWebtoonVO(self.wb_platform, target.webtoonName)

                            legacy_day = CrawlDAO.getWebtoonDay(self.wb_platform, target.webtoonName)
                            target_day = str(day)
                            print("@@@@@@@@@@@@@@@")
                            print(target_day)
                            print("레거시 = %s " %legacy_day)

                            if target_day not in legacy_day:
                                print("이틀이상 연재되는 작품이므로 day를 추가합니다. = %s " % target.webtoonName)
                                vo.day = legacy_day + " %s" % target_day
                                CrawlDAO.updateDay(vo)

                                if day == 8:
                                    legacy_webtoonList[j].day = day + 1
                                elif day < 8:
                                    legacy_webtoonList[j].day = day
                                if CrawlDAO.isCrawlExist(legacy_webtoonList[j].webtoonId, legacy_webtoonList[j].day) == 0:
                                    CrawlDAO.insertCrawlList(legacy_webtoonList[j])
                                break
                            else:
                                print("%s는 잘 등록된 상태입니다." % target.webtoonName)

            print("검색은 끝났습니다 @" + target.webtoonName)

        #최초크롤
        elif legacy_count <= 0:
            print("데이터가 없습니다. 최초 크롤입니다.")
            for webtoon in real_webtoonList:
                if CrawlDAO.isWebtoonExist(self.wb_platform, webtoon.webtoonName) is not True:
                    CrawlDAO.insertWebtoon(webtoon)
                    if day == 8:
                        webtoon.day = day + 1
                    elif day < 8:
                        webtoon.day = day
                    CrawlDAO.insertCrawlList(webtoon)
                else:
                    #검색중인 웹툰이 다른요일 혹은 같은 요일에 존재하면
                    # 찾은웹툰 원본 / 실제 day 다르면 day 추가 후 update
                    print("존재 합니다. 망했습니다 ㅠㅜㅠㅜㅠㅜ")
                    vo = CrawlDAO.getWebtoonVO(self.wb_platform, webtoon.webtoonName)

                    legacy_day = CrawlDAO.getWebtoonDay(self.wb_platform, webtoon.webtoonName)
                    target_day = str(day)

                    if legacy_day not in target_day:
                        print("이틀이상 연재되는 작품이므로 day를 추가합니다. = %s " % webtoon.webtoonName)
                        vo.day = legacy_day + " %s" % target_day
                        CrawlDAO.updateDay(vo)
                    else:
                        print("있습니다.")

        # 완결인식
        for i in range(len(flag_list)):

            if flag_list[i] == 0:
                compare_day = self.isDayChange(legacy_webtoonList[i])
                print("compare_day = %s" % compare_day)
                if compare_day.strip() == "":
                    legacy_webtoonList[i].day = "9"
                    CrawlDAO.updateDay(legacy_webtoonList[i])
                    print(legacy_webtoonList[i].webtoonName + "은 완결로 이동하였습니다.")

                elif compare_day.strip() != "":
                    legacy_webtoonList[i].day = compare_day
                    CrawlDAO.updateDay(legacy_webtoonList[i])
                    print(legacy_webtoonList[i].webtoonName + "은 연재 날짜가 바뀌었습니다.")

    #어느 날짜로 이동해야할지 체크
    def isDayChange(self, WebtoonVO):
        print("날짜가 바뀌었나요?")

        daylist1 = [None, "content", "content", "content", "content", "content", "content", "content", "submenu"]
        daylist2 = [None, "2", "3", "4", "5", "6", "7", "8", "7"]
        compare_day = "1 2 3 4 5 6 7"

        for i in range(1, 9):

            flag = 0
            day1 = daylist1[i]
            day2 = daylist2[i]
            driver.find_element_by_css_selector("#%s > ul > li:nth-child(%s) > a" % (day1, day2)).click()
            wb_name = driver.find_elements_by_css_selector("#%s > div.list_area > ul > li > dl > dt > a" % day1)

            print(len(wb_name))
            print("%s요일에서  %s를 찾습니다" % (day2, WebtoonVO.webtoonName))

            for j in range(1, len(wb_name)+1):
                print("돌아라")
                if wb_name[j-1].get_attribute("title") == WebtoonVO.webtoonName:
                    print("%d요일 %d번째에서 %s을 찾았다." % (i, j, wb_name[j-1].text))
                    flag = 1

            if flag == 0:
                compare_day = compare_day.replace(str(i), "")

        return compare_day.strip()

    def initRoop(self):
        print("@@@@ ROOP CRAWLIST @@@@")
        now = datetime.datetime.now().date()
        crawl_list = CrawlDAO.getCrawlList(self.wb_platform)
        count = len(crawl_list)

        print(count)

        for i in range(count):
            isInsert = 0
            target= crawl_list[i]
            print("%d번째 target의 이름은 "%i + target.webtoonName + "입니다.")
            print("target의 라스트데이트는 = %s"%target.lastDate)
            target_episodeList = self.findWebtoon(target)

            for j in range(len(target_episodeList)):
                CrawlDAO.insertEpisode(target_episodeList[j])
                if target_episodeList[j].episodeDate != target.lastDate or target_episodeList[j].episode != target.lastEpisode:
                    print("EPISODE를 추가합니다.")
                    isInsert = 1

            if isInsert == 1 or count == 0:
                print("Crawllist에서 삭제")
                CrawlDAO.deleteCrawlist(target.webtoonId)

        test = CrawlDAO.getCrawlList(self.wb_platform)
        print("CRAWLIST 남은 웹툰 = %d개" %len(test))
        driver.get("http://comic.naver.com/webtoon/weekday.nhn")
        return test

    def roopNaverCrawllist(self):
        print("@@@@ ROOP CRAWLIST @@@@")
        now = datetime.datetime.now().date()
        crawl_list = CrawlDAO.getCrawlList(self.wb_platform)
        count = len(crawl_list)

        print(count)

        for i in range(count):
            isInsert = 0
            target= crawl_list[i]
            print("%d번째 target의 이름은 "%i + target.webtoonName + "입니다.")
            print("target의 라스트데이트는 = %s"%target.lastDate)
            target_episodeList = self.findWebtoon(target)
            #print("에피소드의 카운트는 = %d" %target_episodeList[i].count)
            for j in range(len(target_episodeList)):
                compare_date = datetime.datetime.strptime(str(target_episodeList[j].episodeDate) + " 12:00:00", '%Y-%m-%d %H:%M:%S')
                compare_date = compare_date.date()

                if target_episodeList[j].episodeDate != target.lastDate or target_episodeList[j].episode != target.lastEpisode:
                    print("EPISODE를 추가합니다.")
                    CrawlDAO.insertEpisode(target_episodeList[j])

                    #30일 이상차면 휴제로 생각하고

                    if int(target.day) <= 7 and int(target.day) == int(compare_date.weekday()) and (now - compare_date < datetime.timedelta(6)) == True:
                        print("열흘")
                        print("오늘 = " + str(now))
                        print("웹툰날짜 =" + str(compare_date))
                        print("정확한 데이터를 긁었습니다. 평일")
                        isInsert =1

                    elif int(target.day) == 8 and (now - compare_date < datetime.timedelta(11)) == True:
                        print("정확한 데이터를 긁었습니다. 열흘")
                        isInsert =1

            if isInsert == 1:
                print("Crawllist에서 삭제")
                CrawlDAO.deleteCrawlist(target.webtoonId)

        test = CrawlDAO.getCrawlList(self.wb_platform)
        print("CRAWLIST 남은 웹툰 = %d개" % len(test))
        return test