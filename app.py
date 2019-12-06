from flask import Flask
from flask import render_template
# from flask_login import login_required, current_user


app = Flask(__name__, template_folder='templates')
app.config.from_object('config')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/what')
def what():
    return render_template("what.html")

@app.route('/how')
def how():
    return render_template("how.html")

@app.route('/findings')
def findings():
    return render_template("findings.html")

@app.route('/papers')
def conclusion():
    return render_template("papers.html")

if __name__ == '__main__':
    app.run()