from flask import Flask, render_template, request, redirect, url_for
import json
import uuid

app = Flask(__name__)

with open("messages.json", "r") as file:
    items = json.loads(file.read())

@app.route('/chat')
def listMessages():
    return render_template("chat.html", messages=items)

@app.route('/chat/add', methods=['POST'])
def addMessage():
    id = uuid.uuid4().hex
    message = {"id": id, "name": request.form['pseudo'], "message": request.form['text'], "like": 0, "comments": []}
    items.append(message)
    with open("messages.json", "w") as file:
        file.write(json.dumps(items, indent=2))
    return redirect(url_for("listMessages"))


@app.route('/chat/like', methods=['POST'])
def is_liked():
    id = request.form['id']
    for x in items:
        if x['id'] == id:
            x['like'] = int(x['like']) + int(1)
    with open("messages.json", "w") as file:
        json.dump(items, file)
    return redirect(url_for("listMessages"))


@app.route('/chat/comment', methods=['POST'])
def add_comment():
    id = request.form['id']
    comment = request.form['commented']
    for x in items:
        if x['id'] == id:
            x['comments'].append(comment)
    with open("messages.json", "w") as file:
        file.write(json.dumps(items, indent=2))
    return redirect(url_for("listMessages"))
