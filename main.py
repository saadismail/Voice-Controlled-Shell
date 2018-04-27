from gtts import gTTS
import speech_recognition as sr
import random
import os
import time
import modules

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

def speak_to_speaker(text):
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save("tts.mp3")
    os.system("mpg321 -q tts.mp3")

def beep_high():
    os.system("mpg321 -q beep_hi.mp3")

def beep_low():
    os.system("mpg321 -q beep_lo.mp3")

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    speak_to_speaker('Hi, How may I help you')

    while (1):
        response = recognize_speech_from_mic(recognizer, microphone)

        if response["error"]:
            print("ERROR: {}".format(response["error"]))
            continue;

        text = str(format(response["transcription"])).lower()
        print("You said:" + text)

        if ('hello' in text):
            beep_high()

            while (1):
                response = recognize_speech_from_mic(recognizer, microphone)
                if response["error"]:
                    print("ERROR: {}".format(response["error"]))
                    continue

                text = str(format(response["transcription"])).lower()
                print("You said:" + text)
                modules.runCommand(text)
                break

            beep_low()

        if 'exit' in text:
            speak_to_speaker("Good Bye")
            speak_to_speaker("Have a nice day")
            print("Good Bye")
            break
