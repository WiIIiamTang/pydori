from .base_objects import *
from .bandori_loader import BandoriLoader


class BandoriApi(BandoriLoader):
    '''
    Represents a class that interacts with the bandori.party
    and bandori.ga APIs
    '''
  
    
    def __init__(self, region = 'en/'):
        super().__init__(region)


    def get_cards(self, id : list = []):
        '''
        Get card by ids, as Card objects.
        If the list is empty, will get all cards.
        '''
        d = self._api_get(id=id, url=self.URL_PARTY+'cards/')
        
        return [Card(data) for data in d]

    def get_members(self, id : list = []):
        '''
        Get member by ids, as Member objects.
        If the list is empty, will get all members.
        '''
        d = self._api_get(id=id, url=self.URL_PARTY+'members/')
        
        return [Member(data) for data in d]

    def get_events(self, id : list = []):
        '''
        Get events by ids, as Event objects.
        If the list is empty, will get all events.
        '''

                # How to get by id? bandori.party doesn't provide event_id
                # (but it's still possible to search by id).

        d = self._api_get(id=[], url=self.URL_PARTY+'events/')

        return [Event(event) for event in d]

    def get_current_event(self):
        '''
        Returns the current ongoing event as a dict, as provided by bandori database.

        ### This event data has a different format than from bandori.party, so
        ### the dictionary will have different contents.
        '''
        return self._retrieve_response(self.URL_GA+'event/')
    
    def get_costumes(self, id : list = []):
        '''
        Get costume by ids, as Costume objects.
        If the list is empty all costumes will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_PARTY+'costumes/')

        return [Costume(data) for data in d]
    
    def get_items(self, id : list = []):
        '''
        Get item by ids, as Item objects.
        If the list is empty all items will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_PARTY+'items/')

        return [Item(data) for data in d]
    
    def get_areaitems(self, id : list = []):
        '''
        Get areaitem by ids, as AreaItem objects.
        If the list is empty all items will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_PARTY+'areaitems/')

        return [AreaItem(data) for data in d]
    
    def get_assets(self, id : list = []):
        '''
        Get asset by ids.
        If the list is empty all items will be returned.
        
        The return value is a dict with keys to the categories of assets,
        and for values a list of Asset objects.
        '''
        d = self._api_get(id=id, url=self.URL_PARTY+'assets/')

        sorted = {"comic" : [], "background" : [], "stamp": [], "title" : [], "interface" : [], "officialart" : []}
        for data in d:
            type = data["i_type"]
            if type == 'comic':
                sorted["comic"].append(Comic(data))
            elif type == 'background':
                sorted["background"].append(Background(data))
            elif type == 'stamp':
                sorted["stamp"].append(Stamp(data))
            elif type == 'title':
                sorted["title"].append(Title(data))
            elif type == 'interface':
                sorted["interface"].append(Interface(data))
            else:
                sorted["officialart"].append(OfficialArt(data))
            
        return sorted
    

    def get_bands(self):
        '''
        Get all bands as a list of Band objects.
        '''
        d = self._api_get(id=[], url=self.URL_GA+'band/', party=False)

        return [Band(data) for data in d]


    def get_songs(self, id : list = []):
        '''
        Get song by ids, as Song objects.

        If the list is empty all songs will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_GA+'music/', party=False)

        return [Song(data) for data in d]
    
    def get_gachas(self, id : list = []):
        '''
        Get gacha by ids, as Gacha objects.

        If the list is empty all gacha will be returned.
        '''
        d = self._api_get(id=id, url=self.URL_GA+'gacha/', party=False)

        return [Gacha(data) for data in d]
