import pytest
from pydori import BandoriApi as ba


@pytest.fixture
def api_en():
    return ba()


@pytest.fixture
def api_jp():
    return ba('jp/')

###############################################################################
# Testing BandoriApi functions


@pytest.mark.parametrize('id, filters, expected', [
    ([866, 1050, 511], {}, ('Call for Courage', 'Cool')),
    ([], {'i_attribute': 'Cool', 'i_rarity': 4},
     ('Number 4, Pitcher', 'Cool')),
    ([511, 511, 1470], {}, ('Delicious Times', 'Cool'))
])
def test_cards(api_en, id, filters, expected):
    cards = api_en.get_cards(id=id, filters=filters)
    result = cards[2]

    assert result.name, result.attribute == expected


@pytest.mark.parametrize('id, filters, expected', [
    ([6, 7, 8], {}, 'Rimi Ushigome'),
    ([], {'i_band': 'Poppin\'Party'}, 'Rimi Ushigome'),
])
def test_members(api_en, id, filters, expected):
    members = api_en.get_members(id=id, filters=filters)
    result = members[2]

    assert result.name == expected


@pytest.mark.parametrize('id, filters, expected', [
    ([82, 98], {}, 'vs_live'),
    ([], {'i_type': 'vs_live'}, 'vs_live'),
])
def test_events(api_en, id, filters, expected):
    events = api_en.get_events(id=id, filters=filters)
    result = events[1]

    assert result.type == expected


@pytest.mark.parametrize('id, filters, expected', [
    ([1463], {}, 1460),
    ([], {'member': 29}, 1460)
])
def test_costumes(api_en, id, filters, expected):
    costumes = api_en.get_costumes(id=id, filters=filters)
    result = costumes[0]

    assert result.card == expected


@pytest.mark.parametrize('id, filters, expected', [
    ([2], {}, 'Live Boosts'),
    ([], {'i_type': 'ticket'}, 'Studio Ticket (Single)'),
    ([], {}, 'Stars')
])
def test_items(api_en, id, filters, expected):
    items = api_en.get_items(id=id, filters=filters)
    result = items[0]

    assert result.name == expected


@pytest.mark.parametrize('id, filters, expected', [
    ([10, 9, 8, 6], {}, 'Kaoru\'s Guitar'),
    ([], {'i_band': 'Afterglow'}, 'Rock Mic'),
    ([], {}, 'Studio Mic')
])
def test_areaitems(api_en, id, filters, expected):
    areaitems = api_en.get_areaitems(id=id, filters=filters)
    result = areaitems[0]

    assert result.name == expected


@pytest.mark.parametrize('id, filters, expected', [
    ([899], {}, ''),
    ([], {'i_type': 'stamp'}, 'stamp'),
])
def test_assets(api_en, id, filters, expected):
    assets = api_en.get_assets(id=id, filters=filters)
    result = assets.get('stamp')[0] if assets.get('stamp') else ''

    if not result:
        assert result == expected
    else:
        assert result.type == expected


@pytest.mark.parametrize('filters, expected', [
    ({}, 'Afterglow')
])
def test_bands(api_en, filters, expected):
    bands = api_en.get_bands(filters=filters)
    result = bands[1]

    assert result.name == expected


@pytest.mark.parametrize('id, filters, expected', [
    ([89, 97], {}, 'Opera of the wasteland'),
    ([], {'bandName': 'Roselia'}, 'FIRE BIRD'),
])
def test_songs(api_en, id, filters, expected):
    songs = api_en.get_songs(id=id, filters=filters)
    result = songs[1]

    assert result.title == expected


@pytest.mark.parametrize('id, filters, expected', [
    ([120], {}, 'Head Start Gacha'),
    ([], {}, 'ガルパーティ！in東京開催記念ガチャ')
])
def test_gachas(api_en, id, filters, expected):
    gachas = api_en.get_gachas(id=id, filters=filters)
    result = gachas[0]

    assert result.name == expected
