# https://soundcloud.com/theletter10/sets/rick-and-morty-episode-5
# https://github.com/hnarayanan/shpotify
# GCP
# darksky weather api : cf7422de0aa9d26f97ff517ab4bcbe46
# Hamilton coords: 43.0521° N, 75.4061° W

import pygame as pg
import speech_recognition as sr
import subprocess
<<<<<<< Updated upstream
import spotipy
import spotipy.util as util
import sys
=======
import time
from forecastiopy import *

>>>>>>> Stashed changes

def play_music(music_file, volume=0.8):
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
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! ({})".format(music_file, pg.get_error()))
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


def main():
    # Greetingz
    # play_music("lookatme.mp3", 1)

    dats = recordAudio()
    #print(dats)

    # Split into words list
    dat_words = dats.split()

    # Trying to give more flexibility to spotify requests
    # Could be "play Spotify" or "Spotify play" or "Spotify play song"
    if "Spotify" in dat_words or "spotify" in dat_words:
        sp = spotipy.Spotify() # Instance of spotipy

        # When searching for a song to play
        uri = False
        if len(dat_words) > 2:
            search = sp.search(q=" ".join(dat_words[2:]))
            if search:
                uri = search['tracks']['items'][0]['uri']

        # Play meeseeks
        music_file = "cando.mp3"
        volume = 1
        play_music(music_file, volume)

        # Play the song using shpotify
        if uri:
            subprocess.check_output(['spotify','play', 'uri', uri])
        else:
            subprocess.check_output(['spotify','play'])

    # If no known command, play sucks and call main recursively to
    # start the process over
    else:
        music_file = "sucks.mp3"
        volume = 1
        play_music(music_file, volume)
        main("play Spotify")


<<<<<<< Updated upstream
if __name__ == "__main__":
    main()
=======
# if __name__ == "__main__":
#     print(" hello ")
#     main()



# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        data = recognizer.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + data)
        checkData(data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def checkData(data):
    print(data)
    if data == "play Spotify":
        music_file = "cando.mp3"
        volume = 1
        play_music(music_file, volume)
        subprocess.check_output(['spotify','play'])

def spotify(data):
    result = {
      'a': lambda x: x * 5,
      'b': lambda x: x + 7,
      'c': lambda x: x - 2
    }['a'](3)


r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
print(stop_listening)
# `stop_listening` is now a function that, when called, stops background listening
>>>>>>> Stashed changes

# do some other computation for 5 seconds, then stop listening and keep doing other computations
for _ in range(10): time.sleep(0.1)  # we're still listening even though the main thread is doing other things
# for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things
# stop_listening()  # calling this function requests that the background listener stop listening
while True: time.sleep(0.1)


# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)
#
