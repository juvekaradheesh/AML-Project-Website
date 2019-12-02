from flask import Flask
from flask import render_template
# from flask_login import login_required, current_user


app = Flask(__name__, template_folder='templates')
app.config.from_object('config')


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()