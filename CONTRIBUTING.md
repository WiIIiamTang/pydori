# Contributing

You can help by adding more endpoints/your own features/fixes:

1. Fork the repo
2. Push changes to your own branch
3. Submit a pull request for review (Not into master please)


To stay consistent, BandoriApi ```get_``` functions should return **lists** (except for assets). The lists should contain BandoriObjects.
BandoriObjects should have all the attributes returned from the JSON in the api GET request. They **do not have to have the same name**, but then it's important to point it out either in the docs or in the comments so I know.


**If you can, also help contribute to the official documentation of bandori.party and bandori database api! See the wiki!**
