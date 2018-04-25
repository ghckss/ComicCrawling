# platform, webtoon, webtoon_info, writer 관련 Table객체
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.dialects.mysql import TINYINT
from GetConnection import Base

class WebtoonTable(Base):
	__tablename__ = 'webtoon'
	webtoonId = Column(String, primary_key=True)
	webtoonName = Column(String)
	webtoonThumbnail = Column(String)
	webtoonIntroduce = Column(String)
	isNew = Column(TINYINT)
	lastDate = Column(Date)
	myThumbnail = Column(String)

	def __init__(self, WebtoonVO):
		self.webtoonId = WebtoonVO.webtoonId
		self.webtoonName = WebtoonVO.webtoonName
		self.webtoonThumbnail = WebtoonVO.webtoonThumbnail
		self.isNew = WebtoonVO.isNew
		self.lastDate = WebtoonVO.lastDate
		self.webtoonIntroduce = WebtoonVO.webtoonIntroduce
		self.myThumbnail = WebtoonVO.myThumbnail

class WriterTable(Base):
	__tablename__ = 'writer'
	webtoonId = Column(String, primary_key=True)
	writer = Column(String)

	def __init__(self, WebtoonVO):
		self.webtoonId = WebtoonVO.webtoonId
		self.writer = WebtoonVO.writer

class PlatformTable(Base):
	__tablename__ = 'platform'
	webtoonId = Column(String, primary_key=True)
	platform = Column(String)

	def __init__(self, WebtoonVO):
		self.webtoonId = WebtoonVO.webtoonId
		self.platform = WebtoonVO.platform

class GenreTable(Base):
	__tablename__ = 'genre'
	webtoonId = Column(String, primary_key=True)
	genre = Column(String)

	def __init__(self, WebtoonVO):
		self.webtoonId = WebtoonVO.webtoonId
		self.genre = WebtoonVO.genre

class DayTable(Base):
	__tablename__ = 'day'
	webtoonId = Column(String, primary_key=True)
	day = Column(String)

	def __init__(self, WebtoonVO):
		self.webtoonId = WebtoonVO.webtoonId
		self.day = WebtoonVO.day

class EpisodeTable(Base):
	__tablename__ = 'episode'
	indexNumber = Column(Integer, primary_key=True)
	webtoonId = Column(String, primary_key=True)
	episode = Column(String)
	episodeThumbnail = Column(String)
	episodeLink = Column(String)
	episodeDate = Column(Date)
	charge = Column(String)
	myEpisodeThumbnail = Column(String)

	def __init__(self, EpisodeVO):
		self.indexNumber = EpisodeVO.indexNumber
		self.webtoonId = EpisodeVO.webtoonId
		self.episode = EpisodeVO.episode
		self.episodeThumbnail = EpisodeVO.episodeThumbnail
		self.episodeLink = EpisodeVO.episodeLink
		self.episodeDate = EpisodeVO.episodeDate
		self.charge = EpisodeVO.charge
		self.myEpisodeThumbnail = EpisodeVO.myEpisodeThumbnail

class CrawllistTable(Base):
	__tablename__ = 'crawllist'
	webtoonId = Column(String, primary_key=True)
	webtoonName = Column(String)
	lastDate = Column(DateTime)
	lastEpisode = Column(String)
	platform = Column(String)
	day = Column(String)

	def __init__(self, webtoonId, webtoonName, lastDate, lastEpisode, platform, day):
		self.webtoonId = webtoonId
		self.webtoonName = webtoonName
		self.lastDate = lastDate
		self.lastEpisode = lastEpisode
		self.platform = platform
		self.day = day