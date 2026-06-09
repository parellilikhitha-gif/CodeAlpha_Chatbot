import difflib

faq = {
    "what is python": "Python is a programming language.",
    "what is flask": "Flask is a Python web framework.",
    "what is html": "HTML is used to create web pages.",
    "what is css": "CSS is used to style web pages.",
    "what is javascript": "JavaScript adds interactivity.",
    "what is chatbot": "Chatbot is a program that talks with users.",
    "who created python": "Python was created by Guido van Rossum.",
    "what is ai": "AI means Artificial Intelligence."
}

def get_response(user_input):
    user_input = user_input.lower().strip()

    # ✅ UPDATED GREETING
    if user_input in ["hi", "hello", "hey"]:
        return "Hello, how  can I help you? 🙂"

    # thank you reply
    if user_input in ["tq", "thank you", "thanks"]:
        return "You're welcome 😊"

    # similarity matching
    match = difflib.get_close_matches(user_input, faq.keys(), n=1, cutoff=0.5)

    if match:
        return faq[match[0]]
    else:
        return "Sorry, I don't understand. Please ask something else."