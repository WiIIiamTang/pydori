# Contributing

## Setup
You just need to clone the repo and run  ``pip install -r requirements.txt``

## Code
Ultimately, you can do whatever you want with the source code, but I will suggest a couple of guidelines so as to keep everything consistent:

### linting
- Must pass linting with flake8
  - 80 char. max per line
  - \_\_init\_\_.py files are ignored
- type hinting strongly suggested
- snake_case functions, var.; CamelCase classes

### endpoints
- Endpoint GET functions should be added to the appropriate place:
  - **p_api.py** -> bandori api
  - **d_api.py** -> bandori database
- Endpoint GET functions should 
  1. Probably make an internal call to ``BandoriLoader._api_get``
  2. Return BandoriObjects
  3. Be instance methods
  4. Use the regional parameter when using bandori database api

### models
- Models should be added to the appropriate place:
  - **base.py** -> BandoriObject base class
  - **gamodels.py** -> bandori database models
  - **ptymodels.py** -> bandori party models
- Models are imported into **p_api.py** and **d_api.py**
- These models are the classes that get returned when using the functions from p_api.py and d_api.py
- The original json object is stored in the data attribute. It would be preferable if you made the attributes accessible as class attributes. Use the dictionary method ``.get()`` so that the attribute will be ``None`` if there is an error.
- The class attributes **do not have to have the same name** as the original data keys. But you would have to note it down somewhere (in the docs, or comments).


## Testing
Test the package with pytest and coverage.
```
coverage run -m pytest --flake8
```

## PR
1. Fork the repo
2. Push changes to your branch
3. Submit a pull request to ``dev``

### Suggested template
```
{Descriptive Title}

# Description
Description of pull request.

# Additions
List of features added.

Add endpoint-example:
Endpoint: ```pydori.p_api.PBandoriApi.get_example(id=[], filters={})```
- Gets example endpoint

Add model-example:
Model: ```pydori.models.ptymodels.ExampleClass(BandoriObject)```
- Provides model for Example

Add function-get_card_member:
Function: ```pydori.models.ptymodels.PCard(BandoriObject).get_card_member()```
- Gets card member

# Removed

# Changes

# Fixes
```

## Issues
The usual stuff; raise any issues here, like bugs, feature requests, etc.
