# CanonProject
#### Video Demo:  <URL HERE>
#### Description:
This program takes as input an audio file which (preferably) contains a short melody and outputs a harmonized version or a canon of the original melody.

<ins>Usage -<ins>
  - A .wav file is required and a .wav file is outputted (to "audio files" folder)

  - To choose between harmony and canon use 'h/H' or 'c/C' respectively.

  - Harmony -  pitch measured in semi-tones.

  - Canon - imitation start point measured in beats.




  <ins>The user can choose between 2 options:<ins>

- Harmony - The same melody in a different pitch overlayed on top of the original melody. User can choose pitch (semi-tones).

- Canon - a melody with one imitation of the melody played after a given duration (e.g., quarter rest, one measure, etc.). the imitative melody, which is
played in a different voice is an exact replication of the original melody. User is restricted to at which point the imitiative melody comes in (beats). The default is the beggining of the 2nd bar (5th beat).




<ins>design choices:<ins>
- user will choose file to work on by typing the path on the command line
- <ins>regarding changing pitch and length in canon:<ins>
> - pitch: allows users to freely pick how many semitones they want to shift the melody by, allowing for different harmonies.
> - canon: the start of the imitating melody is restricted to the default input (starting on the 2nd bar) so that the output file retains some musicality
- output: files will be saved inside the "audio files" folder for better organisation




<ins>Files And Folders:<ins>
- project.py - The implementation of the program + the various helper functions
- test_project.py - Testing that the program and helper functions work correctly
- audio files - where all output files are saved (divided into canon and harmony sub-folders)
- requirements.txt - All the packages you need to download in order to run the program.

