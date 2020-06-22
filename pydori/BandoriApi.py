from .models.gamodels import (
    DCard,
    DSong,
    DGacha,
    DBand,
    DMember,
    DDegree,
    DComic,
    DStamp
)
from .models.ptymodels import (
    PCard,
    PMember,
    PEvent,
    PCostume,
    PItem,
    PAreaItem,
    PComic,
    PBackground,
    PStamp,
    PTitle,
    PInterface,
    POfficialArt
    )
from .loader import BandoriLoader


class BandoriApi(BandoriLoader):
    '''
    Represents a class that interacts with the bandori.party
    and bandori.ga APIs
    '''

    def __init__(self, region='en/', party=True):
        super().__init__(region)
        self.party = party

###############################################################################
    def get_cards(self, id: list = [], filters={}) -> list:
        '''
        Get card by ids, as Card objects.
        If the list is empty, will get all cards.
        '''
        if self.party:
            d = self._api_get(id=id, url=self.URL_PARTY+'cards/',
                              filters=filters)

            return [PCard(data) for data in d]
        else:
            d = self._api_get(id=id, url=self.URL_GA+'card/',
                              party=self.party, filters=filters)

            return [DCard(data, region=self.region) for data in d]

    def get_members(self, id: list = [], filters={}) -> list:
        '''
        Get member by ids, as Member objects.
        If the list is empty, will get all members.
        '''
        if self.party:
            d = self._api_get(id=id, url=self.URL_PARTY+'members/',
                              filters=filters)

            return [PMember(data) for data in d]
        else:
            d = self._api_get(id=id, url=self.URL_GA+'chara/',
                              party=self.party, filters=filters)

            return [DMember(data) for data in d]

    def get_events(self, id: list = [], filters={}) -> list:
        '''
        Get events by ids, as Event objects.
        If the list is empty, will get all events.
        '''
        if not id:
            if not filters:
                events = self._full_event_loader(url=self.URL_PARTY+'events/',
                                                 filters=filters)
            else:
                events = self._full_event_loader(url=self.URL_PARTY+'events/',
                                                 filters={})
                events = [e for e in events if self._check_filters(
                          filters=filters, obj=e)]
        else:
            events = self._api_get(id=id, url=self.URL_PARTY+'events/',
                                   filters=filters)
            for i, event in enumerate(events):
                event['id'] = id[i]

        return [PEvent(event) for event in events]

    def get_current_event(self) -> dict:
        '''
        Returns the current ongoing event, as provided by bandori database.
        '''
        event = self._retrieve_response(self.URL_GA+'event/')
        id = event["eventId"] + 3  # offset of 3 to get the correct event

        return self.get_events(id=[id])[0]

    def get_costumes(self, id: list = [], filters={}) -> list:
        '''
        Get costume by ids, as Costume objects.
        If the list is empty all costumes will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_PARTY+'costumes/',
                          filters=filters)

        return [PCostume(data) for data in d]

    def get_items(self, id: list = [], filters={}):
        '''
        Get item by ids, as Item objects.
        If the list is empty all items will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_PARTY+'items/', filters=filters)

        return [PItem(data) for data in d]

    def get_areaitems(self, id: list = [], filters={}):
        '''
        Get areaitem by ids, as AreaItem objects.
        If the list is empty all items will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_PARTY+'areaitems/',
                          filters=filters)

        return [PAreaItem(data) for data in d]

    def get_assets(self, id: list = [], filters={}):
        '''
        Get bandori party asset by ids.
        If the list is empty all items will be returned.
        The return value is a dict with keys to the categories of assets,
        and for values a list of Asset objects.

        Assets are specific to Bandori Party, so there is no option
        to get Bandori Database objects here. Instead, they are
        defined in another function.
        '''
        d = self._api_get(id=id, url=self.URL_PARTY+'assets/', filters=filters)

        sorted = {"comic": [], "background": [], "stamp": [], "title": [],
                  "interface": [], "officialart": []}
        for data in d:
            type = data["i_type"]
            if type == 'comic':
                sorted["comic"].append(PComic(data))
            elif type == 'background':
                sorted["background"].append(PBackground(data))
            elif type == 'stamp':
                sorted["stamp"].append(PStamp(data))
            elif type == 'title':
                sorted["title"].append(PTitle(data))
            elif type == 'interface':
                sorted["interface"].append(PInterface(data))
            else:
                sorted["officialart"].append(POfficialArt(data))

        return sorted

###############################################################################
# Functions that only work on Bandori database

    def get_bands(self, filters={}):
        '''
        Get all bands as a list of Band objects.
        This cannot search by id.
        '''
        d = self._api_get(id=[], url=self.URL_GA+'band/', party=False,
                          filters=filters)

        return [DBand(data, region=self.region) for data in d]

    def get_songs(self, id: list = [], filters={}):
        '''
        Get song by ids, as Song objects.

        If the list is empty all songs will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_GA+'music/', party=False,
                          filters=filters)

        return [DSong(data, region=self.region) for data in d]

    def get_gachas(self, id: list = [], filters={}):
        '''
        Get gacha by ids, as Gacha objects.

        If the list is empty all gacha will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_GA+'gacha/', party=False,
                          filters=filters)

        return [DGacha(data, region=self.region) for data in d]

    def get_rankings(self, id: list = [], filters={}):
        '''
        Get Degrees by ids, as Degree objects.

        If the list is empty all Degrees will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_GA+'degree/', party=False,
                          filters=filters)

        return [DDegree(data, region=self.region) for data in d]

    def get_ga_comics(self, id: list = [], filters={}):
        '''
        Get the loading screen komas from the bandori database api
        '''
        d = self._api_get(id=id, url=self.URL_GA+'sfc/', party=False,
                          filters=filters)

        return [DComic(data, region=self.region) for data in d]
    
    def get_ga_stamps(self, id: list = [], filters={}):
        '''
        Get the stamps from the bandori database api
        '''
        d = self._api_get(id=id, url=self.URL_GA+'sfc/', party=False,
                          filters=filters)

        return [DStamp(data, region=self.region) for data in d]

###############################################################################

    def get_all(self):
        '''
        Get all possible objects from the apis as a dictionary.
        '''
        d = {'cards': [], 'members': [], 'events': [], 'costumes': [],
             'items': [], 'areaitems': [], 'assets': {}, 'bands': [],
             'songs': [], 'gachas': []}

        d['cards'].extend(self.get_cards())
        d['members'].extend(self.get_members())
        d['events'].extend(self.get_events())
        d['costumes'].extend(self.get_costumes())
        d['items'].extend(self.get_items())
        d['areaitems'].extend(self.get_areaitems())
        d['assets'].update(self.get_assets())
        d['bands'].extend(self.get_bands())
        d['songs'].extend(self.get_songs())
        d['gachas'].extend(self.get_gachas())

        return d
