from flask import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route("/success")
def success():
    return "logged in successfully"

@app.route('/validate', methods = ["POST"])
def validate():
    if request.method == "POST" and request.form['pass'] == 'jtp':
        return redirect(url_for("success"))
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)