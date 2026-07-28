import re


class NLU:

    def clean(self, command):

        command = command.lower()

        words = [
            "please",
            "can you",
            "could you",
            "would you",
            "hey ace",
            "ace",
            "kindly",
            "for me"
        ]

        for word in words:
            command = command.replace(word, "")

        command = command.strip()

        return command

    def intent(self, command):

        command = self.clean(command)

        if command.startswith(("open", "launch", "start")):
            return "open"

        if command.startswith(("play",)):
            return "play"

        if command.startswith(("search", "find")):
            return "search"

        if "volume" in command:
            return "volume"

        if "mute" in command:
            return "volume"

        return "chat"