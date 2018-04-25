class WebtoonVO():

	def __init__(self,  platform, day, webtoonId, webtoonName, writer, webtoonThumbnail, webtoonIntroduce, genre, isNew, lastDate, myThumbnail):
		self.__webtoonId = webtoonId
		self.__webtoonName = webtoonName
		self.__webtoonThumbnail = webtoonThumbnail
		self.__isNew = isNew
		self.lastDate = lastDate
		self.__webtoonIntroduce = webtoonIntroduce
		self.__writer = writer
		self.__platform = platform
		self.__genre = genre
		self.__day = day
		self.__myThumbnail = myThumbnail

	@property
	def webtoonId(self):
		return self.__webtoonId
	@webtoonId.setter
	def webtoonId(self,webtoonId):
		self.__webtoonId = webtoonId
		
	@property
	def webtoonName(self):
		return self.__webtoonName
	@webtoonName.setter
	def webtoonName(self,webtoonName):
		self.__webtoonName = webtoonName
		
	@property
	def webtoonThumbnail(self):
		return self.__webtoonThumbnail
	@webtoonThumbnail.setter
	def webtoonThumbnail(self,webtoonThumbnail):
		self.__webtoonThumbnail = webtoonThumbnail
		
	@property
	def isNew(self):
		return self.__isNew
	@isNew.setter
	def isNew(self,isNew):
		self.__isNew = isNew
		
	@property
	def lastDate(self):
		return self.__lastDate
	@lastDate.setter
	def lastDate(self,lastDate):
		self.__lastDate = lastDate

	@property
	def webtoonIntroduce(self):
		return self.__webtoonIntroduce
	@webtoonIntroduce.setter
	def webtoonIntroduce(self, webtoonIntroduce):
		self.__webtoonIntroduce = webtoonIntroduce

	@property
	def writer(self):
		return self.__writer
	@writer.setter
	def writer(self,writer):
		self.__writer = writer

	@property
	def platform(self):
		return self.__platform
	@platform.setter
	def platform(self,platform):
		self.__platform = platform

	@property
	def genre(self):
		return self.__genre
	@genre.setter
	def genre(self,genre):
		self.__genre = genre

	@property
	def day(self):
		return self.__day
	@day.setter
	def day(self,day):
		self.__day = day

	@property
	def episodeList(self):
		return self.__episodeList
	@episodeList.setter
	def episodeList(self,episodeList):
		self.__episodeList = episodeList

	@property
	def myThumbnail(self):
		return self.__myThumbnail

	@myThumbnail.setter
	def myThumbnail(self, myThumbnail):
		self.__myThumbnail = myThumbnail


class EpisodeVO():

	def __init__(self, indexNumber, webtoonId, episode, episodeThumbnail, episodeLink, episodeDate, charge, myEpisodeThumbnail):
		self.__webtoonId = webtoonId
		self.__episode = episode
		self.__episodeThumbnail = episodeThumbnail
		self.__episodeLink = episodeLink
		self.__episodeDate = episodeDate
		self.__charge = charge
		self.__indexNumber = indexNumber
		self.__myEpisodeThumbnail = myEpisodeThumbnail

	@property
	def webtoonId(self):
		return self.__webtoonId
	@webtoonId.setter
	def webtoonId(self,webtoonId):
		self.__webtoonId = webtoonId
		
	@property
	def episode(self):
		return self.__episode
	@episode.setter
	def episode(self,episode):
		self.__episode = episode
		
	@property
	def episodeThumbnail(self):
		return self.__episodeThumbnail
	@episodeThumbnail.setter
	def episodeThumbnail(self,episodeThumbnail):
		self.__episodeThumbnail = episodeThumbnail
		
	@property
	def episodeLink(self):
		return self.__episodeLink
	@episodeLink.setter
	def episodeLink(self,episodeLink):
		self.__episodeLink = episodeLink
		
	@property
	def episodeDate(self):
		return self.__episodeDate
	@episodeDate.setter
	def episodeDate(self,episodeDate):
		self.__episodeDate = episodeDate

	@property
	def charge(self):
		return self.__charge
	@charge.setter
	def charge(self, charge):
		self.__charge = charge

	@property
	def count(self):
		return self.__count
	@charge.setter
	def count(self, count):
		self.__count = count

	@property
	def indexNumber(self):
		return self.__indexNumber
	@indexNumber.setter
	def indexNumber(self, indexNumber):
		self.__indexNumber = indexNumber

	@property
	def myEpisodeThumbnail(self):
		return self.__myEpisodeThumbnail
	@myEpisodeThumbnail.setter
	def myEpisodeThumbnail(self, myEpisodeThumbnail):
		self.__myEpisodeThumbnail = myEpisodeThumbnail

class CrawllistVO():

	def __init__(self, webtoonId, webtoonName, lastDate, lastEpisode, platform, day):
		self.__webtoonId = webtoonId
		self.__webtoonName = webtoonName
		self.__lastDate = lastDate
		self.__lastEpisode = lastEpisode
		self.__platform = platform
		self.__day = day

	@property
	def webtoonId(self):
		return self.__webtoonId
	@webtoonId.setter
	def webtoonId(self, webtoonId):
		self.__webtoonId = webtoonId

	@property
	def webtoonName(self):
		return self.__webtoonName
	@webtoonName.setter
	def webtoonName(self, webtoonName):
		self.__webtoonName = webtoonName

	@property
	def lastDate(self):
		return self.__lastDate
	@lastDate.setter
	def lastDate(self, lastDate):
		self.lastDate = lastDate

	@property
	def lastEpisode(self):
		return self.__lastEpisode
	@lastEpisode.setter
	def lastEpisode(self, lastEpisode):
		self.lastEpisode = lastEpisode

	@property
	def platform(self):
		return self.__platform
	@platform.setter
	def platform(self,platform):
		self.__platform = platform

	@property
	def day(self):
		return self.__day
	@day.setter
	def day(self,day):
		self.__day = day