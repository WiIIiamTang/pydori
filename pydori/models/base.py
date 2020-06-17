from ..loader import BandoriLoader

###############################################################################
# Base model

class BandoriObject:
    '''
    Represents information retrieved from the api
    as an object
    '''
    
    def __init__(self, data : dict, id_name = 'id', region = 'en/'):
        self.URL_PARTY = "https://bandori.party/api/" # for party objects

        self.URL_GA = "https://api.bandori.ga/v1/" + region # for b database objects
        self.URL_GA_RES = "https://res.bandori.ga"

        self.id = data.get(id_name) # general attributes for all
        self.data = data
        self.bl = BandoriLoader()
    
    def __lt__(self, other):
        return self.id < other.id
    
    def __str__(self):
        return str(self.data)
###############################################################################