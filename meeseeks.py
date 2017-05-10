# https://soundcloud.com/theletter10/sets/rick-and-morty-episode-5

import pygame as pg
import speech_recognition as sr
import subprocess
import spotipy
import spotipy.util as util
import sys

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
    dats = recordAudio()
    #print(dats)

    # Split into words list
    dat_words = dats.split()

    # Trying to give more flexibility to spotify requests
    # Could be "play Spotify" or "Spotify play" or "Spotify play song"
    if "Spotify" in dat_words or "spotify" in dat_words:
        sp = spotipy.Spotify() # Instance of spotipy

        # When searching for a song to play
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


if __name__ == "__main__":
    main()



# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)
#
