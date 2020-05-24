import requests
import datetime
from .bandori_loader import BandoriLoader

class BandoriObject:
    '''
    Represents information retrieved from the api
    as an object
    '''
    
    def __init__(self, data : dict, id_name = 'id', region = 'en/'):
        self.URL_PARTY = "https://bandori.party/api/"
        self.URL_GA = "https://api.bandori.ga/v1/" + region # english server default
        self.URL_GA_RES = "https://res.bandori.ga"

        self.id = data[id_name]
        self.data = data
    
    def __lt__(self, other):
        return self.id < other.id

class Card(BandoriObject):
    '''
    Represents a bang dream card.
    '''
    def __init__(self, data : dict):
        super().__init__(data)
        # not all attributes are listed.
        self.member = data["member"]
        self.rarity = data["i_rarity"]
        self.attribute = data["i_attribute"]
        self.name = data["name"]
        self.japanese_name = data["japanese_name"]
        self.skill_type = data["i_skill_type"]
        self.cameo = data["cameo_members"]
    
    def get_card_member(self):
        b = BandoriLoader()
        data = b._api_get(id=[self.member], url=self.URL_PARTY+'members/')

        return Member(data[0])
    
    def get_cameo_members(self):
        b = BandoriLoader()
        d = b._api_get(id=self.cameo, url=self.URL_PARTY+'members/')

        return [Member(data) for data in d]

class Member(BandoriObject):
    '''
    Represents a bang dream member.
    '''
    def __init__(self, data : dict):
        super().__init__(data)
        self.name = data["name"]
        self.japanese_name = data["japanese_name"]
        self.band = data["i_band"]                    # TODO: match band to Band object
        self.school = data["school"]
        self.year = data["i_school_year"]
        self.romaji_cv = data["romaji_CV"]
        self.cv = data["CV"]
        self.birthday = data["birthday"]
        self.food_likes = data["food_like"]
        self.food_dislikes = data["food_dislike"]
        self.astro = data["i_astrological_sign"]
        self.instrument = data["instrument"]
        self.description = data["description"]
        
class Event:
    '''
    Represents a bang dream game event.
    '''
            # TODO: event id not available.

    def __init__(self, data : dict, region = 'en/'):
        self.URL_PARTY = "https://bandori.party/api/"
        self.URL_GA = "https://api.bandori.ga/v1/" + region
        self.URL_GA_RES = "https://res.bandori.ga/assets/"

        self.name = data["name"]
        self.data = data
        
        self.japanese_name = data["japanese_name"]
        self.type = data["i_type"]

        self.english_start_date = data["english_start_date"]
        self.english_end_date = data["english_end_date"]
        self.jp_start_date = data["start_date"]
        self.jp_end_date = data["end_date"]
        self.tw_start_date = data["taiwanese_start_date"]
        self.tw_end_date = data["taiwanese_end_date"]
        self.kr_start_date = data["korean_start_date"]
        self.kr_end_date = data["korean_end_date"]

        self.versions_available = data["c_versions"]
        self.main_card = data["main_card"]
        self.secondary_card = data["secondary_card"]
        self.boost_attribute = data["i_boost_attribute"]
        self.boost_members = data["boost_members"]

    def get_start_date(self, region = 'en'):
        if region == 'en':
            if self.english_start_date is not None: 
                return datetime.datetime.strptime(self.english_start_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1
        elif region == 'jp':
            if self.jp_start_date is not None:
                return datetime.datetime.strptime(self.jp_start_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1
        elif region == 'tw':
            if self.tw_start_date is not None:
                return datetime.datetime.strptime(self.tw_start_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1
        else:
            if self.kr_start_date is not None:
                return datetime.datetime.strptime(self.kr_start_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1
    
    def get_end_date(self, region = 'en'):
        if region == 'en':
            if self.english_end_date is not None: 
                return datetime.datetime.strptime(self.english_end_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1
        elif region == 'jp':
            if self.jp_end_date is not None:
                return datetime.datetime.strptime(self.jp_end_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1
        elif region == 'tw':
            if self.tw_end_date is not None:
                return datetime.datetime.strptime(self.tw_end_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1
        else:
            if self.kr_end_date is not None:
                return datetime.datetime.strptime(self.kr_end_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1
    
    def get_main_card(self):
        b = BandoriLoader()
        data = b._api_get(id=[self.main_card], url=self.URL_PARTY+'card/')

        return Card(data[0])
    
    def get_secondary_card(self):
        b = BandoriLoader()
        data = b._api_get(id=[self.secondary_card], url=self.URL_PARTY+'card/')

        return Card(data[0])

    def get_boost_members(self):
        b = BandoriLoader()
        d = b._api_get(id=self.boost_attribute, url=self.URL_PARTY+'members/')

        return [Member(data) for data in d]

class Costume(BandoriObject):
    '''
    Represents a bang dream costume.
    '''
    def __init__(self, data : dict):
        super().__init__(data)
        self.type = data["i_costume_type"]
        self.card = data["card"]
        self.member = data["member"]
        self.name = data["name"]
    
    def get_costume_member(self):
        b = BandoriLoader()
        data = b._api_get(id=[self.member], url=self.URL_PARTY+'members/')

        return Member(data[0])
    
    def get_costume_card(self):
        b = BandoriLoader()
        data = b._api_get(id=[self.card], url=self.URL_PARTY+'cards/')

        return Card(data[0])

class Item(BandoriObject):
    '''
    Represents a bang dream in-game item
    '''
    def __init__(self, data : dict):
        super().__init__(data)
        self.name = data["name"]
        self.type = data["i_type"]
        self.description = data["m_description"]

class AreaItem(BandoriObject):
    '''
    Represents a bang dream area item
    '''
    def __init__(self, data):
        super().__init__(data)
        self.name = data["name"]
        self.area = data["area"] # TODO: match area to string (name of area)
        self.type = data["i_type"]
        self.instrument = data["i_instrument"]
        
        self.attribute = data["i_attribute"]
        self.stat = data["i_boost_stat"]
        self.max_level = data["max_level"]
        self.values = data["value_list"]
        self.description = data["about"]


class Asset(BandoriObject):
    '''
    Represents a bang dream asset as defined by bandori.party

    Known assets:
    comic
    background
    stamp
    title
    interface
    officialart
    '''
    def __init__(self, data):
        super().__init__(data)
        self.type = data["i_type"]

class Comic(Asset):
    def __init__(self, data):
        super().__init__(data)
        self.name = data["name"]
        self.members = data["members"]
    
    def get_comic_members(self):
        b = BandoriLoader()
        d = b._api_get(id=self.cameo, url=self.URL_PARTY+'members/')

        return [Member(data) for data in d]

class Background(Asset):
    def __init__(self, data):
        super().__init__(data)
        self.name = data["name"]

class Stamp(Asset):
    def __init__(self, data):  
        super().__init__(data)
        self.name = data["name"]
        self.members = data["members"]
    
    def get_stamp_members(self):
        b = BandoriLoader()
        d = b._api_get(id=self.members, url=self.URL_PARTY+'members/')

        return [Member(data) for data in d]

class Title(Asset):
    def __init__(self, data):
        super().__init__(data)
        self.event = data["event"]
        self.value = data["value"]

    def title_event(self):
        b = BandoriLoader()
        d = b._api_get(id=[self.event], url=self.URL_PARTY+'events/')

        return Event(d[0])
    

class Interface(Asset):
    def __init__(self, data):
        super().__init__(data)
        self.name = data["name"]

class OfficialArt(Asset):
    def __init__(self, data):
        super().__init__(data)
        



################################################################
# The following would be the result of interaction with bandori.ga api

class Band(BandoriObject):
    '''
    Represents a bang dream band
    '''
    def __init__(self, data : dict, id_name = 'bandId', region = 'en/'):
        super().__init__(data, id_name, region)
        self.name = data["bandName"]
        self.introduction = data["introductions"]

        # IDs for bandori.party api
        self.members = [data["leader"]+5, data["member1"]+5, data["member2"]+5, data["member3"]+5, data["member4"]+5]

        # bands past Roselia have messed up members.
    
    def get_band_members(self):
        b = BandoriLoader()
        d = b._api_get(id=self.members, url=self.URL_PARTY+'members/')

        return [Member(data) for data in d]

class Song(BandoriObject):
    '''
    Represents a playable song in bang dream
    '''
    def __init__(self, data : dict, id_name = 'musicId', region = 'en/'):
        super().__init__(data, id_name, region)
        self.title = data["title"]
        self.bgm = self.URL_GA_RES + data["bgmFile"]
        self.thumb = self.URL_GA_RES + data["thumb"]
        self.jacket = self.URL_GA_RES + data["jacket"]
        self.band_name = data["bandName"]
        self.band = data["bandId"]
        self.difficulty = data["difficulty"]
        self.how_to_get = data["howToGet"]
        self.composer = data["composer"]
        self.lyricist = data["lyricist"]

class Gacha(BandoriObject):
    '''
    Represents a gacha in bang dream
    '''
    def __init__(self, data : dict, id_name = 'gachaId', region = 'en/'):
        super().__init__(data, id_name, region)
        self.name = data["gachaName"]
        self.start_date = data["publishedAt"]
        self.end_date = data["closedAt"]
        self.description = data["description"]
        
        self.period = data["gachaPeriod"]
        self.type = data["gachaType"]
    
    def get_start_date(self):
        return datetime.datetime.fromtimestamp(int(self.start_date) / 1000)
    
    def get_end_date(self):
        return datetime.datetime.fromtimestamp(int(self.end_date) / 1000)



