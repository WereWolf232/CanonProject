from pydub import AudioSegment
import librosa
import soundfile
#choose whether to do simple harmony or canon
#make the file input and output more user friendly
#maybe let the user test different canon states and then decide which one to write to file
#could take input on which harmony and at which beat the user would like the canon to start

def main():
    sound1 = AudioSegment.from_file("song.wav", format="wav")
    #request input from user whether he wants harmony or canon
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
        harmony.export("MAboi.wav", format="wav")   #output harmony

    else:                               #implement delayed harmony 
        delayed = delay(panned[1])
        canon = overlay(delayed, panned[0])
        canon.export("MAboi.wav", format="wav")    #output canon
        


def harmonize(sound1):
    #set sound2 1 octave down/up
    y, sr = librosa.load("song.wav", sr=16000)
    shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=-12)
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