import datetime
from .base import BandoriObject


###############################################################################
# Bandori Party models

class PCard(BandoriObject):
    '''
    Represents a bang dream card.
    '''
    def __init__(self, data: dict):
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
        self.performance_min = data.get("performance_min")
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

        d = self._api_get(id=[self.member], url=self.URL_PARTY+'members/')

        return PMember(d[0])

    def get_cameo_members(self):

        d = self._api_get(id=self.cameo, url=self.URL_PARTY+'members/')

        return [PMember(data) for data in d]


class PMember(BandoriObject):
    '''
    Represents a bang dream member.
    '''
    def __init__(self, data: dict):
        super().__init__(data)
        self.name = data.get("name")
        self.japanese_name = data.get("japanese_name")
        self.image = data.get("image")
        self.square_image = data.get("square_image")
        self.band = data.get("i_band")  # TODO: match band to Band object?
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


class PEvent(BandoriObject):
    '''
    Represents a bang dream game event.
    '''

    def __init__(self, data: dict):
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
        self.boost_members = data.get("boost_members")

    def get_start_date(self, region='en'):
        if region == 'en':
            if self.english_start_date is not None:
                return datetime.datetime.strptime(
                    self.english_start_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1
        elif region == 'jp':
            if self.jp_start_date is not None:
                return datetime.datetime.strptime(
                    self.jp_start_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1
        elif region == 'tw':
            if self.tw_start_date is not None:
                return datetime.datetime.strptime(
                    self.tw_start_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1
        else:
            if self.kr_start_date is not None:
                return datetime.datetime.strptime(
                    self.kr_start_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1

    def get_end_date(self, region='en'):
        if region == 'en':
            if self.english_end_date is not None:
                return datetime.datetime.strptime(
                    self.english_end_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1
        elif region == 'jp':
            if self.jp_end_date is not None:
                return datetime.datetime.strptime(
                    self.jp_end_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1
        elif region == 'tw':
            if self.tw_end_date is not None:
                return datetime.datetime.strptime(
                    self.tw_end_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1
        else:
            if self.kr_end_date is not None:
                return datetime.datetime.strptime(
                    self.kr_end_date, '%Y-%m-%dT%H:%M:%SZ')
            else:
                return -1

    def get_main_card(self):

        data = self._api_get(id=[self.main_card],
                             url=self.URL_PARTY+'cards/')

        return PCard(data[0])

    def get_secondary_card(self):

        data = self._api_get(id=[self.secondary_card],
                             url=self.URL_PARTY+'cards/')

        return PCard(data[0])

    def get_boost_members(self):

        d = self._api_get(id=self.boost_attribute,
                          url=self.URL_PARTY+'members/')

        return [PMember(data) for data in d]


class PCostume(BandoriObject):
    '''
    Represents a bang dream costume.
    '''
    def __init__(self, data: dict):
        super().__init__(data)
        self.type = data.get("i_costume_type")
        self.card = data.get("card")
        self.member = data.get("member")
        self.name = data.get("name")

        self.display_image = data.get("display_image")

    def get_costume_member(self):

        data = self._api_get(id=[self.member], url=self.URL_PARTY+'members/')

        return PMember(data[0])

    def get_costume_card(self):

        d = self._api_get(id=[self.card], url=self.URL_PARTY+'cards/')

        return PCard(d[0])


class PItem(BandoriObject):
    '''
    Represents a bang dream in-game item
    '''
    def __init__(self, data: dict):
        super().__init__(data)
        self.name = data.get("name")
        self.type = data.get("i_type")
        self.description = data.get("m_description")
        self.image = data.get("image")


class PAreaItem(BandoriObject):
    '''
    Represents a bang dream area item
    '''
    def __init__(self, data):
        super().__init__(data)
        self.name = data.get("name")
        self.image = data.get("image")
        self.area = data.get("area")    # TODO: name of area??
        self.type = data.get("i_type")
        self.instrument = data.get("i_instrument")
        self.attribute = data.get("i_attribute")
        self.boost_stat = data.get("i_boost_stat")
        self.max_level = data.get("max_level")
        self.values = data.get("value_list")
        self.description = data.get("about")


class PAsset(BandoriObject):
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


class PComic(PAsset):
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

        d = self._api_get(id=self.cameo, url=self.URL_PARTY+'members/')

        return [PMember(data) for data in d]


class PBackground(PAsset):
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


class PStamp(PAsset):
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

    def get_stamp_members(self):

        d = self._api_get(id=self.members, url=self.URL_PARTY+'members/')

        return [PMember(data) for data in d]


class PTitle(PAsset):
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

        d = self._api_get(id=[self.event], url=self.URL_PARTY+'events/')

        return PEvent(d[0])


class PInterface(PAsset):
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


class POfficialArt(PAsset):
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

#############################################################################
