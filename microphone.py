
import speech_recognition as sr

class Microphone:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio_data = self.recognizer.listen(source)
        return audio_data

    def recognize_speech(self, audio_data):
        try:
            text = self.recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")
            return None
