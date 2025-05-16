from flask import Flask, render_template, request, session
from dotenv import load_dotenv
import os
import google.generativeai as genai

app = Flask(__name__)
app.secret_key = "supersecretkey"
load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    prompt = ""
    response_text = ""
    if request.method == "POST":
        prompt = request.form.get("input")  # not 'chat', use 'input' to match input name
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        response_text = response.text  

    return render_template("chat.html", prompt=prompt, response_text=response_text)

@app.route("/clear")
def clear_chat():
    session.clear()
    return render_template("chat.html", history=[])

if __name__ == "__main__":
    app.run(debug=True)
