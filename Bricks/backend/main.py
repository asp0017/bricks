from flask import Flask, jsonify, request
from flask_cors import CORS



app = Flask(__name__)
CORS(app, resources={r"/*":{'origins':"*"}})
app.config.from_object(__name__)

DATA = [
    {
    "account":"RuCiCa",
    "password": "RuCiCa0307"
    }
]
INFO = [
    {
        "purpose": ["營隊"],
        "identity":"學生",
        "otherTool":["Notion", "Asana"]
    }
]

# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world!")


@app.route('/bricks', methods=['GET'])
def bricks():
    return("Bricks專案管理實用工具讚讚!")

@app.route('/login', methods=['GET', 'POST'])
def login():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        #print(post_data.get("account"))
        #print(post_data.get("password"))
        response_object['status'] = "failure"
        response_object['message'] = "登入失敗"
        for account_info in DATA:
            #print(account_info)
            if account_info['account'] == post_data.get("account") and account_info['password'] == post_data.get("password"):
                response_object['status'] = "success"
                response_object['message'] = "登入成功"
                break

    else:
        response_object['items'] = DATA

    return jsonify(response_object)

@app.route('/register', methods=['POST'])
def register():
    response_object = {'status': 'success'}
    
    post_data = request.get_json()
    #print(post_data.get("account"))
    #print(post_data.get("password"))
    for account_info in DATA:
        #print(account_info)
        if account_info['account'] == post_data.get("account"):
            response_object['message'] = "此信箱已註冊過"
            response_object['status'] = "failed"
            return jsonify(response_object)
        
    DATA.append({
        "account":post_data.get("account"),
        "password":post_data.get("password")
    })
    #print(DATA)
    response_object['message'] = "註冊成功！"
    return jsonify(response_object)

@app.route('/register/survey', methods=['POST'])
def register_survey():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    INFO.append({
        "purpose": post_data.get("purpose"),
        "identity": post_data.get("identity"),
        "otherTool":post_data.get("otherTool")
    })
    return jsonify(response_object)

if __name__ == "__main__":
    app.run(debug=True)