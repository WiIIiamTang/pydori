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


class PBandoriApi(BandoriLoader):
    '''
    Represents a class that interacts with the bandori party API
    '''

    def __init__(self, region='en/', party=True):
        super().__init__(region)
        self.party = party

    def get_cards(self, id: list = [], filters: dict = {}) -> list:
        '''
        Get card by ids, as Card objects.
        If the list is empty, will get all cards.
        '''
        d = self._api_get(id=id, url=self.URL_PARTY+'cards/',
                          filters=filters)

        return [PCard(data) for data in d]

    def get_members(self, id: list = [], filters: dict = {}) -> list:
        '''
        Get member by ids, as Member objects.
        If the list is empty, will get all members.
        '''
        d = self._api_get(id=id, url=self.URL_PARTY+'members/',
                          filters=filters)

        return [PMember(data) for data in d]

    def get_events(self, id: list = [], filters: dict = {}) -> list:
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

    def get_costumes(self, id: list = [], filters: dict = {}) -> list:
        '''
        Get costume by ids, as Costume objects.
        If the list is empty all costumes will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_PARTY+'costumes/',
                          filters=filters)

        return [PCostume(data) for data in d]

    def get_items(self, id: list = [], filters: dict = {}) -> list:
        '''
        Get item by ids, as Item objects.
        If the list is empty all items will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_PARTY+'items/', filters=filters)

        return [PItem(data) for data in d]

    def get_areaitems(self, id: list = [], filters: dict = {}) -> list:
        '''
        Get areaitem by ids, as AreaItem objects.
        If the list is empty all items will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_PARTY+'areaitems/',
                          filters=filters)

        return [PAreaItem(data) for data in d]

    def get_assets(self, id: list = [], filters={}) -> dict:
        '''
        Get bandori party asset by ids.
        If the list is empty all items will be returned.
        The return value is a dict with keys to the categories of assets,
        and for values a list of Asset objects.
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
