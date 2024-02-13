from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/my/secret/page")
def secret():
    return "Shh!"

@app.route("/user/<username>")
def user_page(username):
    return f"Welcome,{username}!"

@app.route("/blog/post/<int:post_id>")
def show_post(post_id):
    return f"This is the page fot post #{post_id}"