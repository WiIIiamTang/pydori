from .models.gamodels import (
    DCard,
    DSong,
    DGacha,
    DBand,
    DMember,
    DDegree,
    DComic,
    DStamp,
    DEvent
)
from .loader import BandoriLoader


class DBandoriApi(BandoriLoader):
    '''
    Represents a class that interacts with the bandori database API
    '''

    def __init__(self, region='en/'):
        super().__init__(region)
        self.party = False

    def get_cards(self, id: list = [], filters={}) -> list:
        '''
        Get card by ids, as Card objects.
        If the list is empty, will get all cards.
        '''
        d = self._api_get(id=id, url=self.URL_GA+'card/',
                          party=self.party, filters=filters)

        return [DCard(data, region=self.region) for data in d]

    def get_members(self, id: list = [], filters={}) -> list:
        '''
        Get member by ids, as Member objects.
        If the list is empty, will get all members.
        '''
        d = self._api_get(id=id, url=self.URL_GA+'chara/',
                          party=self.party, filters=filters)

        return [DMember(data) for data in d]

    def get_current_event(self) -> DEvent:
        '''
        Returns the current ongoing event, as provided by bandori database.
        '''
        event = self._retrieve_response(self.URL_GA+'event/')

        return DEvent(data=event, region=self.region)

    def get_bands(self, filters: dict = {}) -> list:
        '''
        Get all bands as a list of Band objects.
        This cannot search by id.
        '''
        d = self._api_get(id=[], url=self.URL_GA+'band/', party=False,
                          filters=filters)

        return [DBand(data, region=self.region) for data in d]

    def get_songs(self, id: list = [], filters: dict = {}) -> list:
        '''
        Get song by ids, as Song objects.

        If the list is empty all songs will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_GA+'music/', party=False,
                          filters=filters)

        return [DSong(data, region=self.region) for data in d]

    def get_gachas(self, id: list = [], filters: dict = {}) -> list:
        '''
        Get gacha by ids, as Gacha objects.

        If the list is empty all gacha will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_GA+'gacha/', party=False,
                          filters=filters)

        return [DGacha(data, region=self.region) for data in d]

    def get_active_gachas(self) -> list:
        '''
        Get active gachas as Gacha objects.
        '''
        d = self._api_get(url=self.URL_GA+'gacha/current', party=False)

        return [DGacha(data, region=self.region) for data in d]

    def get_rankings(self, id: list = [], filters: dict = {}) -> list:
        '''
        Get Degrees by ids, as Degree objects.

        If the list is empty all Degrees will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_GA+'degree/', party=False,
                          filters=filters)

        return [DDegree(data, region=self.region) for data in d]

    def get_comics(self, id: list = [], filters: dict = {}) -> list:
        '''
        Get the loading screen komas from the bandori database api
        '''
        d = self._api_get(id=id, url=self.URL_GA+'sfc/', party=False,
                          filters=filters)

        return [DComic(data, region=self.region) for data in d]

    def get_stamps(self, id: list = [], filters: dict = {}) -> list:
        '''
        Get the stamps from the bandori database api
        '''
        d = self._api_get(id=id, url=self.URL_GA+'sfc/', party=False,
                          filters=filters)

        return [DStamp(data, region=self.region) for data in d]
