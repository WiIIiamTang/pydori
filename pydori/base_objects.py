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

        self.id = data.get(id_name)
        self.data = data
        self.bl = BandoriLoader()
    
    def __lt__(self, other):
        return self.id < other.id
    
    def __str__(self):
        return str(self.data)

class Card(BandoriObject):
    '''
    Represents a bang dream card.
    '''
    def __init__(self, data : dict):
        super().__init__(data)
        
        self.member = data.get("member")
        self.rarity = data.get("i_rarity")
        self.attribute = data.get("i_attribute")
        self.name = data.get("name")
        self.japanese_name = data.get("japanese_name")
        self.is_promo = data.get("is_promo")
        self.is_original = data.get("is_original")
        self.image = data.get("image")
        self.image_trained = data.get("image_trained")
        self.art = data.get("art")
        self.art_trained = data.get("art_trained")
        self.transparent = data.get("transparent")
        self.transparent_trained = data.get("transparent_trained")
        self.skill_name = data.get("skill_name")
        self.japanese_skill_name = data.get("japanese_skill_name")
        self.skill_type = data.get("i_skill_type")
        self.side_skill_type = data.get("i_side_skill_type")
        self.skill_template = data.get("skill_template")
        self.skill_variables = data.get("skill_variables")
        self.side_skill_template = data.get("side_skill_template")
        self.side_skill_variables = data.get("side_skill_variables")
        self.full_skill = data.get("full_skill")
        self.performance_min = data.get("performnce_min")
        self.performance_max = data.get("performance_max")
        self.performance_trained_max = data.get("performance_trained_max")
        self.technique_min = data.get("technique_min")
        self.technique_max = data.get("technique_max")
        self.technique_trained_max = data.get("technique_trained_max")
        self.visual_min = data.get("visual_min")
        self.visual_max = data.get("visual_max")
        self.visual_trained_max = data.get("visual_trained_max")
        self.cameo = data.get("cameo_members")
    
    def get_card_member(self):
        
        d = self.bl._api_get(id=[self.member], url=self.URL_PARTY+'members/')

        return Member(d[0])
    
    def get_cameo_members(self):
        
        d = self.bl._api_get(id=self.cameo, url=self.URL_PARTY+'members/')

        return [Member(data) for data in d]

class Member(BandoriObject):
    '''
    Represents a bang dream member.
    '''
    def __init__(self, data : dict):
        super().__init__(data)
        self.name = data.get("name")
        self.japanese_name = data.get("japaense_name")
        self.band = data.get("i_band")                    # TODO: match band to Band object
        self.school = data.get("school")
        self.year = data.get("i_school_year")
        self.romaji_cv = data.get("romaji_CV")
        self.cv = data.get("CV")
        self.birthday = data.get("birthday")
        self.food_likes = data.get("food_like")
        self.food_dislikes = data.get("food_dislike")
        self.astro = data.get("i_astrological_sign")
        self.instrument = data.get("instrument")
        self.description = data.get("description")
        
class Event(BandoriObject):
    '''
    Represents a bang dream game event.
    '''

    def __init__(self, data : dict, region = 'en/'):
        super().__init__(data)

        self.name = data.get("name")      
        self.japanese_name = data.get("japanese_name")
        self.type = data.get("i_type")
        self.image = data.get("image")

        self.english_start_date = data.get("english_start_date")
        self.english_end_date = data.get("english_end_date")
        self.jp_start_date = data.get("start_date")
        self.jp_end_date = data.get("end_date")
        self.tw_start_date = data.get("taiwanese_start_date")
        self.tw_end_date = data.get("taiwanese_end_date")
        self.kr_start_date = data.get("korean_start_date")
        self.kr_end_date = data.get("korean_end_date")

        self.versions_available = data.get("c_versions")
        self.main_card = data.get("main_card")
        self.secondary_card = data.get("secondary_card")
        self.boost_attribute = data.get("i_boost_attribute")
        self.boost_stat = data.get("i_boost_stat")
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
        
        data = self.bl._api_get(id=[self.main_card], url=self.URL_PARTY+'card/')

        return Card(data[0])
    
    def get_secondary_card(self):
        
        data = self.bl._api_get(id=[self.secondary_card], url=self.URL_PARTY+'card/')

        return Card(data[0])

    def get_boost_members(self):
        
        d = self.bl._api_get(id=self.boost_attribute, url=self.URL_PARTY+'members/')

        return [Member(data) for data in d]

class Costume(BandoriObject):
    '''
    Represents a bang dream costume.
    '''
    def __init__(self, data : dict):
        super().__init__(data)
        self.type = data.get("i_costume_type")
        self.card = data.get("card")
        self.member = data.get("member")
        self.name = data.get("name")

        self.display_image = data.get("display_image")
    
    def get_costume_member(self):
        
        data = self.bl._api_get(id=[self.member], url=self.URL_PARTY+'members/')

        return Member(data[0])
    
    def get_costume_card(self):
        
        d = self.bl._api_get(id=[self.card], url=self.URL_PARTY+'cards/')

        return Card(d[0])

class Item(BandoriObject):
    '''
    Represents a bang dream in-game item
    '''
    def __init__(self, data : dict):
        super().__init__(data)
        self.name = data.get("name")
        self.type = data.get("i_type")
        self.description = data.get("m_description")
        self.image = data.get("image")

class AreaItem(BandoriObject):
    '''
    Represents a bang dream area item
    '''
    def __init__(self, data):
        super().__init__(data)
        self.name = data.get("name")
        self.image = data.get("image")
        self.area = data.get("area")    # TODO: match area id to a string - name of area (not available through api)
        self.type = data.get("i_type")
        self.instrument = data.get("i_instrument")
        self.attribute = data.get("i_attribute")
        self.boost_stat = data.get("i_boost_stat")
        self.max_level = data.get("max_level")
        self.values = data.get("value_list")
        self.description = data.get("about")


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
        self.type = data.get("i_type")

class Comic(Asset):
    def __init__(self, data):
        super().__init__(data)
        self.name = data.get("name")
        self.members = data.get("members")
        self.image = data.get("image")
        self.english_image = data.get("english_image")
        self.taiwanese_image = data.get("taiwanese_image")
        self.korean_image = data.get("korean_image")
        self.band = data.get("i_band")
        self.tags = data.get("c_tags")
        self.event = data.get("event")
        self.source = data.get("source")
        self.source_link = data.get("source_link")
        self.song = data.get("song")

    def get_comic_members(self):
        
        d = self.bl._api_get(id=self.cameo, url=self.URL_PARTY+'members/')

        return [Member(data) for data in d]

class Background(Asset):
    def __init__(self, data):
        super().__init__(data)
        self.name = data.get("name")
        self.members = data.get("members")
        self.image = data.get("image")
        self.english_image = data.get("english_image")
        self.taiwanese_image = data.get("taiwanese_image")
        self.band = data.get("i_band")
        self.tags = data.get("c_tags")
        self.event = data.get("event")
        self.source = data.get("source")
        self.source_link = data.get("source_link")
        self.song = data.get("song")

class Stamp(Asset):
    def __init__(self, data):  
        super().__init__(data)
        self.name = data.get("name")
        self.members = data.get("members")
        self.image = data.get("image")
        self.english_image = data.get("english_image")
        self.taiwanese_image = data.get("taiwanese_image")
        self.band = data.get("i_band")
        self.tags = data.get("c_tags")
        self.event = data.get("event")
        self.source = data.get("source")
        self.source_link = data.get("source_link")
        self.song = data.get("song")
    
    def get_stamp_members(self):
        
        d = self.bl._api_get(id=self.members, url=self.URL_PARTY+'members/')

        return [Member(data) for data in d]

class Title(Asset):
    def __init__(self, data):
        super().__init__(data)
        self.name = data.get("name")
        self.members = data.get("members")
        self.image = data.get("image")
        self.english_image = data.get("english_image")
        self.taiwanese_image = data.get("taiwanese_image")
        self.korean_image = data.get("korean_image")
        self.band = data.get("i_band")
        self.tags = data.get("c_tags")
        self.event = data.get("event")
        self.source = data.get("source")
        self.source_link = data.get("source_link")
        self.song = data.get("song")
        self.value = data.get("value")

    def get_title_event(self):
        
        d = self.bl._api_get(id=[self.event], url=self.URL_PARTY+'events/')

        return Event(d[0])
    

class Interface(Asset):
    def __init__(self, data):
        super().__init__(data)
        self.name = data.get("name")
        self.members = data.get("members")
        self.image = data.get("image")
        self.english_image = data.get("english_image")
        self.taiwanese_image = data.get("taiwanese_image")
        self.korean_image = data.get("korean_image")
        self.band = data.get("i_band")
        self.tags = data.get("c_tags")
        self.event = data.get("event")
        self.source = data.get("source")
        self.source_link = data.get("source_link")
        self.song = data.get("song")

class OfficialArt(Asset):
    def __init__(self, data):
        super().__init__(data)
        self.name = data.get("name")
        self.members = data.get("members")
        self.image = data.get("image")
        self.english_image = data.get("english_image")
        self.taiwanese_image = data.get("taiwanese_image")
        self.korean_image = data.get("korean_image")
        self.band = data.get("i_band")
        self.tags = data.get("c_tags")
        self.event = data.get("event")
        self.source = data.get("source")
        self.source_link = data.get("source_link")
        self.song = data.get("song")
        



################################################################
# The following would be the result of interaction with bandori.ga api

class Band(BandoriObject):
    '''
    Represents a bang dream band
    '''
    def __init__(self, data : dict, id_name = 'bandId', region = 'en/'):
        super().__init__(data, id_name, region)
        self.name = data.get("bandName")
        self.introduction = data.get("introductions")
        self.type = data.get("bandType")

        # IDs for bandori.party api
        self.members = [data.get("leader", -5)+5, data.get("member1", -5)+5,
                         data.get("member2", -5)+5, data.get("member3", -5)+5, data.get("member4", -5)+5]

        # bands past Roselia have messed up members.
    
    def get_band_members(self):
        
        d = self.bl._api_get(id=self.members, url=self.URL_PARTY+'members/')

        return [Member(data) for data in d]

class Song(BandoriObject):
    '''
    Represents a playable song in bang dream
    '''
    def __init__(self, data : dict, id_name = 'musicId', region = 'en/'):
        super().__init__(data, id_name, region)
        self.title = data.get("title")
        self.bgm = self.URL_GA_RES + data.get("bgmFile", '')
        self.thumb = self.URL_GA_RES + data.get("thumb", '')
        self.jacket = self.URL_GA_RES + data.get("jacket", '')
        self.band_name = data.get("bandName")
        self.band = data.get("bandId")              # The band id is for api.bandori.ga and not, if applicable, for bandori.party api
        self.difficulty = data.get("difficulty")
        self.how_to_get = data.get("howToGet")
        self.achievements = data.get("achievements")
        self.published_at = data.get("publishedAt")
        self.closed_at = data.get("closedAt")

        self.composer = data.get("composer")
        self.lyricist = data.get("lyricist")
        self.arranger = data.get("arranger")


class Gacha(BandoriObject):
    '''
    Represents a gacha in bang dream
    '''
    def __init__(self, data : dict, id_name = 'gachaId', region = 'en/'):
        super().__init__(data, id_name, region)
        self.name = data.get("gachaName")
        self.start_date = data.get("publishedAt")
        self.end_date = data.get("closedAt")
        self.description = data.get("description")
        self.rates = data.get("rates")
        self.annotation = data.get("annotation")
        self.gacha_period = data.get("gachaPeriod")
        self.sub_name = data.get("gachaSubName")
        self.type = data.get("gachaType")
    
    def get_start_date(self):
        return datetime.datetime.fromtimestamp(int(self.start_date) / 1000)
    
    def get_end_date(self):
        return datetime.datetime.fromtimestamp(int(self.end_date) / 1000)



