from modules.app_control import open_app
from modules.web_search import search_web
from core.brain import ask_ai
from core.voice import speak
import webbrowser


def route(command):

    command = command.lower()

    # OPEN CHROME
    if "open chrome" in command:
        speak("Opening Chrome")
        open_app("chrome")

    # OPEN YOUTUBE
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    # PLAY MUSIC
    elif "play" in command and "song" in command:
        speak("Playing music on YouTube")
        query = command.replace("play", "")
        webbrowser.open(
            f"https://www.youtube.com/results?search_query={query}"
        )

    # SEARCH INTERNET
    elif "search" in command:
        speak("Searching the web")
        search_web(command)

    # AI RESPONSE
    else:
        speak("Let me think")
        answer = ask_ai(command)

        print("AI:", answer)

        speak(answer)