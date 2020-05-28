# Changelog
All notable changes are documented in this file.

## 0.4.0
### Added
- GET functions now can take a filters argument (as a dict). When the list of ids is empty, GET functions will filter with the parameters provided in the dictionary. Filter keys are based on the response json attributes. See documentation.
- _check_filters() function in BandoriLoader class; see above.

## 0.3.1 - 2020-05-26
### Fixed
- Fixed an issue where getting all possible objects was not returning the full amount.


## 0.3.0 - 2020-05-25
### Added
- get_all() function to get everything available from the api.
- BandoriObjects now print out their **data** attribute when cast to a string.
- Event objects now inherit from BandoriObject
- new function in BandoriLoader that handles getting the id of each event.

### Fixed
- Documentation : typos, small changes to wording, changed description of Event class
- get_current_event() returns an Event object and not a list anymore


## 0.2.0 - 2020-05-24
### Added
- new : get_current_event() from BandoriApi class uses the bandori.party api instead.
- Band, Song, Gacha class now accept a ```region``` parameter
- Stamp class has a ```members``` attribute
- BandoriLoader now has a ```region``` attribute
- Documentation, README, CONTRIBUTING updated

### Removed
- Song attribute ```arranger```
- Gacha attribute ```annotation```

### Fixed
- get_bands(), get_songs(), get_gachas() from BandoriApi class now correctly return all objects possible
- Song class attribute: urls now show the correct links
- Stamp class typo: renamed get_stamp_member() -> get_stamp_members()
- Stamp class : get_stamp_members() now correctly returns the list of members

## 0.1.0 - 2020-05-23
### Added
- Core functions
