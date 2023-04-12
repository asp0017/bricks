from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*":{'origins':"*"}})
app.config.from_object(__name__)


# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world!")


@app.route('/bricks', methods=['GET'])
def bricks():
    return("Bricks專案管理實用工具讚讚!")


if __name__ == "__main__":
    app.run(debug=True)