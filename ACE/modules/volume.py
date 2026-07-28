import pyautogui
from voice import VoiceEngine

voice = VoiceEngine()


class Volume:

    def control(self, command):

        command = command.lower()

        if "volume up" in command:

            pyautogui.press("volumeup")

            voice.speak("Volume Up")

        elif "volume down" in command:

            pyautogui.press("volumedown")

            voice.speak("Volume Down")

        elif "mute" in command:

            pyautogui.press("volumemute")

            voice.speak("Muted")