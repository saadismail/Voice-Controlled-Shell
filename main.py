import random
from gtts import gTTS
import speech_recognition as sr
import os
import time

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

if __name__ == "__main__":
	recognizer = sr.Recognizer()
	microphone = sr.Microphone()

	tts = gTTS(text='Hello', lang='en', slow=True)

	while (1):
		response = recognize_speech_from_mic(recognizer, microphone)

		if response["error"]:
			print("ERROR: {}".format(response["error"]))
			continue;

		text = str(format(response["transcription"]));
		print("You said:" + text)

		if 'exit' in text:
			print("Good Bye")
			break;