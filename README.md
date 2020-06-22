# Pydori

  

[![PyPI version fury.io](https://badge.fury.io/py/pydori.svg)](https://pypi.python.org/pypi/pydori/)


[![Build Status](https://travis-ci.org/WiIIiamTang/pydori.svg?branch=master)](https://travis-ci.org/WiIIiamTang/pydori)
  

A python wrapper to provide easier access to the bandori party and bandori database public APIs.

# Contents
- [Info](https://github.com/WiIIiamTang/pydori/tree/dev#info)
- [Installation](https://github.com/WiIIiamTang/pydori/tree/dev#installation)
- [Usage](https://github.com/WiIIiamTang/pydori/tree/dev#usage)
- [Examples](https://github.com/WiIIiamTang/pydori/tree/dev#examples)
- [Documentation](https://github.com/WiIIiamTang/pydori/tree/dev#documentation)
- [Contributing](https://github.com/WiIIiamTang/pydori/tree/dev#contributing)
- [Alternatives](https://github.com/WiIIiamTang/pydori/tree/dev#alternatives)
- [License](https://github.com/WiIIiamTang/pydori/tree/dev#license)
- [Credits](https://github.com/WiIIiamTang/pydori/tree/dev#credits)

# Info
Both bandori party and bandori database provide extensive public bang dream apis. The purpose of this package is to simplify accessing the various endpoints they provide, while providing sufficient detailed documentation. Additional helper functions and classes are used to automate manual tasks. Users are able to choose between the Bandori Party API or the Bandori Database API. 
 
### Features
- bandori party endpoints
- bandori database endpoints
- OOP class design
- Make use of the bandori party and bandori database api in one package
- additional functions to improve productivity

# Installation

Use pip to install:

``` pip install pydori ```


# Usage

Read this to get started on pydori:


 1. Create a bandori api instance by using the ```bandori_api()``` function. The function returns a class whose functions you can use. Bandori party api does not rely on region; Bandori database api does.
 ```python
 import pydori
 
 bapi = pydori.bandori_api()  # uses all default settings
 
 # This uses the bandori database api.
 # bapi = pydori.bandori_api(region='jp/', party=False)
 ```
 
 2. Use the bandori api class functions to access the endpoint you want. All requests made in this wrapper are GET requests using the requests module. See the documentation for what functions to use. The basic syntax is simple: ```get_{endpoint}()```, called on the api class. They usually return lists.
 ```python
 cards = bapi.get_cards()
 ```
 
 3. GET requests can take optional arguments **id** and **filters**. **id** is a list of integers corresponding to the ids of the objects you want to get. **filters** are search terms you want to filter by: the key is the category to filter, and the value is the actual value to filter by (ie. results will only include objects that have this value for this corresponding key).
 ```python
 cards = bapi.get_cards(id=[511], filters={})
 ```
 
 4. BandoriObjects are returned from the requests. The original json object will always be stored in ``BandoriObject.data`` but all (or most) of the terms can be accessed directly as class attributes. There can also be helper functions in these objects that speed up accessing relevant data.
 ```python
 cards = bapi.get_cards(id=[511])
 card = cards[0]
 
 rimi = card.get_card_member()  # returns a PMember object
 
 print(rimi.name)
 ```
 
 5. See the examples below or the Documentation if you need any help.

# Examples
This example instantiates a PBandoriApi object, gets a card by ID, and displays the card's name.
```python
import pydori

b = pydori.bandori_api()
result = b.get_cards(id=[511])
card = result[0]

print(card.name)
```

Here we get the current event and display the start and end times:
```python
from pydori import bandori_api

b = bandori_api()
current = b.get_current_event()

print(current.get_start_date())
print(current.get_end_date())
```

Pydori accepts filters for the objects, as a dictionary. This example shows how to get all songs by the band "Roselia".

```python
import pydori

b = pydori.bandori_api(region='en/', party=False)
roselia_songs = b.get_songs(id=[], filters={'bandName' : 'Roselia'})
```

# Documentation
The documentation is being moved to the [github wiki page](https://github.com/WiIIiamTang/pydori/wiki).

# Contributing

See [contributing](https://github.com/WiIIiamTang/pydori/blob/master/CONTRIBUTING.md).


# Alternatives

There are a couple of node packages that serve the same purpose, most notably [node-dori](https://github.com/LeNitrous/node-dori). If you're more familiar with javascript you could go search for those. This seems to be the only port in python so far, though.



  



  





# License
[![PyPI license](https://img.shields.io/pypi/l/pydori.svg)](https://pypi.python.org/pypi/pydori/)

This project is licensed under the MIT license.

  
  
  
# Credits

API provided by [bandori.party](https://bandori.party/) and [bandori database](https://bangdream.ga/).

  

I do not own any logos, images, or assets of the BanG Dream! Franchise, they are the property and trademark of Bushiroad.
