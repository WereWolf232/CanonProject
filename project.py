from pydub import AudioSegment
import librosa
import soundfile
import os
from tkinter import *
from tkinter import filedialog


# program allows user to either create a harmony or a canon for a given audio file

harmony_canon = ""

def main():
    sound1 = openfile() 
    #request input from user whether he wants harmony or canon
    while True:
        try:
            global harmony_canon
            harmony_canon = input("harmony or canon? ")
            if harmony_canon not in ['h','H','c','C']: raise ValueError    
            break
        except ValueError: print("h/c")
    

    harmony = harmonize(sound1)
    panned = pan(*harmony)
    if harmony_canon in ['h','H']:      #only harmonize (without delay)
        harmony = overlay(*panned)
        savefile(harmony)                # save as...
        os.remove("sound2.wav")

    else:                               #implement delayed harmony 
        delayed = delay(panned[1])
        canon = overlay(delayed, panned[0])
        savefile(canon)                  # save as...
        os.remove("sound2.wav")





'''
Helper Functions
'''



def openfile():
    # '''functions as "open file..." '''
    return AudioSegment.from_file(filedialog.askopenfilename(filetypes=[("wav file", ".wav")])) 

def savefile(audio):
    # '''functions as a "save as..." '''
    filename = filedialog.asksaveasfile(defaultextension='.wav',filetypes=[("wav file",".wav")])
    audio.export(filename.name, format="wav")

def harmonize(sound1):
    # implements simple harmony
    global harmony_canon
    #shift sound2 by how many semitones user wants
    y, sr = librosa.load("song.wav", sr=16000)
    if harmony_canon in ['c','C']: shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=-12)
    else: 
        #make sure user input is a number
        while True:
            try: 
                semitones = int(input("shift harmony by __ semitones: "))
                break
            except (ValueError): print("input a number please ")
        shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=semitones)
    #need to turn shifted back to other format
    soundfile.write("sound2.wav", shifted, sr)
    sound2 = AudioSegment.from_file("sound2.wav", format="wav")
    return sound1, sound2


def pan(sound1, sound2):
    #pan the sounds to left and right
    return sound1.pan(+0.5), sound2.pan(-0.5)


def delay(sound):
    #delay the 2nd harmony to the start of the 2nd bar of the base melody
    y, sr = librosa.load("song.wav", sr=16000)
    #detect BPM
    bpm = librosa.beat.tempo(y=y, sr=sr)
    while True:
        try: 
            beats = input("The imitation melody starts after __ beats: (for default value press ENTER): ")
            if beats == "":
                beats = 4
                break
            beats = int(beats)
            break
        except ValueError: print("beats must be a number")
    length = beats/bpm*60*1000  #milliseconds
    silence = AudioSegment.silent(duration=length) #append silence to 2nd harmony
    delayed_harm = silence.append(sound)
    return delayed_harm


def overlay(panned_right, panned_left):
    #overlay + higher volume
    return panned_right.overlay(panned_left) + 10


if __name__ == "__main__":
    main()
