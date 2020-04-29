from flask import Flask, redirect, url_for, render_template, request, send_from_directory
import json

app = Flask(__name__, template_folder='templates')



@app.route('/')
def main():
   # return render_template('main.html')
   return render_template('firstQuestion.html')

@app.route('/data')
def data():
    with open('questions.json') as json_file:
        data = json.load(json_file)
        return data 

@app.route('/first',methods=['GET','POST'])
def firstQuestion():
    if request.method == "POST":
        answer = request.form["q1"]

    else:
        return render_template('testQ.html')

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0',port=3000)


