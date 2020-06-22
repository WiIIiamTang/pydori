import datetime
from .base import BandoriObject

###############################################################################
# Bandori Database models


class DCard(BandoriObject):
    '''
    Represents a bang dream card
    '''
    def __init__(self, data: dict, id_name='cardId', region='en/'):
        super().__init__(data, id_name, region)
        self.character_id = data.get("characterId")
        self.rarity = data.get("rarity")
        self.attribute = data.get("attr")
        self.skill_id = data.get("skillId")
        self.title = data.get("title")
        self.level_limit = data.get("levelLimit")
        self.res_link = (self.URL_GA_RES
                         + '/assets/characters/resourceset/'
                         + data.get("cardRes")  # TODO finish url
                         )
        self.live2d_link = (self.URL_GA_RES
                            + '/assets/characters/resourceset/'
                            + data.get("live2dRes"))  # TODO finish url
        self.costume_id = data.get("costumeId")
        self.released_at = data.get("releasedAt")
        self.min_stats = data.get("simpleParams").get("min")
        self.max_stats = data.get("simpleParams").get("max")

    def get_skill(self):
        d = self._api_get(url=self.URL_GA + 'skill/' + str(self.skill_id),
                          party=False
                          )

        return DSkill(data=d, region=self.region)


class DSkill(BandoriObject):
    '''
    Represents a Card's skill.
    '''
    def __init__(self, data: dict, id_name='skillId', region='en/'):
        super().__init__(data, id_name, region)
        self.skill_level = data.get("skillLevel")
        self.duration = data.get("duration")
        self.short_description = data.get("simpleDescription")
        self.description = data.get("description")
        self.skill_type = data.get("skillSortType")


class DMember(BandoriObject):
    '''
    Represents a bang dream member.
    Referred to as Character in bandori database.
    '''
    def __init__(self, data: dict, id_name='characterId', region='en/'):
        super().__init__(data, id_name, region)
        self.character_type = data.get("characterType")
        self.band_id = data.get("bandId")
        self.name = data.get("characterName")
        self.ruby = data.get("ruby")


class DDegree(BandoriObject):
    '''
    Represents a ranking from bang dream event.
    '''
    def __init__(self, data: dict, id_name='degreeId', region='en/'):
        super().__init__(data, id_name, region)
        self.seq = data.get("seq")
        self.image_name = data.get("imageName")
        self.degree_rank = data.get("degreeRank")
        self.degree_name = data.get("degreeName")
        self.degree_type = data.get("degreeType")
        self.icon = data.get("iconImageName")
        self.description = data.get("description")


class DComic(BandoriObject):
    '''
    Represents a loading screen koma.
    '''
    def __init__(self, data: dict, 
                 id_name='singleFrameCartoonId', region='en/'):
        super().__init__(data, id_name, region)
        self.title = data.get("title")
        self.asset_name = data.get("assetBundleName")
        self.seq = data.get("seq")
        self.subTitle = data.get("subTitle")
        self.asset_link = (self.URL_GA_RES
                           + data.get("assetAddress")
                           )


class DStamp(BandoriObject):
    '''
    Represents a stamp
    '''
    def __init__(self, data, id_name='stampId', region='en/'):
        super().__init__(data, id_name=id_name, region=region)
        self.seq = data.get("seq")
        self.image_link = data.get("imageName")  # TODO get link
        self.type = data.get("stampType")


class DBand(BandoriObject):
    '''
    Represents a bang dream band
    '''
    def __init__(self, data: dict, id_name='bandId', region='en/'):
        super().__init__(data, id_name, region)
        self.name = data.get("bandName")
        self.introduction = data.get("introductions")
        self.type = data.get("bandType")
        self.members = [data.get("leader", -5), data.get("member1", -5),
                        data.get("member2", -5), data.get("member3", -5),
                        data.get("member4", -5)]

        # Note: bands past Roselia have messed up members.

    def get_band_members(self):
        d = self._api_get(id=self.members,
                          url=self.URL_GA+'chara/',
                          party=False)

        return [DMember(data) for data in d]


class DSong(BandoriObject):
    '''
    Represents a playable song in bang dream
    '''
    def __init__(self, data: dict, id_name='musicId', region='en/'):
        super().__init__(data, id_name, region)
        self.title = data.get("title")
        self.bgm = self.URL_GA_RES + data.get("bgmFile", '')
        self.thumb = self.URL_GA_RES + data.get("thumb", '')
        self.jacket = self.URL_GA_RES + data.get("jacket", '')
        self.band_name = data.get("bandName")
        self.band = data.get("bandId")
        self.difficulty = data.get("difficulty")
        self.how_to_get = data.get("howToGet")
        self.achievements = data.get("achievements")
        self.published_at = data.get("publishedAt")
        self.closed_at = data.get("closedAt")

        self.composer = data.get("composer")
        self.lyricist = data.get("lyricist")
        self.arranger = data.get("arranger")


class DGacha(BandoriObject):
    '''
    Represents a gacha in bang dream
    '''
    def __init__(self, data: dict, id_name='gachaId', region='en/'):
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
