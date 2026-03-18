import time

from core.voice import listen, speak
from core.router import route
from core.wake_word import wait_for_wake_word
from gui.jarvis_ui import create_ui


# Start GUI
app, ui = create_ui()

speak("Jarvis system started")


while True:

    # Keep GUI responsive
    app.processEvents()

    # Wait for wake word
    wait_for_wake_word()

    # Listening state
    ui.set_listening()
    app.processEvents()

    speak("Yes, I am listening")

    # Capture command
    command = listen()

    if not command:
        ui.set_idle()
        continue

    # Thinking state
    ui.set_thinking()
    app.processEvents()

    # Process command
    route(command)

    # Back to idle
    ui.set_idle()
    app.processEvents()

    time.sleep(0.2)