from ..loader import BandoriLoader


class BandoriObject(BandoriLoader):
    '''
    Represents information retrieved from the api
    '''
    def __init__(self, data: dict, id_name='id', region='en/'):
        super().__init__(region)

        self.id = data.get(id_name)
        self.data = data

    def __lt__(self, other):
        return self.id < other.id

    def __str__(self):
        return str(self.data)

    def __iter__(self):
        return iter(self.data)
