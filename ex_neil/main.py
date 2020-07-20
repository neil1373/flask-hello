from flask import *

app = Flask(__name__)

@app.route("/")
def template():
    return render_template("template.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/login')  
def login():
    return render_template("login.html");  
 
@app.route('/validate', methods = ["POST"])  
def validate():  
    if request.method == 'POST' and request.form['pass'] == 'jtp':  
        return redirect(url_for('success')) 

    return redirect(url_for('login'))  
 
@app.route('/success')  
def success():
    return "Logged in successfully"

if __name__ == "__main__":
    app.run(threaded = True)
