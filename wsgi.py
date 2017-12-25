from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Eliad Sason 111"

if __name__ == "__main__":
    application.run()
