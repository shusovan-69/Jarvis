import webbrowser


def search_web(command):

    command = command.replace("search", "")
    command = command.strip()

    url = f"https://www.google.com/search?q={command}"

    webbrowser.open(url)