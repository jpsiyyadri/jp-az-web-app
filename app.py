from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
	return """
	<!DOCTYPEhtml>
	<h1>Hello World, welcome to my new azure web app</h1>
	<a href="/form">add new name</a><br>
	<a href="/view">view names</a>

	"""

@app.route("/form")
def form():
	return """
	<!DOCTYPEhtml>
	<form action="/add" method=POST>
		<input type="text" name=user_name>
		<input type="submit" value=add>
	</form>
	"""

@app.route("/add", methods=["POST"])
def add():
	if request.method == 'POST':
		name = request.form.get('user_name')
		with open("names.txt", "a") as f:
			f.write("\n"+name)
			f.close()
		return '''
		<!DOCTYPEhtml>user has been added succesfully
		<a href="/view">click here view names</a>
		'''
	return redirect("/form")

@app.route("/view", methods=["GET"])
def view():
	with open("names.txt", "r") as f:
		names = f.read().split("\n")
		f.close()
		html = "".join(["<li>{}</li>".format(i) if i != "" else "" for i in names])
		return """
			<!DOCTYPEhtml><ul>{0}</ul>
			<a href="/">home</a>
		""".format(html)
	return []