import CrawlDAO
from ControlToonVO import WebtoonVO
platform = "Naver"
webtoonName = "팀피닉스"
vo = WebtoonVO(platform, "0", "10", "1", "1", "1", "1", "1", "1", "2011-11-11", "1")


print(CrawlDAO.getLastEpisode("d")==[None])
#print(legacy_thumbnail)
#print(a[0])
#print(a[0][0])

