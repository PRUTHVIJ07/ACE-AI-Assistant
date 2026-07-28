from modules.browser import Browser
from modules.music import Music
from modules.system import System
from modules.volume import Volume
from modules.apps import Apps
from modules.ai import AI

from voice import VoiceEngine


# ----------------------------
# Initialize Modules
# ----------------------------

voice = VoiceEngine()

browser = Browser()
music = Music()
system = System()
volume = Volume()
apps = Apps()
ai = AI()


# ----------------------------
# Short-term Conversation Memory
# ----------------------------
# Stores only the last few exchanges so follow-ups like "yes"/"haan"
# can be resolved against what ACE just said. Kept small on purpose —
# this is NOT meant to be a full chat history, just enough context.

MAX_HISTORY_TURNS = 3  # keeps last 3 user+ACE exchanges (6 messages)

conversation_history = []


def _remember(user_text, ace_reply):
    conversation_history.append({"role": "user", "content": user_text})
    conversation_history.append({"role": "assistant", "content": ace_reply})

    # trim to last N turns (each turn = 2 messages)
    max_messages = MAX_HISTORY_TURNS * 2
    if len(conversation_history) > max_messages:
        del conversation_history[: len(conversation_history) - max_messages]


# ----------------------------
# Command Executor
# ----------------------------

def execute_command(command):

    command = command.lower().strip()

    print(f"[COMMAND] {command}")

    # ==================================
    # EXIT
    # ==================================

    if command in ["exit", "quit", "goodbye"]:

        voice.speak("Goodbye.")

        conversation_history.clear()

        exit()

    # ==================================
    # OPEN APPLICATION / WEBSITE (fast path for exact phrasing)
    # ==================================

    if command.startswith("open "):

        target = command.replace("open", "", 1).strip()

        if apps.open_app(target):

            voice.speak(f"Opening {target}")

            return

        if browser.open_site(target):

            voice.speak(f"Opening {target}")

            return

        voice.speak(f"I couldn't find {target}")

        return

    # ==================================
    # SEARCH GOOGLE (fast path)
    # ==================================

    if command.startswith("search "):

        query = command.replace("search", "", 1).strip()

        voice.speak(f"Searching {query}")

        browser.google_search(query)

        return

    # ==================================
    # PLAY MUSIC (fast path)
    # ==================================

    if command.startswith("play "):

        music.play(command)

        return

    # ==================================
    # VOLUME (fast path)
    # ==================================

    if (
        "volume" in command
        or "mute" in command
        or "unmute" in command
    ):

        volume.control(command)

        return

    # ==================================
    # SYSTEM COMMANDS (fast path)
    # ==================================

    if system.execute(command):

        return

    # ==================================
    # AI FALLBACK — understands ANY phrasing/language, remembers the
    # last few exchanges, and can trigger ANY tool below.
    # ==================================

    voice.speak("Let me think...")

    result = ai.ask(command, history=conversation_history)

    print("\nACE:", result)

    reply = result.get("reply", "")

    voice.speak(reply)

    # remember this exchange for future follow-ups ("yes"/"haan" etc.)
    _remember(command, reply)

    action = result.get("action", "none")
    target = result.get("target", "")

    if action == "play_music" and target:
        music.play(f"play {target}")

    elif action == "search_web" and target:
        browser.google_search(target)

    elif action == "open_app" and target:
        if not apps.open_app(target):
            browser.open_site(target)

    elif action == "adjust_volume" and target:
        volume.control(target)

    elif action == "system_command" and target:
        system.execute(target)