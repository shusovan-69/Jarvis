import requests

def ask_ai(question):

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": question,
        "stream": False
    }

    try:
        response = requests.post(url, json=data, timeout=60)

        result = response.json()

        return result.get("response", "I couldn't understand that.")

    except Exception as e:
        print("AI error:", e)
        return "Sorry, something went wrong."