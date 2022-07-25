from pydub import AudioSegment
import librosa
import soundfile
import os


#choose whether to do simple harmony or canon

def main():
    # User picks file
    while True:
        try:
            sound1 = AudioSegment.from_file(input("choose .wav file: "), format="wav")
            break
        except (FileNotFoundError):
            print("file not found")

    # request input from user whether he wants harmony or canon
    while True:
        try:
            harmony_canon = input("harmony or canon? ")
            if harmony_canon not in ['h','H','c','C']:
                raise ValueError
            break
        except ValueError:
            pass


    harmony = harmonize(sound1)
    panned = pan(*harmony)
    if harmony_canon in ['h','H']:      #only harmonize (without delay)
        harmony = overlay(*panned)
        # Let user choose what name the file should be saved as
        while True:
            try:
                harmony.export("audio files/harmony/" + input("save as: ") + ".wav", format="wav")   #output harmony
                break
            except (FileNotFoundError):
                print("File name invalid")
        os.remove("sound2.wav")

    else:                               #implement delayed harmony
        delayed = delay(panned[1])
        canon = overlay(delayed, panned[0])
        # Let user choose what name the file should be saved as
        while True:
            try:
                canon.export("audio files/canon/" + input("save as: ") + ".wav", format="wav")   #output canon
                break
            except (FileNotFoundError):
                print("File name invalid")
        os.remove("sound2.wav")





'''
helper functions
'''


def harmonize(sound1):
    #shift sound2 by how many semitones user wants
    y, sr = librosa.load("song.wav", sr=16000)
    shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=input("shift harmony by _ semitones: "))
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
    length = 4/bpm*60*1000  #milliseconds
    silence = AudioSegment.silent(duration=length) #append silence to 2nd harmony
    delayed_harm = silence.append(sound)
    return delayed_harm


def overlay(panned_right, panned_left):
    #overlay + higher volume
    return panned_right.overlay(panned_left) + 10


if __name__ == "__main__":
    main()
