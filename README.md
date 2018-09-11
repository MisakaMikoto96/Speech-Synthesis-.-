# Speech-Synthesis

This will be a very basic waveform concatenation system, whereby the acoustic units are recordings of monophones. 

simpleaudio.py
This is a version of the simpleaudio.py module that we have used in the lab sessions. The Audio class contained therein will allow you to save, load and play .wav files as well as perform some simple audio processing functions. You should not modify this file.

synth.py
This is a skeleton structure for your program. Your task is to fill in the missing components to make it work. You are free to add any classes, methods or functions that you wish but you must not change the existing argparse arguments.

monophones/
A folder containing .wav files for the monophone sounds. 

examples/
A folder containing example .wav files of how the synthesiser should sound. 


• normalise the text (convert to lower/upper case, remove all punctuation, etc.) to give you a straightforward sequence of words
• expand the word sequence to a phone sequence–making use of nltk.corpus.cmudict to do this, which is a pronunciation lexicon provided as part of NLTK. 
• concatenate the monophone wav files corresponding to the phone sequence above together in the right order to produce the required synthesised audio.

