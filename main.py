from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/first')
def firstQuestion():
	return render_template('firstQustion.html')

if __name__ == "__main__":
    app.run('0.0.0.0',port=3000)


