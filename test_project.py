from pydub import AudioSegment, silence
import librosa
import soundfile
from project import harmonize, pan, delay, overlay
import numpy

def test_harmonize():
    #test 2 known pitches
    y, sr = librosa.load("song.wav", sr=16000)
    #get frequency
    a = librosa.feature.spectral_rolloff(y, sr)
    shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=-12)
    if not numpy.array_equal(a-12, librosa.feature.spectral_rolloff(shifted)):
        raise ValueError
    
    


def test_delay():  
    if silence.detect_nonsilent(delay(librosa.load("song.wav", sr=16000)[0]).silent(300)):   #silent in beginning
        raise ValueError   
    #AudioSegment(…).duration_seconds
    


def test_overlay():
    y, sr = librosa.load("song.wav", sr=16000)
    x, sr = librosa.load("sound2.wav", sr=16000)
    if silence.detect_silence(overlay(y, x).silent(300)):   #not silent in beginning
        raise ValueError
    #AudioSegment(…).duration_seconds
    