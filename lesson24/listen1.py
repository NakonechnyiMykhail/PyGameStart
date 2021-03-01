# recognizes a voice
# https://pypi.org/project/SpeechRecognition
# pip3 install SpeechRecognition wheel
# ONLY FOR MAC 
# # installation HOMEBREW manager
# # /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# #
# # brew install portaudio
# # brew install flac
######### next installation
# pip3 install pyaudio
# pip3 install google-api-python-client 

import speech_recognition

# obtain audio from the microphone
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something: ")
    audio = recognizer.listen(source)

print("You said:")
print(recognizer.recognize_google(audio, language="en")) 


