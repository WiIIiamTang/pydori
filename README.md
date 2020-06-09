
# Pydori

  

[![PyPI version fury.io](https://badge.fury.io/py/pydori.svg)](https://pypi.python.org/pypi/pydori/)
[![Build Status](https://travis-ci.org/WiIIiamTang/pydori.svg?branch=master)](https://travis-ci.org/WiIIiamTang/pydori)
  

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
current = b.get_current_event()

print(current.get_start_date())
print(current.get_end_date())
```

Pydori accepts filters for the objects, as a dictionary. If a list of ids are present, then the filters will be ignored completely. This example shows how to get all songs by the band "Roselia".

```python
import pydori

b = pydori.BandoriApi()
roselia_songs = b.get_songs(id=[], filters={'bandName' : 'Roselia'})
```

# Documentation

## BandoriApi
 ```pydori.BandoriApi(BandoriLoader)```
 
A class that talks to the bandori APIs. All functions that should be used are in this class.

| Attributes | Description                                |
|------------|--------------------------------------------|
| URL_PARTY  | A url to the bandori.party api             |
| URL_GA     | a url to the bandori.ga api                |
| URL_GA_RES | a url to the bandori database resource api |
| region     |                                            |

### Parameters
- region(Optional[str]) - Region used for the bandori database api. Other options include 'jp/', 'tw/' (not tested), 'kr/' (not tested)

### Functions
#### ```get_cards(id : list = [], filters : dict = {})```
Returns a list of ```Card``` objects based on the ids provided. If the list is empty, all cards will be returned.

#### ```get_members(id : list = [], filters : dict = {})```
Returns a list of ```Member``` objects based on the ids provided. If the list is empty, all members will be returned.

#### ```get_events(id : list = [], filters : dict = {})```
Returns a list of ```Event``` objects based on the ids provided. If the list is empty, all members will be returned.

#### ```get_current_event()```
Returns the current event as an ```Event``` object in a list (it makes an internal call to ```get_events```). The current event is provided by the bandori database api, but the event data itself is from bandori.party.

#### ```get_costumes(id : list = [], filters : dict = {})```
Returns a list of ```Costume``` objects based on the ids provided. If the list is empty, all costumes will be returned.

#### ```get_items(id : list = [], filters : dict = {})```
Returns a list of ```Item``` objects based on the ids provided. If the list is empty, all items will be returned.

#### ```get_areaitems(id : list = [], filters : dict = {})```
Returns a list of ```AreaItem``` objects based on the ids provided. If the list is empty, all areaitems will be returned.

#### ```get_assets(id : list = [], filters : dict = {})```
Returns a dict where the keys are the different subtypes of ```Asset```, and the values are a list of those objects. If the input list is empty, all assets will be returned.

Even when there is only one asset queried, a full dict will be returned - just with empty lists in some of the values.


#### ```get_bands(filters : dict = {})```
Returns a list of all bands as ```Band``` objects. You cannot get a specific band from id. This is region sensitive.

#### ```get_songs(id : list = [], filters : dict = {})```
Returns a list of ```Song``` objects based on the ids provided. If the list is empty, all songs will be returned. This is region sensitive.

#### ```get_gachas(id : list = [], filters : dict = {})```
Returns a list of ```Gacha```objects based on the ids provided. If the list is empty, all gachas will be returned. This is region sensitive.

#### ```get_all()```
Returns all possible objects from the api as a dictionary. It is separated by object type.


### Using filters
A function can accept an optional "filters" parameter. If the list with ids is not empty, filters will be ignored. You are able to filter by the objects' attributes. The keys should be the attribute you want to filter, the values are what you want. For example,
```python
c = api.get_cards(filters={'i_attribute' : 'Cool'})
```
will get all cards with the attribute *Cool*. For a list of all attributes you can filter by, see the **BandoriObject** section below.
The keys of the dict can be any attribute of the objects (as a string), and the return value will be a list of objects with the desired attributes, provided that the value in the dict is valid. Filters are case sensitive (you need to put the exact, correct value).

**The filter attributes may have different format. For example, you can access a Card's rarity by doing : ```Card.rarity```
but in order to filter by rarity, I would have to do something like : ```get_cards(filters={'i_rarity' : 4}```
In other words, the _keys for filters_ are not always exactly the same as the attribute name. When _it is different_, the correct filter keyword will be indicated.**


## BandoriObject
```pydori.base_objects.BandoriObject(data : dict, id_name = 'id', region = 'en/')```

Bandori objects are classes that represent data retrieved from the api. They are used to have quick access to certain attributes, and provide helpful methods on the data. They can be sorted by id. **They should not be normally instantiated (unless for debugging) and are meant as outputs from BandoriApi.** All BandoriObjects have the follow attributes:

| Attributes | Description                                                 |
|------------|-------------------------------------------------------------|
| URL_PARTY  | A url to the bandori.party api                              |
| URL_GA     | a url to the bandori.ga api                                 |
| URL_GA_RES | a url to the bandori database resource api                  |
| id         | The object's id                                             |
| data       | The original dict of the object's information from the api. |
| region     |                                                             |
| bl         | An instance of BandoriLoader                                |


_Notes:_

*Region select only works on certain methods, namely, Song, Gacha, Band. See below*

*Some attributes may have a null value. The objects may not work with their intended functions. Check before using.*

*The bandori.party api is used to retrieve data for most classes. Only Songs, Bands, and Gachas class make use of the bandori database api.*

### Parameters
- data([dict]) - A python dictionary containing the data for the class

- id_name(Optional[str]) - The string to use when searching for the id in the dict.

- region(Optional[str]) - Region used for the bandori database api. Other options include 'jp/', 'tw/' (not tested), 'kr/' (not tested)


The following classes inherit from BandoriObject:

___
### ```Card(BandoriObject)```
Represents a Bang Dream card with the following attributes:

| Attributes              | Description                                         | filter keyword (if different only) |
|-------------------------|-----------------------------------------------------|------------------------------------|
| member                  | The member id                                       |                                    |
| rarity                  | card rarity (num of stars) as an int                | i_rarity                           |
| attribute               | card attribute                                      | i_attribute                        |
| name                    | card's english name                                 |                                    |
| japanese_name           |                                                     |                                    |
| is_promo                | True/False                                          |                                    |
| is_original             | True/False                                          |                                    |
| image                   | url to the card image                               |                                    |
| image_trained           | url to the trained card image                       |                                    |
| art                     | url to the card art                                 |                                    |
| art_trained             | url to the trained card art                         |                                    |
| transparent             | url to the transparent image                        |                                    |
| transparent_trained     | url to the transparent trained image                |                                    |
| skill_name              |                                                     |                                    |
| japanese_skill_name     |                                                     |                                    |
| skill_type              |                                                     | i_skill_type                       |
| side_skill_type         |                                                     | i_side_skill_type                  |
| skill_template          |                                                     |                                    |
| skill_variables         |                                                     |                                    |
| side_skill_variables    |                                                     |                                    |
| full_skill              | The complete description of the skill at max level. |                                    |
| performance_min         |                                                     |                                    |
| performance_max         |                                                     |                                    |
| performance_trained_max |                                                     |                                    |
| technique_min           |                                                     |                                    |
| technique_max           |                                                     |                                    |
| technique_trained_max   |                                                     |                                    |
| visual_min              |                                                     |                                    |
| visual_max              |                                                     |                                    |
| visual_trained_max      |                                                     |                                    |
| cameo                   | A list of member ids that also appear in the card.  | cameo_members                      |

#### Functions
#### ```get_card_member()```
Returns a ```Member``` corresponding to the Card's **member** attribute.
#### ```get_cameo_members()```
Returns a list of ```Member``` corresponding to the Card's **cameo** attribute.
___
### ```Member(BandoriObject)```
Represents a Bang Dream member with the following attributes:

| Attributes    | Description                                                  | filter keyword (if different only) |
|---------------|--------------------------------------------------------------|------------------------------------|
| name          | english name                                                 |                                    |
| japanese_name |                                                              |                                    |
| band          | The band name as a string                                    | i_band                             |
| school        |                                                              |                                    |
| year          | School year (First, Second, Third)                           | i_school_year                      |
| romaji_cv     | CV name in romaji                                            | romaji_CV                          |
| cv            | CV name                                                      | CV                                 |
| birthday      | This doesn't seem realistic (maybe when they were released?) |                                    |
| food_likes    |                                                              | food_likes                         |
| food_dislikes |                                                              | food_dislikes                      |
| astro         | member's astrological sign                                   | i_astrological_sign                |
| instrument    |                                                              |                                    |
| description   | description of member                                        |                                    |


___
### ```Event(BandoriObject)```
Represents a bang dream event with the following attributes:

| Attributes                                      | Description                                                     | filter keyword (if different only)                              |
|-------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|
| name                                            | english name                                                    |                                                                 |
| japanese_name                                   |                                                                 |                                                                 |
| type                                            | event type                                                      | i_type                                                          |
| image                                           | url to event image                                              |                                                                 |
| [english \| jp \| tw \| kr]_[start \| end]_date | start and end dates for the event as a timestamp (milliseconds) | [english \| (empty) \| taiwanese \| korean]_[start \| end]_date |
| versions_available                              | versions available for event (as a list)                        | c_versions                                                      |
| main_card                                       | id of main card                                                 |                                                                 |
| secondary_card                                  |                                                                 |                                                                 |
| boost_attribute                                 | attribute boosted for this event                                | i_boost_attribute                                               |
| boost_stat                                      | stat boosted for this event                                     | i_boost_stat                                                    |
| boost_members                                   | members boosted for this event                                  |                                                                 |

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

| Attributes    | Description                          | filter keyword (if different only) |
|---------------|--------------------------------------|------------------------------------|
| name          | english name                         |                                    |
| type          | costume type                         | i_costume_type                     |
| card          | card id associated to this costume   |                                    |
| member        | member id associated to this costume |                                    |
| display_image | url to the display image             |                                    |


#### Functions
#### ```get_costume_member()```
Returns a ```Member``` object corresponding to the Costume's **member** attribute
#### ```get_costume_card()```
Returns a ```Card``` object corresponding to the Costume's **card** attribute

---
### ```Item(BandoriObject)```
Represents an in-game item with the following attributes:

| Attributes  | Description      | filter keyword (if different only) |
|-------------|------------------|------------------------------------|
| name        | english name     |                                    |
| type        | item type        | i_type                             |
| description |                  | m_description                      |
| image       | url to the image |                                    |



---
### ```AreaItem(BandoriObject)```
Represents an in-game area item with the following attributes:

| Attributes  | Description                        | filter keyword (if different only) |
|-------------|------------------------------------|------------------------------------|
| name        | english name                       |                                    |
| area        | area id                            |                                    |
| type        |                                    | i_type                             |
| image       | url to the image                   |                                    |
| instrument  |                                    | i_instrument                       |
| attribute   |                                    | i_attribute                        |
| boost_stat  | what stat this item boosts         | i_boost_stat                       |
| max_level   |                                    |                                    |
| values      | a list of how much the item boosts | value_list                         |
| description |                                    | about                              |


___
### ```Asset(BandoriObject)```


Represents a Bang Dream asset as defined by bandori.party. Every asset has a **type**.


| Attributes  | Description                        | filter keyword (if different only) |
|-------------|------------------------------------|------------------------------------|
| type        | type of asset                      | i_type                             |


There are multiple types of ```Asset``` from this:

### ```Comic(Asset)```
A bandori comic.

| Attributes      | Description                   | filter keyword (if different only) |
|-----------------|-------------------------------|------------------------------------|
| name            | english name                  |                                    |
| members         | list of member ids            |                                    |
| image           | url to image                  |                                    |
| english_image   |                               |                                    |
| taiwanese_image |                               |                                    |
| korean_image    |                               |                                    |
| band            | The name of the band          | i_band                             |
| tags            |                               | c_tags                             |
| event           | event id associated with this |                                    |
| source          |                               |                                    |
| source_link     |                               |                                    |
| song            |                               |                                    |

#### Functions
#### ```get_comic_members()```
Returns a list of ```Member``` object corresponding to the Comic's **members** attribute

### ```Background(Asset)```
A bandori background.

| Attributes      | Description                   | filter keyword (if different only) |
|-----------------|-------------------------------|------------------------------------|
| name            | english name                  |                                    |
| members         | list of member ids            |                                    |
| image           | url to image                  |                                    |
| english_image   |                               |                                    |
| taiwanese_image |                               |                                    |
| korean_image    |                               |                                    |
| band            | The name of the band          | i_band                             |
| tags            |                               | c_tags                             |
| event           | event id associated with this |                                    |
| source          |                               |                                    |
| source_link     |                               |                                    |
| song            |                               |                                    |


### ```Stamp(Asset)```
A bandori stamp.

| Attributes      | Description                   | filter keyword (if different only) |
|-----------------|-------------------------------|------------------------------------|
| name            | english name                  |                                    |
| members         | list of member ids            |                                    |
| image           | url to image                  |                                    |
| english_image   |                               |                                    |
| taiwanese_image |                               |                                    |
| korean_image    |                               |                                    |
| band            | The name of the band          | i_band                             |
| tags            |                               | c_tags                             |
| event           | event id associated with this |                                    |
| source          |                               |                                    |
| source_link     |                               |                                    |
| song            |                               |                                    |

#### Functions
#### ```get_stamp_members()```
Returns a list of ```Member``` object corresponding to the Comic's **members** attribute

### ```Title(Asset)```
A bandori profile title.

| Attributes      | Description                   | filter keyword (if different only) |
|-----------------|-------------------------------|------------------------------------|
| name            | english name                  |                                    |
| members         | list of member ids            |                                    |
| image           | url to image                  |                                    |
| english_image   |                               |                                    |
| taiwanese_image |                               |                                    |
| korean_image    |                               |                                    |
| band            | The name of the band          | i_band                             |
| tags            |                               | c_tags                             |
| event           | event id associated with this |                                    |
| source          |                               |                                    |
| source_link     |                               |                                    |
| song            |                               |                                    |
| value           | top {value} of the event      |                                    |

#### Functions
#### ```get_title_event()```
Returns an ```Event``` object corresponding to the Title's **event** attribute.

### ```Interface(Asset)```
A bandori interface (mostly pictures).

| Attributes      | Description                   | filter keyword (if different only) |
|-----------------|-------------------------------|------------------------------------|
| name            | english name                  |                                    |
| members         | list of member ids            |                                    |
| image           | url to image                  |                                    |
| english_image   |                               |                                    |
| taiwanese_image |                               |                                    |
| korean_image    |                               |                                    |
| band            | The name of the band          | i_band                             |
| tags            |                               | c_tags                             |
| event           | event id associated with this |                                    |
| source          |                               |                                    |
| source_link     |                               |                                    |
| song            |                               |                                    |

### ```OfficialArt(Asset)```
Bandori official art.

| Attributes      | Description                   | filter keyword (if different only) |
|-----------------|-------------------------------|------------------------------------|
| name            | english name                  |                                    |
| members         | list of member ids            |                                    |
| image           | url to image                  |                                    |
| english_image   |                               |                                    |
| taiwanese_image |                               |                                    |
| korean_image    |                               |                                    |
| band            | The name of the band          | i_band                             |
| tags            |                               | c_tags                             |
| event           | event id associated with this |                                    |
| source          |                               |                                    |
| source_link     |                               |                                    |
| song            |                               |                                    |


___
### ```Band(BandoriObject)```
This takes in a dict from the bandori database api (so it is by region). Represents a Bang Dream band with the following attributes:

| Attributes   | Description                      | filter keyword (if different only) |
|--------------|----------------------------------|------------------------------------|
| name         | english name                     | bandName                           |
| introduction |                                  | introductions                      |
| type         |                                  | bandType                           |
| members      | a list of member ids of the band | **should not filter**              |


*Bands past Roselia have messed up member ids*.


#### Functions
#### ```get_band_members()```
Returns a list of ```Member``` object corresponding to the Band's **members** attribute

___
### ```Song(BandoriObject)```
This takes in a dict from the bandori database api (so it is by region). Represents a Bang Dream in-game song with the following attributes:

| Attributes   | Description                   | filter keyword (if different only) |
|--------------|-------------------------------|------------------------------------|
| title        | song title                    |                                    |
| bgm          | bgm url link                  | **should not filter**              |
| thumb        | thumbnail url                 | **should not filter**              |
| jacket       | jacket url                    | **should not filter**              |
| band_name    |                               | bandName                           |
| band         | band id                       | bandId                             |
| difficulty   | a list of difficulties        |                                    |
| how_to_get   | how to get the song           | howToGet                           |
| achievements | rewards for clearing the song |                                    |
| published_at |                               | publishedAt                        |
| closed_at    |                               | closedAt                           |
| composer     |                               |                                    |
| lyricist     |                               |                                    |
| arranger     |                               |                                    |


---
### ```Gacha(BandoriObject)```
This takes in a dict from the bandori database api(so it is by region). Represents a Bang Dream gacha with the following attributes:

| Attributes   | Description             | filter keyword (if different only) |
|--------------|-------------------------|------------------------------------|
| name         | gacha name              | gachaName                          |
| start_date   | start date as timestamp | publishedAt                        |
| end_date     | end date as timestamp   | closedAt                           |
| description  |                         |                                    |
| rates        | a list of gacha rates   |                                    |
| annotation   |                         |                                    |
| gacha_period |                         | gachaPeriod                        |
| sub_name     |                         | gachaSubName                       |
| type         | gacha type              | gachaType                          |


#### Functions
#### ```get_start_date()```
Returns a datetime object for the start date of the Gacha.
#### ```get_end_date()```
See ```get_start_date()```


## BandoriLoader
```pydori.bandori_loader.BandoriLoader(region = 'en/')```

BandoriApi inherits from this class. **It is only meant for internal use, and its purpose is to make api calls to bandori.party and bandori.database and return the result as dictionaries or lists.** It should not be normally instantiated, but is useful sometimes for debugging.


# Credits

  

[![PyPI license](https://img.shields.io/pypi/l/pydori.svg)](https://pypi.python.org/pypi/pydori/)

  

This project is licensed under the MIT license.

  

API provided by [bandori.party](https://bandori.party/) and [bandori database](https://bangdream.ga/).

  

I do not own any logos, images, or assets of the BanG Dream! Franchise, they are the property and trademark of Bushiroad.
