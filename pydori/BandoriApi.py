from .p_api import PBandoriApi
from .d_api import DBandoriApi
import json


def bandori_api(region: str = None, party: bool = None):
    try:
        with open('default_config.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        reset_defaults()
        with open('default_config.json', 'r') as f:
            config = json.load(f)

    if region is None:
        region = config.get('region')
    if party is None:
        party = config.get('party')

    if party:
        return PBandoriApi(region=region, party=party)
    else:
        return DBandoriApi(region=region)


def set_defaults(settings: dict = {}) -> bool:
    with open('default_config.json', 'r') as f:
        config = json.load(f)

    try:
        for key, value in settings:
            config[key] = value

        return True

    except Exception:
        return False


def reset_defaults() -> bool:
    try:
        config = {}
        config['party'] = True
        config['region'] = 'en/'

        with open('default_config.json', 'w') as f:
            json.dump(config, f)

        return True

    except Exception:
        return False
