from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('sample.html')
    
if __name__ == "__main__":
    app.run('0.0.0.0',port=3000)
