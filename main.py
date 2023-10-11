from flask import Flask, render_template, session, redirect, url_for, request
import db
app = Flask(__name__)
app.secret_key="G201004005"


@app.route('/')
def index():
	nomeUsuario = 'Visitante'
	logado = False
	try:
		if session['user']:
			nomeUsuario = session['user']
			logado = True
		else:
			pass

	except Exception:
		pass

	return render_template('index.html', logado=logado,username=nomeUsuario, posts=db.read_posts())

@app.route('/register')
def registrar():
	return render_template('register.html')

@app.route('/postar', methods=["POST"])
def postar():
    postContent = request.form['post']
    user = session['user']

    db.newpost(user,postContent)
    return redirect('/')

@app.route('/perfil',methods=['POST'])
def perfis():
	name = request.form['nome']

	return render_template('/perfilproprio.html',username=name)

@app.route('/like',methods=["POST"])
def likepost():
		idpost = request.form['id']
		db.like_post(idpost)
		return "a"

@app.route('/register-user', methods=["POST"])
def register_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password == confirm_password:
        if len(password) >= 8 and len(password) <= 10:
            if len(username) <= 10:
                if password in ['.','?',":","^",'~','!',"@","$","%","&",'-','_']:

                    db.register(username,email,password)
                    session['user'] = username

                    return redirect('/')
                else:    
    
                    return 'Registration failed, Your pass dont have any special char. <a href="/">back to the principal page here</a>'
            else:    
    
                return 'Registration failed, Name limit is 10 digits. <a href="/">back to the principal page here</a>'
        else:    
    
            return 'Registration failed, Your pass is soo big or little 8 (min), 10 (max). <a href="/">back to the principal page here</a>'
    else:    
    
        return 'Registration failed, the passwords are not iguals. <a href="/">back to the principal page here</a>'


@app.route('/logout')
def logout():
    # Remover a chave de usuário da sessão (logout)
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/login-user', methods=["POST"])
def loginuser():
	password = request.form['password']
	username = request.form['username']

	b = db.login(username,password)
	if b == True:
		print(b)
		session['user'] = username
		return redirect('/')
	else:	
		print(b)
		return "Fail to login."

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000)