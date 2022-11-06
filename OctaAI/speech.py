import speech_recognition as sr
import pyaudio
import pywhatkit

def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("say somthin...")
        audio = recorder.listen(source)
    text = recorder.recognize_google(audio)
    print(f"you said : {text}")
    return text
    
get_audio()