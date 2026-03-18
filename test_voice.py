from core.voice import listen, speak

speak("Hello, I am Jarvis")

command = listen()

speak("You said " + command)