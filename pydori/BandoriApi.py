from .p_api import PBandoriApi
from .d_api import DBandoriApi


def bandori_api(region: str = 'en/', party: bool = True):

    if party:
        return PBandoriApi(region=region, party=party)
    else:
        return DBandoriApi(region=region)
