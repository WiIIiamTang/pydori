# Changelog
All notable changes are documented in this file.

## 0.2.0 - 2020-05-24
### Added
- new get_current_event that uses the bandori.api instead.
- Band, Song, Gacha class now accept a ```region``` parameter
- Stamp class has a ```members``` attribute
- BandoriLoader now has a ```region``` attribute
- Documentation, README, CONTRIBUTING

### Removed
- Song attribute ```arranger```
- Gacha attribute ```annotation```

### Fixed
- get_bands, get_songs, get_gachas now correctly return all objects possible
- Song objects' attribute: urls are updated to the correct links
- Stamp class typo: renamed get_stamp_member -> get_stamp_members
- Stamp class : get_stamp_members now correctly returns the list of members

## 0.1.0 - 2020-05-23
### Added
- Core functions