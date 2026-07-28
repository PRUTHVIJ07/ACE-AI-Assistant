import os
from voice import VoiceEngine

voice = VoiceEngine()


class System:

    def execute(self, command):

        command = command.lower()

        if "open notepad" in command:
            voice.speak("Opening Notepad")
            os.system("notepad")
            return True

        elif "open calculator" in command:
            voice.speak("Opening Calculator")
            os.system("calc")
            return True

        elif "open paint" in command:
            voice.speak("Opening Paint")
            os.system("mspaint")
            return True

        elif "shutdown" in command:
            voice.speak("Shutting down computer")
            os.system("shutdown /s /t 5")
            return True

        elif "restart" in command:
            voice.speak("Restarting computer")
            os.system("shutdown /r /t 5")
            return True

        return False