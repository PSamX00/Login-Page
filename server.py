from flask import Flask,request,render_template


app = Flask(__name__)


@app.route('/')
def log_in():
    return render_template("login.html")
small_database={'sam': '123', 'dan': 'qwerty', 'Apu': 'Qqq123', 'Quin': '7890','Kay': '78945','One': '12@12','Ani': 'Anio@420',}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name=request.form['username']
    name_to_upper= name.upper()
    password=request.form['password']
    print(name, password)
    if name not in small_database:
	    return render_template('login.html',info='User Does not Exists')
    else:
        if small_database[name]!=password:
            return render_template('login.html',info='Wrong Password')
        else:
	         return render_template('user.html',name=name_to_upper)

if __name__ == '__main__':
    app.run()
