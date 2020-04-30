from flask import Flask, redirect, url_for, render_template, request, send_from_directory
import json

app = Flask(__name__, template_folder='templates')

def superhero(answers):
    # TODO : return correct superhero based on answers
    return "superman"

@app.route('/')
def main():
   # return render_template('main.html')
   return render_template('firstQuestion.html')

@app.route('/data')
def data():
    with open('questions.json') as json_file:
        data = json.load(json_file)
        return data 

@app.route('/getSuperhero', methods=['POST'])
def getSuperhero():
    # ImmutableMultiDict([('{"answers":["D","D","F","C","D","D","C","C","D","D"]}', '')])
    # {'{"answers":["G","D"]}': ''}
    # {'answers': ['G', 'D']}
    data = list(request.form.to_dict().keys())[0]
    data = json.loads(data)
    answers = data['answers']
    print(answers)



    hero = superhero(answers)
    return {"hero" : hero}

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0',port=3000)


