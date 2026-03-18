import subprocess
import webbrowser


def open_app(app_name):

    app_name = app_name.lower()

    if "chrome" in app_name:
        webbrowser.open("https://www.google.com")

    elif "spotify" in app_name:
        subprocess.Popen("spotify")

    elif "vscode" in app_name:
        subprocess.Popen("code")

    elif "notepad" in app_name:
        subprocess.Popen("notepad")

    else:
        print("App not recognized")