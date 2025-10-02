from flask import Flask, render_template, url_for, request ,session
# インポートしても下で使われてなかったら、黒めの文字になるよ。
# from flask_wtf.csrf import CSRFProtect ,generate_csrf

#Flaskのインスタンスを生成
#flaskでアプリを作りますよってやつ。

app = Flask(__name__, static_folder="./templates/imagebox")
app.config['SECRET_KEY'] = '306cf1aff2196801ea027556d43b6f618323d62238e1849ec9193a2157eb35c0'
app.secret_key = "your_secret_key"  # 適当な長い文字列に置き換える。

# csrf = CSRFProtect()

@app.route("/zatu")
def zatu():
    return render_template("zatu.html")

@app.route("/debug")
def debug():
    return render_template("debug.html")

@app.route("/")
def top():
    return render_template("top.html")

@app.route("/intro")
def intro():
    return render_template("intro.html")

# html一からではなく、問題集から取ってくる形式にすると大幅削減
# 辞書型で保存して、HTML内でジンジャーテキスト使う

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    question1    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.route("/mistake", methods=["GET", "POST"])
def mistake():
    return render_template("mistake.html")

@app.route("/question1", methods=["GET", "POST"])
def question1():
    # csrf_token = generate_csrf()
    
    if "mistake" not in session:
        session["mistake"] = 0

    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question1.html")

    
    answer=request.form.get("python")
    # pythonっていう名前のFormから取ってくるよってこと。question1.htmlから。
    cleaned_text = answer.replace('\n', '').replace('\r', '')
    # answerに含まれる改行文字を何もない状態に置き換える（改行文字を消すのと同じ意味。）
    cleaned_text = cleaned_text.replace(' ', '').replace(' ', '')

    if session["mistake"] >= 2:
        session["mistake"] = 0
        session["answer"] = answer
        # print(f"[DEBUG] mistake = {session['mistake']}")
        return render_template('mistake.html', answer = answer)
            
    if 'print("' in cleaned_text and 'ello' in cleaned_text and 'orld!")' in cleaned_text:
        session["mistake"] = 0
        return render_template('correct1.html')
        # , csrf_token=csrf_token
        
    if 'print("' in cleaned_text and 'ello' in cleaned_text and 'orld")' in cleaned_text:
        session["mistake"] = 0
        return render_template('correct1.html')
        # , csrf_token=csrf_token
            
    elif "print(HelloWorld!)" in cleaned_text or "print(HelloWorld)" in cleaned_text:
        session["mistake"] += 1
        return render_template('error1.html')
            
    else:
        session["mistake"] += 1
        return render_template('error.html')
        # ポストされた時に、テキストをrequest.form.get()で読み込む。

@app.route("/error1")
def error1():
    # csrf_token = generate_csrf()
    return render_template("error1.html")

# question1.htmlを正解した時の遷移先。
@app.route("/correct1")
def correct1():
    # csrf_token = generate_csrf()
    return render_template("correct1.html")
    # , csrf_token=csrf_token
    
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    question2    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.route("/mistake2", methods=["GET", "POST"])
def mistake2():
    return render_template("mistake2.html")

@app.route("/question2", methods=["GET", "POST"])
def question2():
    # csrf_token = generate_csrf()
    
    if "mistake" not in session:
        session["mistake"] = 0

    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question2.html")

    
    answer=request.form.get("python")
    # pythonっていう名前のFormから取ってくるよってこと。question1.htmlから。
    cleaned_text = answer.replace('\n', '').replace('\r', '')
    # answerに含まれる改行文字を何もない状態に置き換える（改行文字を消すのと同じ意味。）
    cleaned_text = cleaned_text.replace(' ', '').replace(' ', '')

    if session["mistake"] >= 2:
        session["mistake"] = 0
        session["answer"] = answer
        # print(f"[DEBUG] mistake = {session['mistake']}")
        return render_template('mistake2.html', answer = answer)
            
    if 'print(7)' in cleaned_text and 'print(9+3)' in cleaned_text and 'print("9+3")' in cleaned_text:
        session["mistake"] = 0
        return render_template('correct2.html')
        #csrf_token=csrf_token
    
    elif 'print("7")' in cleaned_text and 'print(9+3)' in cleaned_text and 'print("9+3")' in cleaned_text:
        session["mistake"] += 1
        return render_template('correct2.html')
        #表示されるけど、型が違うかもエラー

    else:
        session["mistake"] += 1
        return render_template('error.html')
        # ポストされた時に、テキストをrequest.form.get()で読み込む。

@app.route("/error2")
def error2():
    # csrf_token = generate_csrf()
    return render_template("error2.html")

@app.route("/correct2")
def correct2():
    # csrf_token = generate_csrf()
    return render_template("correct2.html")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    question3    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.route("/mistake3", methods=["GET", "POST"])
def mistake3():
    return render_template("mistake3.html")

@app.route("/question3", methods=["GET", "POST"])
def question3():
    # csrf_token = generate_csrf()
    
    if "mistake" not in session:
        session["mistake"] = 0

    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question3.html")

    
    answer=request.form.get("python")
    # pythonっていう名前のFormから取ってくるよってこと。question1.htmlから。
    cleaned_text = answer.replace('\n', '').replace('\r', '')
    # answerに含まれる改行文字を何もない状態に置き換える（改行文字を消すのと同じ意味。）
    cleaned_text = cleaned_text.replace(' ', '').replace(' ', '')

    if session["mistake"] >= 2:
        session["mistake"] = 0
        session["answer"] = answer
        # print(f"[DEBUG] mistake = {session['mistake']}")
        return render_template('mistake3.html', answer = answer)
            
    if 'print("7-3")' in cleaned_text and 'print(2*6)' in cleaned_text and 'print(24/3)' in cleaned_text and 'print(12%5)' in cleaned_text:
        session["mistake"] = 0
        return render_template('correct3.html')
        #csrf_token=csrf_token
        
    elif 'print(7-3)' in cleaned_text and 'print(2*6)' in cleaned_text and 'print(24/3)' in cleaned_text and 'print(12%5)' in cleaned_text:
        session["mistake"] += 1
        return render_template('error3.html')
    
    else:
        session["mistake"] += 1
        return render_template('error.html')
        # ポストされた時に、テキストをrequest.form.get()で読み込む。

@app.route("/error3")
def error3():
    return render_template("error3.html")

@app.route("/correct3")
def correct3():
    # csrf_token = generate_csrf()
    return render_template("correct3.html")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    question4    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.route("/mistake4", methods=["GET", "POST"])
def mistake4():
    return render_template("mistake4.html")

@app.route("/question4", methods=["GET", "POST"])
def question4():
    # csrf_token = generate_csrf()
    
    if "mistake" not in session:
        session["mistake"] = 0

    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question4.html")

    
    answer=request.form.get("python")
    # pythonっていう名前のFormから取ってくるよってこと。question1.htmlから。
    cleaned_text = answer.replace('\n', '').replace('\r', '')
    # answerに含まれる改行文字を何もない状態に置き換える（改行文字を消すのと同じ意味。）
    cleaned_text = cleaned_text.replace(' ', '').replace(' ', '')


    if session["mistake"] >= 2:
        session["mistake"] = 0
        session["answer"] = answer
        # print(f"[DEBUG] mistake = {session['mistake']}")
        return render_template('mistake4.html', answer = answer)

    if 'mojiretu="あいうえお"'in cleaned_text and 'suuti=8' in cleaned_text and 'print(mojiretu)' in cleaned_text and 'print(suuti)' in cleaned_text:
        session["mistake"] = 0
        return render_template('correct4.html')
        #csrf_token=csrf_token
    
    # error4への分岐、必要だったら、追加してくれ。＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
    elif 'mojiretu="あいうえお"' in cleaned_text and 'suuti="8"' in cleaned_text and 'print(mojiretu)' in cleaned_text and 'print(suuti)' in cleaned_text:
        session["mistake"] += 1
        return render_template('error4.html')
    
    else:
        session["mistake"] += 1
        return render_template('error.html')
        # ポストされた時に、テキストをrequest.form.get()で読み込む。

@app.route("/error4")
def error4():
    return render_template("error4.html")

@app.route("/correct4")
def correct4():
    # csrf_token = generate_csrf()
    return render_template("correct4.html")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    question5    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route("/mistake5", methods=["GET", "POST"])
def mistake5():
    return render_template("mistake5.html")

@app.route("/question5", methods=["GET", "POST"])
def question5():
    # csrf_token = generate_csrf()
    
    if "mistake" not in session:
        session["mistake"] = 0

    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question5.html")

    
    answer=request.form.get("python")
    # pythonっていう名前のFormから取ってくるよってこと。question1.htmlから。
    cleaned_text = answer.replace('\n', '').replace('\r', '')
    # answerに含まれる改行文字を何もない状態に置き換える（改行文字を消すのと同じ意味。）
    cleaned_text = cleaned_text.replace(' ', '').replace(' ', '')


    if session["mistake"] >= 2:
        session["mistake"] = 0
        session["answer"] = answer
        # print(f"[DEBUG] mistake = {session['mistake']}")
        return render_template('mistake5.html', answer = answer)

    if "=5" in cleaned_text and "=3" in cleaned_text and "print" in cleaned_text and "ython" in cleaned_text and "勉強中" in cleaned_text and "*" in cleaned_text:
        session["mistake"] = 0
        return render_template('correct5.html')
        #csrf_token=csrf_token
    
    elif '="5"' in cleaned_text or '="3"' in cleaned_text:
        session["mistake"] += 1
        return render_template('error5A.html')

    elif '=python' in cleaned_text or '=勉強中' in cleaned_text:
        session["mistake"] += 1
        return render_template('error5B.html')
    
    else:
        session["mistake"] += 1
        return render_template('error.html')
        # ポストされた時に、テキストをrequest.form.get()で読み込む。

@app.route("/error5A")
def error5A():
    # csrf_token = generate_csrf()
    return render_template("error5A.html")

@app.route("/error5B")
def error5B():
    # csrf_token = generate_csrf()
    return render_template("error5B.html")

@app.route("/correct5")
def correct5():
    # csrf_token = generate_csrf()
    return render_template("correct5.html")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    question6    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route("/mistake6", methods=["GET", "POST"])
def mistake6():
    return render_template("mistake6.html")

@app.route("/question6", methods=["GET", "POST"])
def question6():
    # csrf_token = generate_csrf()
    
    if "mistake" not in session:
        session["mistake"] = 0

    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question6.html")

    
    answer=request.form.get("python")
    # pythonっていう名前のFormから取ってくるよってこと。question1.htmlから。
    cleaned_text = answer.replace('\n', '').replace('\r', '')
    # answerに含まれる改行文字を何もない状態に置き換える（改行文字を消すのと同じ意味。）
    cleaned_text = cleaned_text.replace(' ', '').replace(' ', '')


    if session["mistake"] >= 2:
        session["mistake"] = 0
        session["answer"] = answer
        # print(f"[DEBUG] mistake = {session['mistake']}")
        return render_template('mistake6.html', answer = answer)

    if 'A=10' in cleaned_text and 'print(A)' in cleaned_text and 'A=20' in cleaned_text and 'print(A)' in cleaned_text and 'B=7' in cleaned_text and 'B=B-2' in cleaned_text and 'print(B)'  in cleaned_text:
        session["mistake"] = 0
        return render_template('correct6.html')
        #csrf_token=csrf_token

    elif 'A=10' in cleaned_text and 'print(A)' in cleaned_text and 'A=20' in cleaned_text and 'print(A)' in cleaned_text and 'B=7' in cleaned_text and 'B-=2' in cleaned_text and 'print(B)'  in cleaned_text:
        session["mistake"] = 0
        return render_template('correct6.html')
       
    elif 'B=B-2' in cleaned_text:
        session["mistake"] += 1
        return render_template('error6.html')
    
    else:
        session["mistake"] += 1
        return render_template('error.html')
        # ポストされた時に、テキストをrequest.form.get()で読み込む。

@app.route("/error6")
def error6():
    # csrf_token = generate_csrf()
    return render_template("error6.html")

@app.route("/correct6")
def correct6():
    # csrf_token = generate_csrf()
    return render_template("correct6.html")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    question7    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.route("/mistake7", methods=["GET", "POST"])
def mistake7():
    return render_template("mistake7.html")

@app.route("/question7", methods=["GET", "POST"])
def question7():
    # csrf_token = generate_csrf()
    
    if "mistake" not in session:
        session["mistake"] = 0

    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question7.html")

    
    answer=request.form.get("python")
    # pythonっていう名前のFormから取ってくるよってこと。question1.htmlから。
    cleaned_text = answer.replace('\n', '').replace('\r', '')
    # answerに含まれる改行文字を何もない状態に置き換える（改行文字を消すのと同じ意味。）
    cleaned_text = cleaned_text.replace(' ', '').replace(' ', '')
    # cleaned_textに含まれる空白文字を何もない状態に置き換える（空白文字を消すのと同じ意味。）


    if session["mistake"] >= 2:
        session["mistake"] = 0
        session["answer"] = answer
        # print(f"[DEBUG] mistake = {session['mistake']}")
        return render_template('mistake7.html', answer = answer)

    if 'price=150' in cleaned_text and 'print("ジュースは"+str(price)+"円")' in cleaned_text and 'kosuu="6"' in cleaned_text and 'print(price*int(kosuu))' in cleaned_text:
            session["mistake"] = 0
            return render_template('correct7.html')
        #csrf_token=csrf_token

    elif "price=150" in cleaned_text and "kosuu=6" in cleaned_text and "print(price*kosuu)" in cleaned_text:
        session["mistake"] = 0
        return render_template('error7A.html')
       
    elif '"ジュースは"+int(price)+"円"' in cleaned_text or 'int(price)' in cleaned_text:
        session["mistake"] += 1
        return render_template('error7B.html')

    elif "print(price*str(kosuu))" in cleaned_text:
        session["mistake"] += 1
        return render_template('error7C.html')
    
    else:
        session["mistake"] += 1
        return render_template('error.html')
        # ポストされた時に、テキストをrequest.form.get()で読み込む。

@app.route("/error7A")
def error7A():
    return render_template("error7A.html")

@app.route("/error7B")
def error7B():
    return render_template("error7B.html")

@app.route("/error7C")
def error7C():
    return render_template("error7C.html")

@app.route("/correct7")
def correct7():
    # csrf_token = generate_csrf()
    return render_template("correct7.html")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    question8    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.route("/mistake8", methods=["GET", "POST"])
def mistake8():
    return render_template("mistake8.html")

@app.route("/question8", methods=["GET", "POST"])
def question8():
    # csrf_token = generate_csrf()
    
    if "mistake" not in session:
        session["mistake"] = 0

    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question8.html")

    
    answer=request.form.get("python")
    # pythonっていう名前のFormから取ってくるよってこと。question1.htmlから。
    cleaned_text = answer.replace('\n', '').replace('\r', '')
    # answerに含まれる改行文字を何もない状態に置き換える（改行文字を消すのと同じ意味。）
    #今回の問題ではインデントが重要になるから、空白文字の削除はしない。その代わり、条件分岐がやたら長くなるのはごめん。

    if session["mistake"] >= 2:
        session["mistake"] = 0
        session["answer"] = answer
        # print(f"[DEBUG] mistake = {session['mistake']}")
        return render_template('mistake8.html', answer = answer)

    if "x" in cleaned_text and "=" in cleaned_text and "40" in cleaned_text and "if" in cleaned_text and ">" in cleaned_text and "20" in cleaned_text and ":" in cleaned_text and "    print" in cleaned_text and "y" in cleaned_text and "10" in cleaned_text and "z" in cleaned_text and "50" in cleaned_text and "y" in cleaned_text and ">" in cleaned_text and "z" in cleaned_text:
        session["mistake"] = 0
        return render_template('correct8.html')
        #csrf_token=csrf_token
    
    elif ":print" in cleaned_text: #if文のインデントがない時のエラー分岐。
        session["mistake"] += 1
        return render_template('error8A.html')
        #csrf_token=csrf_token        
    
    elif "(xは20より大きいよ)" in cleaned_text or "(yの方が大きいよ)" in cleaned_text: #printの中身が文字列になっていない時のエラー分岐。
        session["mistake"] += 1
        return render_template('error8B.html')
    
    elif ":" not in cleaned_text: #コロンのつけ忘れエラー分岐。
        session["mistake"] += 1
        return render_template('error8C.html')

    else:
        session["mistake"] += 1
        return render_template('error.html')
        # ポストされた時に、テキストをrequest.form.get()で読み込む。

@app.route("/error8A")
def error8A():
    # csrf_token = generate_csrf()
    return render_template("error8A.html") #インデントについてのerror

@app.route("/error8B")
def error8B():
    # csrf_token = generate_csrf()
    return render_template("error8B.html") #不適切な型error。　（""忘れ。）

@app.route("/error8C")
def error8C():
    # csrf_token = generate_csrf()
    return render_template("error8C.html") #コロンつけ忘れerror

@app.route("/correct8")
def correct8():
    # csrf_token = generate_csrf()
    return render_template("correct8.html")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    question9    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.route("/mistake9", methods=["GET", "POST"])
def mistake9():
    return render_template("mistake9.html")

@app.route("/question9", methods=["GET", "POST"])
def question9():
    # csrf_token = generate_csrf()
    
    if "mistake" not in session:
        session["mistake"] = 0

    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question9.html")

    
    answer=request.form.get("python")
    # pythonっていう名前のFormから取ってくるよってこと。question1.htmlから。
    cleaned_text = answer.replace('\n', '').replace('\r', '')
    # answerに含まれる改行文字を何もない状態に置き換える（改行文字を消すのと同じ意味。）
    #今回の問題ではインデントが重要になるから、空白文字の削除はしない。その代わり、条件分岐がやたら長くなるのはごめん。

    if session["mistake"] >= 2:
        session["mistake"] = 0
        session["answer"] = answer
        # print(f"[DEBUG] mistake = {session['mistake']}")
        return render_template('mistake9.html', answer = answer)

    if ':print' in cleaned_text or ': print' in cleaned_text or ':  print' in cleaned_text or ':   print' in cleaned_text or ':     print' in cleaned_text or ':      print' in cleaned_text:
        session["mistake"] += 1
        return render_template('error9A.html') #インデント忘れerror分岐
    
    elif 'x' in cleaned_text and '=' in cleaned_text and '10' in cleaned_text and 'y' in cleaned_text and '40' in cleaned_text and 'if' in cleaned_text and '>' in cleaned_text and ':' in cleaned_text and '    print' in cleaned_text and '"xの方が大きいよ"' in cleaned_text and 'else' in cleaned_text and '"yの方が大きいよ"' in cleaned_text:
        session["mistake"] = 0
        return render_template('correct9.html')
        #csrf_token=csrf_token

    elif ":" not in cleaned_text:
        session["mistake"] += 1
        return render_template('error9B.html') #コロンのつけ忘れエラー分岐。

    else:
        session["mistake"] += 1
        return render_template('error.html')
        # ポストされた時に、テキストをrequest.form.get()で読み込む。

@app.route("/error9A")
def error9A():
    # csrf_token = generate_csrf()
    return render_template("error9A.html") #インデント忘れエラー分岐

@app.route("/error9B")
def error9B():
    # csrf_token = generate_csrf()
    return render_template("error9B.html") #コロンのつけ忘れエラー分岐。

@app.route("/correct9")
def correct9():
    # csrf_token = generate_csrf()
    return render_template("correct9.html")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    question10    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.route("/mistake10", methods=["GET", "POST"])
def mistake10():
    return render_template("mistake10.html")

@app.route("/question10", methods=["GET", "POST"])
def question10():
    # csrf_token = generate_csrf()
    
    if "mistake" not in session:
        session["mistake"] = 0

    # "/"にGETメソッドで渡された場合の処理
    if request.method == "GET":
        # 取得したpostsという全データをindex.htmlに渡す
        return render_template("question10.html")

    
    answer=request.form.get("python")
    # pythonっていう名前のFormから取ってくるよってこと。question1.htmlから。
    cleaned_text = answer.replace('\n', '').replace('\r', '')
    # answerに含まれる改行文字を何もない状態に置き換える（改行文字を消すのと同じ意味。）
    #今回の問題ではインデントが重要になるから、空白文字の削除はしない。その代わり、条件分岐がやたら長くなるのはごめん。

    if session["mistake"] >= 2:
        session["mistake"] = 0
        session["answer"] = answer
        # print(f"[DEBUG] mistake = {session['mistake']}")
        return render_template('mistake10.html', answer = answer)
    
    if ':print' in cleaned_text or ': print' in cleaned_text or ':  print' in cleaned_text or ':   print' in cleaned_text or ':     print' in cleaned_text or ':      print' in cleaned_text:
        session["mistake"] += 1
        return render_template('error10A.html') #インデント忘れerror分岐
    
    if ("x<y" in cleaned_text and "y<x" in cleaned_text) or ("y>x" in cleaned_text and "x>y" in cleaned_text) or ("x<y" in cleaned_text and "x>y" in cleaned_text) or ("y>x" in cleaned_text and "y<x" in cleaned_text):
        
        if "x=10" in cleaned_text and "y=20" in cleaned_text and "if" in cleaned_text and "elif" in cleaned_text and "else:" in cleaned_text and "print" in cleaned_text and "x>y" in cleaned_text and "x<y" in cleaned_text and '("' in cleaned_text and '")' in cleaned_text:
            session["mistake"] = 0
            return render_template('correct10.html')
        
        elif ":" not in cleaned_text:
            session["mistake"] += 1
            return render_template('error10B.html') #コロンのつけ忘れエラー分岐。
    
    elif ("x<y" in cleaned_text and "y>x" in cleaned_text) or ("x>y" in cleaned_text and "y<x" in cleaned_text) or ("y>x" in cleaned_text and "x<y" in cleaned_text) or ("y<x" in cleaned_text and "x>y" in cleaned_text) or ("x<y" in cleaned_text and "x<y" in cleaned_text) or ("x>y" in cleaned_text and "x>y" in cleaned_text) or ("y>x" in cleaned_text and "y>x" in cleaned_text) or ("y<x" in cleaned_text and "y<x" in cleaned_text):
        session["mistake"] += 1
        return render_template('error10C.html') #比較演算子の向きについてのエラー分岐。
        
    else:
        session["mistake"] += 1
        return render_template('error.html')
        # ポストされた時に、テキストをrequest.form.get()で読み込む。

@app.route("/error10A")
def error10A():
    # csrf_token = generate_csrf()
    return render_template("error10A.html") #インデント忘れエラー分岐

@app.route("/error10B")
def error10B():
    # csrf_token = generate_csrf()
    return render_template("error10B.html") #コロンのつけ忘れエラー分岐。

@app.route("/error10C")
def error10C():
    # csrf_token = generate_csrf()
    return render_template("error10C.html") #コロンのつけ忘れエラー分岐。

@app.route("/correct10")
def correct10():
    # csrf_token = generate_csrf()
    return render_template("correct10.html")

# ページを作るときは、app.py に def 記述して、その後に html を作る。それだけでいい。

# 不正解の時の遷移先
@app.route("/error")
def error():
    # csrf_token = generate_csrf()
    return render_template("error.html")

if __name__=="__main__":
    #CSRF保護を初期化。CSRF拡張機能を用いて、CSRF保護を追加する。
    # csrf.init_app(app)

    #デバッグモード有効化はTrue,無効化がFalse。
    app.run(debug=False)

