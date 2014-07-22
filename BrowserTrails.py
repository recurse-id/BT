from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    url = request.args.get("url")
    selection = request.args.get("selection")

    return url + " "+ selection





if __name__ == '__main__':
    app.run()
