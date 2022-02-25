from flask import Flask  
from flask import render_template
from flaskwebgui import FlaskUI
from handlers.file_loader import load_csv

app = Flask(__name__)
ui = FlaskUI(app, width=500, height=500)


@app.route("/")
def hello():  
    return render_template('index.html')

@app.route("/home", methods=['GET'])
def home():
    res = load_csv("test")
    print(res)
    return render_template('some_page.html', test = res)



if __name__ == "__main__":
    ui.run()
   
