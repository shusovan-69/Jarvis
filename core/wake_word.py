from core.voice import listen

def wait_for_wake_word():

    while True:

        command = listen()

        if " jarvis" in command:
            return True