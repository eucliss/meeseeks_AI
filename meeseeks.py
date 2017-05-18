# https://soundcloud.com/theletter10/sets/rick-and-morty-episode-5
# https://github.com/hnarayanan/shpotify
# GCP
# Hamilton coords: 43.0521 N, 75.4061 W

import pygame as pg
import speech_recognition as sr
import subprocess
import spotipy
import spotipy.util as util
import sys
from forecastiopy import *


def playMusic(musicFile, volume=0.8):
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''
    # set up the mixer
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(musicFile)
        print("Music file {} loaded!".format(musicFile))
    except pg.error:
        print("File {} not found! ({})".format(musicFile, pg.get_error()))
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        #`r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def playSpotfiy(recordingList):
    sp = spotipy.Spotify() # Instance of spotipy

    # When searching for a song to play
    uri = False # Initialize uri so the conditional below in line 85 doesnt throw erro
    if len(recordingList) > 2:
        search = sp.search(q=" ".join(recordingList[2:]))
        if search:
            uri = search['tracks']['items'][0]['uri']

    # Play meeseeks
    musicFile = "cando.mp3"
    volume = 1
    playMusic(musicFile, volume)

    # Play the song using shpotify
    if uri:
        subprocess.check_output(['spotify','play', 'uri', uri])
    else:
        subprocess.check_output(['spotify','play'])

    # ------------------------------------------
    # THis was one way I was thinking of expanding spotify
    #  Like doing something with lamda statements to parse the strings
    #    more efficiently and stuff idk just a thought I had monday night
    #
    # def spotify(data):
    #
    #     result = {
    #         'play': lamda x: subprocess.check_output(['spotify','play']),
    #         'pause': lamda x: subprocess.check_output(['spotify','pause']),
    #         'quit': lamda x: subprocess.check_output(['spotify','quit']),
    #         '': lamda x: subprocess.check_output(['spotify','pause']),
    #
    #     }
    #
    #
    #     result = {
    #       'a': lambda x: x * 5,
    #       'b': lambda x: x + 7,
    #       'c': lambda x: x - 2
    #     }['a'](3)
    # ------------------------------------------

def describeWeather(recordingList):
    # Sign up for a darksky account and get an api key, theyre free
    #  I just dont wanna put credentials on github for security reasons obv
    apikey = 'placeholder'
    HamiltonCollegeCoord = [43.048403, -75.378503]

    try :
        fio = ForecastIO.ForecastIO(apikey,
            units=ForecastIO.ForecastIO.UNITS_US,
            lang=ForecastIO.ForecastIO.LANG_ENGLISH,
            latitude=HamiltonCollegeCoord[0], longitude=HamiltonCollegeCoord[1])

        if fio.has_currently() is True:
            currently = FIOCurrently.FIOCurrently(fio)
            weatherString = 'It is currently ' + str(currently.temperature) + \
            ' degrees and ' + currently.summary + ' with a ' + \
            str(currently.precipProbability) + ' percent chance of precipitation'

            # This for loop will print all the keys in the currently object
        	# for item in currently.get().keys():
        	# 	print item + ' : ' + unicode(currently.get()[item])
        else:
        	weatherString =  'No Currently data'

        # uses built in terminal commands to say text
        # hopefully can change this eventually to meeseeks sounds
        subprocess.call(["say", weatherString])

    except:
        err = "Something went wrong. Try again."
        subprocess.call(["say", err])

def main(recording=""):
    # Greetingz
    if recording == "":
        playMusic("lookatme.mp3", 1)

        recording = recordAudio()

    # Split into words list
    # ASCII encode and also lowercase the strings
    recordingList = [x.encode('ascii') for x in recording.lower().split()]

    print(recordingList)

    # Trying to give more flexibility to spotify requests
    # Could be "play Spotify" or "Spotify play" or "Spotify play song"
    if "spotify" in recordingList:
        playSpotfiy(recordingList)
    elif "weather" in recordingList:
        describeWeather(recordingList)


    # If no known command, play sucks and call main recursively to
    # start the process over
    else:
        musicFile = "sucks.mp3"
        volume = 1
        playMusic(musicFile, volume)
        main()

if __name__ == "__main__":
    main()

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)
#
