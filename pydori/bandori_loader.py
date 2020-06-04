import requests

class BandoriLoader:
    '''
    Represents a class that makes api calls to bandori.party
    and bandori database
    '''
    def __init__(self, region = 'en/'):
        self.region = region
        self.URL_PARTY = "https://bandori.party/api/"
        self.URL_GA = "https://api.bandori.ga/v1/" + region # english server default
        self.URL_GA_RES = "https://res.bandori.ga"
    
    class FailedRequest(Exception):
        pass


    def _retrieve_response(self, url) -> dict:
        '''
        Gets a response from the url and returns the result
        as a dict.
        '''
        res = requests.get(url)
        if res.status_code != 200:
            raise BandoriLoader.FailedRequest(f'Could not get request from {url}')
        
        return res.json()

    def _retrieve_responses(self, url, filters={}) -> list:
        '''
        ### FOR BANDORI.PARTY API CALLS

        Gets responses from provided url and returns the 
        result as a list of dictionaries. 
        
        This is intended to get all pages.
        '''
        res = []
        page = url
        #print(filters)

        while(True):
            response = requests.get(page)
            if response.status_code != 200:
                raise BandoriLoader.FailedRequest(f'Could not get request from {page}. Stopping operation.')
            data = response.json()

            if data["next"] is None:
                for d in data["results"]:
                    if self._check_filters(filters=filters, obj=d):
                        res.append(d)
                break
            else:
                for d in data["results"]:
                    if self._check_filters(filters=filters, obj=d):
                        res.append(d)
                page = data["next"]
        
        return res
    
    def _check_filters(self, filters={}, obj : dict=None):
        '''
        Checks if the object (a dict) has the correct key-pair values
        corresponding to the filters.
        '''
        if not filters:
            return True
        
        for key, value in filters.items():
            if obj[key] != value:
                return False
        return True
    
    def _api_get(self, id : list = [], url='', party=True, filters={}):
        '''
        Handles getting responses from the APIs.
        The result may be returned as a list (of dicts) or a dict.
        '''
        if party:
            if not id:
                return self._retrieve_responses(url=url, filters=filters)
            
            else:
                res = []
                for i in id:
                    res.append(self._retrieve_response(url + str(i)))

                return res
        
        else:
            if not id:
                return self._retrieve_response(url)
            else:
                res = []
                for i in id:
                    res.append(self._retrieve_response(url + str(i)))
                
                return res
    

    def _full_event_loader(self, url, filters={}) -> list:
        '''
        A function that returns a list of dicts.

        Each dict is an event.

        It grabs all events from bandori.party api,
        and adds the appropriate id to the event.
        '''
        events = []
        id = 1 # assuming the smallest event id is 1.

        # getting the total count of events.
        data = self._retrieve_response(url)
        total_count = data["count"]

        # adding all events to the list.
        while len(events) < total_count:
            try:
                data = self._retrieve_response(url + str(id))
                if self._check_filters(filters=filters, obj=data):
                    if 'detail' in data.keys():
                        pass
                    else:
                        data['id'] = id
                        events.append(data)
                    id += 1
                    #print(id, end='\r')
            except BandoriLoader.FailedRequest as e:
                # a failed request is expected since some event ids are not used.
                id += 1
                continue

        return events