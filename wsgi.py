from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
<<<<<<< HEAD
    return "Hello Eliad 222"
=======
    return "Hello Eliad 2"
>>>>>>> d54bea9ca958ded33051d510835afce44e1262fc

if __name__ == "__main__":
    application.run()
