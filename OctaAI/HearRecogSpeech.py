import speech_recognition as sr


def speech2text():
    r = sr.Recognizer()
    mic = sr.Microphone()

    try:
       # print("A moment of silence, please...")
        with mic as source: r.adjust_for_ambient_noise(source)
       # print("Set minimum energy threshold to {}".format(r.energy_threshold))
        print("listening...")
        with mic as source: audio = r.listen(source)
       # print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # this version of Python uses unicode for strings (Python 3+)
            wordsres = format(value)
        except sr.UnknownValueError:
            wordsres = "Oops! Didn't catch that"
        except sr.RequestError as e:
            wordsres = "Uh oh! Couldn't request results from Google Speech Recognition service,check internet Please! {0}".format(e)

        return wordsres
    
    except KeyboardInterrupt:
        pass


