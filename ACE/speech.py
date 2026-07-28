import speech_recognition as sr


class SpeechEngine:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):

        with sr.Microphone() as source:

            print("\n🎤 Listening...")

            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = self.recognizer.listen(source)

        try:

            text = self.recognizer.recognize_google(audio)

            print("👤 You:", text)

            return text.lower()

        except sr.UnknownValueError:

            return ""

        except sr.RequestError:

            return ""