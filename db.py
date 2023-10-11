#CRUD
import mysql.connector
import random
import hashlib

conexao = mysql.connector.connect(
	host='db4free.net',
	user='dimensyadmin',
	password='xrB~8Zk=r*Pv8gt',
	database='dimensydatabase'
)                 

cursor = conexao.cursor()

def register(name,email,password):
	#idPass= '94882257'
	#name='gv.dsy'
	#email='signgetsh.xit@gmail.com'
	
	password_encrypted = hashlib.md5(password.encode())
	passwd = password_encrypted.hexdigest()
	comando = f'INSERT INTO usuarios (nome, email, password) VALUES ("{name}","{email}","{passwd}")'
	cursor.execute(comando)
	conexao.commit()

#register('Thaisb','thaysmoisesgg@gmail.com','thais.gustavo')

def login(email,passw):
	password_encrypted = hashlib.md5(passw.encode())
	passwd = password_encrypted.hexdigest()

	cursor.execute("SELECT * FROM usuarios")
	result = cursor.fetchall()

	for i in result:


		if i[1] == email:
			if passwd == i[3]:
				return True
			else:
				pass
		else:
			pass

def newpost(user,postcontent):
	comando = f'INSERT INTO postagens (usuario, postcontent, likes) VALUES ("{user}","{postcontent}",0)'
	cursor.execute(comando)
	conexao.commit()


def read_posts():
	cursor.execute("SELECT * FROM postagens")
	result = cursor.fetchall()

	return result

def like_post(idPost):
	cursor.execute("SELECT * FROM postagens")
	result = cursor.fetchall()
	valor = 0

	for i in result:
		if i[0] == idPost:
			valor = int(i[3]) + 1

	cursor.execute(f"UPDATE postagens SET likes = {valor} WHERE id = {idPost}")
	conexao.commit()

def close():
	cursor.close()
	conexao.close()