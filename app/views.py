from flask import render_template
from flask import request
from app import app
import RSA

@app.route('/')
@app.route('/index')
def index():
	#return "Hello, World!"
	
	#action = encrypt/decrypt/getVars
	#set Title to action
	#if action == encrypt -> title = "Encrypt"
	title = "Home"
	return render_template("index.html", title = title)
@app.route('/enc')
def encForm():
	return render_template("enc.html")
@app.route('/', methods=['POST'])
def encForm_post():
	text = str(request.form['text'])
	e = request.form['e']
	m = request.form['m']
	encText = RSA.encrypt(text, e, m)
	return render_template("encOutput.html", text = encText)