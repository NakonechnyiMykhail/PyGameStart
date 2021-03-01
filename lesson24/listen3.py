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
import re 
import speech_recognition

# obtain audio from the microphone
recognizer = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()  # device_index=15

# with mic as source:
#     print("Say something: ")
#     audio = recognizer.listen(source)
with mic as source:
    print("Say something: ")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

words = recognizer.recognize_google(audio)



# respond to speech
matches = re.search("my name is (.*)", words)
if matches:
    print(f"Hey, {matches[1]}.")
else:
    print("Hey, you.")
