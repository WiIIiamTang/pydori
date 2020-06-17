import requests
import datetime
from .base import *
from ..loader import BandoriLoader


###############################################################################
# Bandori Database models

class Band(BandoriObject):
    '''
    Represents a bang dream band
    '''
    def __init__(self, data : dict, id_name = 'bandId', region = 'en/'):
        super().__init__(data, id_name, region)
        self.name = data.get("bandName")
        self.introduction = data.get("introductions")
        self.type = data.get("bandType")


        # This needs to be changed later to use bandori database api:

        # IDs for bandori.party api
        self.members = [data.get("leader", -5)+5, data.get("member1", -5)+5,
                         data.get("member2", -5)+5, data.get("member3", -5)+5, data.get("member4", -5)+5]

        # bands past Roselia have messed up members.
    

    # TODO: This method needs to be rewritten for bandori database api
    '''
    def get_band_members(self):
        
        d = self.bl._api_get(id=self.members, url=self.URL_PARTY+'members/')

        return [Member(data) for data in d]
    '''

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



