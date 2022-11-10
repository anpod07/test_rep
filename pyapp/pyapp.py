#!/usr/bin/env python3
from flask import Flask
from flask import render_template		# модуль для использования html-шаблонов из директории './templates'
from flask import request				# модуль для определения метода (GET, POST)
from flask import redirect				# модуль для перехода на другую страницу
from flask import session				# модуль для использования сессионных ключей (куки) https://stackoverflow.com/questions/17057191/redirect-while-passing-arguments


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		if request.form.get("btn_1"):
			Var1 = (request.form.get("inp_1"))
			somevar = 'You have entered: ' + Var1
			return render_template("index.html", somevar=somevar)
	else:
		return render_template("index.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
