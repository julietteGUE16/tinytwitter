from flask import Flask, render_template, request, redirect, url_for
import json,emoji
app = Flask(__name__)


with open("messages.json", "r") as file:
    items = json.loads(file.read())


@app.route('/chat')
def listMessages():
    return render_template("chat.html", messages = items)


@app.route('/chat/add', methods=['POST'])
def addMessage():
    message = { "name": request.form['pseudo'], "message": request.form['text'], "like": request.form['like']}
    items.append(message)
    with open("messages.json", "w") as file:
        file.write(json.dumps(items, indent=2))
    return redirect(url_for("listMessages"))

def is_liked():
    like = "aimé"
    return like
