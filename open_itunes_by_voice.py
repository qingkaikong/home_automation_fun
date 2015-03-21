'''
Script to open itunes by voice, and you need the following dependence:
(1) speech_recognition library
(2) PyAudio
(3) FLAC

I found it is a quite slow in terms of the recognition, maybe this is 
because it use the google speech recognition api?

Example: 
say 'open ituns', it will open itunes
say 'finish', it will stop listening 
if you start with 'say ...', it will repeat you ^)^

author: Qingkai
qingkai.kong@gmail.com
2015-03-21

'''

import speech_recognition as sr
r = sr.Recognizer()
import os

while 1:
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source)  
        
    try:                 # listen for the first phrase and extract it into audio data
        st = r.recognize(audio)
        print st
        if st == 'finish':
            break

        if st == 'open iTunes':
            os.system('open -a /Applications/iTunes.app/Contents/MacOS/iTunes')
            
        if st.split()[0] == 'say':
            os.system(st)
    except:
        pass

try:
    print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")