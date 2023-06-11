##import gtts
##from playsound import playsound
##
##tts = gtts.gTTS("Hello Kids",lang="en")
##tts.save("hello.mp3")
##playsound("hello.mp3")
##print(gtts.lang.tts_langs())

import pyttsx3
converter = pyttsx3.init()
converter.say("Hello")
converter.say("star")
converter.say("circle")
converter.runAndWait()
