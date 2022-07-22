# CanonProject
#### Video Demo:  <URL HERE>
#### Description:
This program takes as input an audio file which (preferably) contains a short melody and outputs a harmonized version or a canon of the original melody.

<ins>Usage -<ins>
  - A .wav file is required and a .wav file is outputted
  
  - To choose between harmony and canon use 'h/H' or 'c/C' respectively.
  
  - Harmony -  pitch measured in semi-tones.
  
  - Canon - imitation start point measured in beats.


  

  <ins>The user can choose between 2 options:<ins>

- 1. Harmony - The same melody in a different pitch overlayed on top of the original melody. User can choose pitch (semi-tones).

- 2. Canon - a melody with one imitation of the melody played after a given duration (e.g., quarter rest, one measure, etc.). the imitative melody, which is
played in a different voice is an exact replication of the original melody. User can choose at which point the imitiative melody comes in (beats).

  

  
<ins>design choices:<ins>
- regarding input of audio
- regarding changing pitch and length in canon
- pitch: maybe not to allow all pitches so it doesn't sound shot
- length in canon: maybe allow just some inputs so it doesn't sound shit


  
  
<ins>Files:<ins>
- project.py - The implementation of the program
- test_project.py - Testing that the program works correctly
- canon.wav / harmony.wav - The output file
- requirements.txt - All the packages you need to download in order to run the program.
  
