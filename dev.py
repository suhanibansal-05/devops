from flask import Flask

app = Flask(_name_)

@app.route("/info")

def myinfo():
	return "i am suhani hi"
@app.route("/phone")
def myphone():
	return "8484026911"

app.run(host="0.0.0.0")
