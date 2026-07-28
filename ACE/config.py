import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# -----------------------------
# Assistant Settings
# -----------------------------
ASSISTANT_NAME = "ACE"
VERSION = "2.0"

# -----------------------------
# OpenRouter API
# -----------------------------
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")



OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

MODEL = "openrouter/free"

# -----------------------------
# Voice
# -----------------------------
VOICE_RATE = 170
VOICE_VOLUME = 1.0