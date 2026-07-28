import pywhatkit


class Music:

    def play(self, command):

        song = command.replace("play", "").strip()

        pywhatkit.playonyt(song)