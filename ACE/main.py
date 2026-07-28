from speech import SpeechEngine
from voice import VoiceEngine
from commands import execute_command

speech = SpeechEngine()
voice = VoiceEngine()


def main():

    voice.speak("Hello Pruthviraj. I am Ace.")

    while True:

        command = speech.listen()```

        if command == "":
            continue

        if command in ["exit", "quit", "goodbye"]:

            voice.speak("Goodbye.")

            break

        execute_command(command)


if __name__ == "__main__":
    main()