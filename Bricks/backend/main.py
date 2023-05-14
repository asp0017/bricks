from flask import Flask, jsonify, request, url_for
from flask_cors import CORS
import logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text

app = Flask(__name__)
CORS(app, resources={r"/*":{'origins':"*"}})

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://gdsc:NCCUgdsc1234!@34.81.186.58:3306/bricksdata"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#連線到伺服器上的 MySQL
engine = create_engine("mysql+pymysql://gdsc:NCCUgdsc1234!@34.81.186.58:3306/bricksdata")

app.config.from_object(__name__)

# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return ("hello world")

@app.route('/bricks', methods=['GET'])
def bricks():
    return("Bricks專案管理實用工具讚讚!")

#test connect and get the data from MySQL
@app.route('/testMySQL', methods=['GET'])
def testMySQL():

    #建立連線
    conn = engine.connect()

    #SQL指令
    testquery = """
        SELECT id, user_password FROM users;
    """
    # testquery = """
    #     SELECT IF(SUM(IF(user_email != "test1@gmail.com", 0, 1))>0, 1, 0) AS exist FROM users;
    # """
    selectUserId = f"""
            SELECT id, user_password FROM users
            WHERE user_email = "test1@gmail.com";
        """
    test = conn.execute(text(selectUserId))
    #執行SQL指令
    # test = conn.execute(text(testquery))

    #取得欄位名稱
    keys = list(test.keys())

    #將取得資料轉換成dict
    # data = [dict(zip(keys, row)) for row in test.fetchall()]
    data1 = test.fetchall()[0][1]
    # data2 =[row for row in test.fetchall()]
    #關閉連線
    test.close()
    conn.close()
    print(data1)
    # return jsonify(data)
    return jsonify("0")

#注意的點：fetchall()只能用一次，取出會是list[tuple(), tuple()]
# 登入範例
@app.route('/login', methods=['POST'])
def login():
    response_object = {'status': 'success'}
    response_object['message'] = "登入成功"

    #連線資料庫
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)
    
    #取得檔案
    post_data = request.get_json()

    #對比信箱，如正確回傳 user_id
    try:
        selectUserId = f"""
            SELECT id, user_password FROM users
            WHERE user_email = "{post_data.get("user_email")}";
        """
        result = conn.execute(text(selectUserId))
        result_list = result.fetchall()
        response_object['user_id'] = result_list[0][0]
        user_password = result_list[0][1]
        if user_password != post_data.get("user_password"):
            response_object['status'] = "failure"
            response_object['message'] = "您的帳號或密碼不正確，請再試一次"     
    except IndexError:
        response_object['status'] = "failure"
        response_object['message'] = "您的帳號或密碼不正確，請再試一次"
    except:
        response_object['status'] = "failure"
        response_object['message'] = "SELECT user_id 失敗"
    
    result.close()
    conn.close()
    return jsonify(response_object)

#註冊 --> 對比信箱及存入信箱、密碼及使用者名稱
@app.route('/register', methods=['POST'])
def register():
    response_object = {'status': 'success'}
    response_object['message'] = "信箱註冊成功"  
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)  
    post_data = request.get_json()
    if((post_data.get("user_email")==None)|(post_data.get("user_password")==None)|(post_data.get("user_name")==None)):
        response_object['status'] = "failure"
        response_object['message'] = "有缺失信箱、密碼和使用者名稱回傳值"
        return jsonify(response_object)
    try:
        isRegisted = f"""
            SELECT IF(SUM(IF(user_email != "{post_data.get("user_email")}", 0, 1))>0, 1, 0) AS exist FROM users;
        """
        result = conn.execute(text(isRegisted))
        result_list = result.fetchall()
        if  (result_list[0][0]==0):
            addAccount = f"""
            INSERT INTO users (user_email, user_password, user_name)
            VALUES ("{post_data.get("user_email")}", "{post_data.get("user_password")}"," {post_data.get("user_name")}");
            """
            conn.execute(text(addAccount))
            conn.execute(text("COMMIT;"))
        else:
            response_object['status'] = "failure"
            response_object['message'] = "此信箱已被註冊過"
            return jsonify(response_object)
        
        selectUserId = f"""
            SELECT id FROM users
            WHERE user_email = "{post_data.get("user_email")}";
        """
        result2 = conn.execute(text(selectUserId))
        result2_list = result2.fetchall()
        response_object['user_id'] = result2_list[0][0]

    except:
        response_object['status'] = "failure"
        response_object['message'] = "SELECT user_id 失敗 或 INSERT 失敗"
        return jsonify(response_object)
    
    result.close()
    result2.close()
    conn.close()
    return jsonify(response_object)

#加入使用者資訊 #取出資訊如果為list 要轉字串
@app.route('/register/survey', methods=['POST'])
def register_survey():
    response_object = {'status': 'success'}
    response_object['message'] = "使用者調查註冊成功"  
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)  
    post_data = request.get_json()
    try:
        addInfo = f"""
            UPDATE users
            SET user_purpose = "{",".join(post_data.get("user_purpose"))}", user_identity = "{(post_data.get("user_identity"))}", user_otherTool = "{",".join(post_data.get("user_otherTool"))}" 
            WHERE id = {(post_data.get("user_id"))};
        """
        conn.execute(text(addInfo))
        conn.execute(text("COMMIT;"))

        selectId = f"""
            SELECT user_email FROM users
            WHERE id = {(post_data.get("user_id"))};
        """
        result = conn.execute(text(selectId))
        response_object['user_email'] = result.fetchall()[0][0]

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = "INSERT userInfo 失敗"
        logging.exception('Error at %s', 'division', exc_info=e)
          
    conn.close()
    return jsonify(response_object)

if __name__ == "__main__":
    app.run(debug=True)