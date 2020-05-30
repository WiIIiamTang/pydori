
# Pydori

  

[![PyPI version fury.io](https://badge.fury.io/py/pydori.svg)](https://pypi.python.org/pypi/pydori/)

  

A python wrapper for the bandori.party and bandori.ga public APIs.

  

# Info
Although both bandori.party and bandori database provide extensive public bang dream api's, there is currently not much documentation to help navigate through them. This package attempts to simplify accessing the various endpoints they provide. Not everything is available through this package, but the main ones should be here. This package consolidates both the bandori.party and bandori.ga APIs - for example, songs are not available through the bandori.party API, so all music-related data is gotten from bandori database.
  

# Installation

Use pip to install:

``` pip install pydori ```

  

# Example
This example instantiates a BandoriApi object, gets a card by ID, and displays the card's name.
```python
import pydori

b = pydori.BandoriApi()
result = b.get_cards(id=[511])
card = result[0]

print(card.name)
```

Here we get the current event and display the start and end times:
```python
from pydori import BandoriApi as api

b = api()
current = b.get_current_event()[0]

print(current.get_start_date())
print(current.get_end_date())
```

# Documentation

## BandoriApi
 ```pydori.BandoriApi(region = 'en/')```
 
A class that talks to the bandori APIs. All functions that should be used are in this class. It holds the following attributes:

- **URL_PARTY** - A url to the bandori.party api

- **URL_GA** - a url to the bandori.ga api

- **URL_GA_RES** - a url to the bandori database resource api

### Parameters
- region(Optional[str]) - Region used for the bandori database api. Other options include 'jp/', 'tw/' (not tested), 'kr/' (not tested)

### Functions
#### ```get_cards(id : list = [])```
Returns a list of ```Card``` objects based on the ids provided. If the list is empty, all cards will be returned.

#### ```get_members(id : list = [])```
Returns a list of ```Member``` objects based on the ids provided. If the list is empty, all members will be returned.

#### ```get_events(id : list = [])```
Returns a list of ```Event``` objects based on the ids provided. If the list is empty, all members will be returned.

#### ```get_current_event()```
Returns the current event as an ```Event``` object in a list (it makes an internal call to ```get_events```). The current event is provided by the bandori database api, but the event data itself is from bandori.party.

#### ```get_costumes(id : list = [])```
Returns a list of ```Costume``` objects based on the ids provided. If the list is empty, all costumes will be returned.

#### ```get_items(id : list = [])```
Returns a list of ```Item``` objects based on the ids provided. If the list is empty, all items will be returned.

#### ```get_areaitems(id : list = [])```
Returns a list of ```AreaItem``` objects based on the ids provided. If the list is empty, all areaitems will be returned.

#### ```get_assets(id : list = [])```
Returns a dict where the keys are the different subtypes of ```Asset```, and the values are a list of those objects. If the input list is empty, all assets will be returned.

Even when there is only one asset queried, a full dict will be returned - just with empty lists in some of the values.


#### ```get_bands()```
Returns a list of all bands as ```Band``` objects. You cannot get a specific band from id. This is region sensitive.

#### ```get_songs(id : list = [])```
Returns a list of ```Song``` objects based on the ids provided. If the list is empty, all songs will be returned. This is region sensitive.

#### ```get_gachas(id : list = [])```
Returns a list of ```Gacha```objects based on the ids provided. If the list is empty, all gachas will be returned. This is region sensitive.


## BandoriObject
```pydori.base_objects.BandoriObject(data : dict, id_name = 'id', region = 'en/')```

Bandori objects are classes that represent data retrieved from the api. They are used to have quick access to certain attributes, and provide helpful methods on the data. They can be sorted by id. **They should not be normally instantiated (unless for debugging) and are meant as outputs from BandoriApi.** All BandoriObjects have the follow attributes:

- **URL_PARTY** - A url to the bandori.party api

- **URL_GA** - a url to the bandori.ga api

- **URL_GA_RES** - a url to the bandori database resource api


- **id** - The object's id

- **data** - The original dict of the object's information from the api.


_Notes:_

*Region select only works on certain methods - Song, Gacha, Band. See below*

*Not all attributes available from the api are recorded when creating these objects. It's best to work with the **data** dict as it contains everything.*

*Some attributes may have a null value and not work with their intended functions. Check before using.*

*The bandori.party api is used for most classes. The Songs, Bands, and Gachas class make use of the bandori database api.*

### Parameters
- data([dict]) - A python dictionary containing the data for the class

- id_name(Optional[str]) - The string to use when searching for the id in the dict.

- region(Optional[str]) - Region used for the bandori database api. Other options include 'jp/', 'tw/' (not tested), 'kr/' (not tested)


The following classes inherit from BandoriObject:

___
### ```Card(BandoriObject)```
Represents a Bang Dream card with the following attributes:

- **member** - member id

- **rarity** - card rarity

- **attribute** - card attribute

- **id** - The object's id

- **name** - english name

- **japanese_name**

- **skill_type**

- **cameo** - a list of cameo member ids

#### Functions
#### ```get_card_member()```
Returns a ```Member``` corresponding to the Card's **member** attribute.
#### ```get_cameo_members()```
Returns a list of ```Member``` corresponding to the Card's **cameo** attribute.
___
### ```Member(BandoriObject)```
Represents a Bang Dream member with the following attributes:

- **name**

- **japanese_name**

- **band** - the band name that the member belongs to

- **school**

- **year**

- **romaji_cv**

- **cv**

- **birthday**

- **food_likes**

- **food_dislikes**

- **astro** - astrological sign

- **instrument**

- **description**

___
### ```Event(BandoriObject)```
Represents a bang dream event with the following attributes:

- **name**

- **japanese_name**

- **type**

- **[english | jp | tw | kr]_[start | end]_date** - start and end dates for the events, for different servers.

- **versions_available** - versions of the game where the event is available

- **main_card** - main card id

- **secondary_card** - secondary card id

- **boost_attribute**

- **boost_members** - a list of member ids who are boosted during event

#### Functions
#### ```get_start_date(region = 'en')```
Returns a datetime object of the start date of the event, depending on region (default en). If the date attribute is null, returns -1.
#### ```get_end_date(region = 'en')```
See ```get_start_date```.
#### ```get_main_card()```
Returns a ```Card``` object corresponding to the Event's **main_card** id
#### ```get_secondary_card()```
Returns a ```Card``` object corresponding to the Event's **secondary_card** id
#### ```get_boost_members()```
Returns a list of ```Member``` corresponding to the Event's **boost_members** ids
___
### ```Costume(BandoriObject)```
Represents an in-game costume with the following attributes:

- **type**

- **card** - card id if applicable

- **member** - member id

- **name**

#### Functions
#### ```get_costume_member()```
Returns a ```Member``` object corresponding to the Costume's **member** attribute
#### ```get_costume_card()```
Returns a ```Card``` object corresponding to the Costume's **card** attribute

---
### ```Item(BandoriObject)```
Represents an in-game item with the following attributes:

- **name**

- **type**

- **description**


---
### ```AreaItem(BandoriObject)```
Represents an in-game area item with the following attributes:

- **name**

- **area** - id for the area. Currently unusable.

- **type**

- **instrument**


- **attribute**

- **stat**

- **max_level**

- **values** - list of percentages that the item boosts at each level.

- **description**

___
### ```Asset(BandoriObject)```
Represents a Bang Dream asset as defined by bandori.party. Every asset has a **type**. There are multiple types of ```Asset``` from this:
### ```Comic(Asset)```
A bandori comic.

- **name**

- **members** - a list of member ids (that appear in the comic)

#### Functions
#### ```get_comic_members()```
Returns a list of ```Member``` object corresponding to the Comic's **members** attribute

### ```Background(Asset)```
A bandori background.

- **name**

### ```Stamp(Asset)```
A bandori stamp.

- **name**

- **members** - a list of member ids that appear in the stamp.

#### Functions
#### ```get_stamp_members()```
Returns a list of ```Member``` object corresponding to the Comic's **members** attribute

### ```Title(Asset)```
A bandori profile title.

- **event** - the event id this title is from.

- **value** - TOP {value} of the event.

#### Functions
#### ```title_event()```
Returns an ```Event``` object corresponding to the Title's **event** attribute.

### ```Interface(Asset)```
A bandori interface (mostly pictures).

- **name**

### ```OfficialArt(Asset)```
Bandori official art.

___
### ```Band(BandoriObject)```
This takes in a dict from the bandori database api (so it is by region). Represents a Bang Dream band with the following attributes:

- **name**

- **introduction**

- **members** - The bandori.party member ids for the members in this band. Note that any bands past Roselia have wrong ids for some reason.

#### Functions
#### ```get_band_members()```
Returns a list of ```Member``` object corresponding to the Band's **members** attribute

___
### ```Song(BandoriObject)```
This takes in a dict from the bandori database api (so it is by region). Represents a Bang Dream in-game song with the following attributes:

- **title**

- **bgm** - link to song mp3.

- **thumb**

- **jacket**

- **band_name**

- **band** - the band id.

- **difficulty** 

- **how_to_get**

- **composer**

- **lyricist**

---
### ```Gacha(BandoriObject)```
This takes in a dict from the bandori database api(so it is by region). Represents a Bang Dream gacha with the following attributes:

- **name**

- **[start | end]_date** - a *timestamp* in milliseconds for the start/end dates of the event.

- **description**

- **period**

- **type**

#### Functions
#### ```get_start_date()```
Returns a datetime object for the start date of the Gacha.
#### ```get_end_date()```
See ```get_start_date()```


## BandoriLoader
```pydori.bandori_loader.BandoriLoader(region = 'en/')```

BandoriApi inherits from this class. It is only meant for internal use, and its purpose is to make api calls to bandori.party and bandori.database and return the result as dictionaries or lists. It should not be normally instantiated, but is useful sometimes for debugging.


# Credits

  

[![PyPI license](https://img.shields.io/pypi/l/pydori.svg)](https://pypi.python.org/pypi/pydori/)

  

This project is licensed under the MIT license.

  

API provided by [bandori.party](https://bandori.party/) and [bandori database](https://bangdream.ga/).

  

I do not own any logos, images, or assets of the BanG Dream! Franchise, they are the property and trademark of Bushiroad.
