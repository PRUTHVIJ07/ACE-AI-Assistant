import os
import subprocess


class Apps:

    def __init__(self):

        self.apps = {
            "notepad": "notepad",
            "calculator": "calc",
            "paint": "mspaint",
            "chrome": "chrome",
            "edge": "msedge",
            "cmd": "cmd",
            "powershell": "powershell",
            "task manager": "taskmgr",
            "settings": "start ms-settings:",
            "explorer": "explorer",
        }

    def open_app(self, app):

        app = app.lower()

        if app not in self.apps:
            return False

        command = self.apps[app]

        try:

            if command.startswith("start "):
                os.system(command)
            else:
                subprocess.Popen(command)

            return True

        except Exception:
            return False