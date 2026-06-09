from flask import Flask, render_template, request

app = Flask(__name__)

# FAQ data
faq = {
    "hi": "Hello! How can I help you?",
    "hello": "Hello! How can I help you?",
    "tq": "You're welcome!",
    "thank you": "You're welcome!",

    "what is python": "Python is a simple programming language.",
    "what is html": "HTML is used to create web pages.",
    "what is css": "CSS is used to design web pages.",
    "what is chatbot": "A chatbot is a program that responds to users."
}

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/chat')
def chat():
    return render_template("chat.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/get', methods=["POST"])
def chatbot():
    msg = request.form["msg"].lower().strip()

    if msg in faq:
        return faq[msg]
    else:
        return "Sorry, I don't understand."

if __name__ == "__main__":
    app.run(debug=True)