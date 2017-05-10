# Mr. Meeseeks AI

The beginning of my beautiful yet simple Mr. Meeseeks based AI that will run on my rasberry pi and do cool stuff. Inspired by Rick and Morty Season 1 Episode 5

<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6QRqMSb05tMl41nAK-_Sn6RS79qg2qy2aiIjv7dju2CwGlEpFIQ"/>
</p>

Also a good introduction to using GCP, currently only using the Speech API, but hopefully will expand

Using Python 2.7.10

## Initialization 
### Needs : 
  - GCP account
  - DarkSky weather API key
  - Spotify application downloaded on your machine

### To run : 
 - Install the Google Cloud SDK - https://cloud.google.com/sdk/ 
 - Follow the SDK initialization instructions here - https://cloud.google.com/sdk/docs/
 - Follow the Speech API initialization instructions here - https://cloud.google.com/speech/docs/getting-started
 - Install all the necessary packages used in meeseeks.py - Hopefully we will use a package manager in the future
 - Run by doing `python meeseeks.py`
 


## To do : 
- [ ] Make a good way to store API keys
- [ ] Seperate Spotify logic from main function
- [ ] Add functionality to tell us the weather for that day for a given location
  - Probably will just end up using the built in voice using subproccess say command
  - [ ] Allow different voices aka meeseeks voice for any string ( ? )
- [ ] Make it a chatbot ?  https://chatbotsmagazine.com/the-complete-beginner-s-guide-to-chatbots-8280b7b906ca
- [ ] Expand Spotify logic to allow much more detailed commands for 
  - [ ] Playlists
  - [ ] Artists
  - [ ] Albums
  - [ ] Specific songs
  - [ ] Specific songs by specific artists
  - [ ] Genres
  - [ ] Stations ( ? ) 
  - [ ] Radio ( ? )
- [ ] Remove the coupling of spotify commands to having spotify application installed ( ? )
- [ ] Create a package management system
- [ ] Use GCP Natural language processor to make the AI comprehend english better rather than hard coded commands
- [ ] Integrate with G-Suite
  - [ ] Gmail
  - [ ] Calendar
- [ ] Slack integration ( ? )
- [ ] Port it to a raspberry pi 
  - [ ] Create a way to turn on and off the AI
    - [ ] Meeseeks box with a button on it ( ? )
    - [ ] Iphone application ( ? )
    - [ ] Web App ( ?) 
