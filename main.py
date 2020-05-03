from flask import Flask, redirect, url_for, render_template, request, send_from_directory
import json

app = Flask(__name__, template_folder='templates')

def superhero(answers):
    # TODO : return correct superhero based on answers
    counter = {
    'Wonderwoman' : 0,
    'Batman' : 0,
    'Aquaman' : 0,
    'Spiderman' : 0,
    'Ironman' : 0,
    'Hulk' : 0,
    'Wolverine' : 0
    }

    q1 = answers[0]
    if q1 == 'A':
        counter['Wonderwoman'] += 1
    elif q1 == 'B':
        counter['Batman'] += 1
    elif q1 == 'C':
        counter['Aquaman'] += 1
    elif q1 == 'D':
        counter['Spiderman'] += 1
    elif q1 == 'E':
        counter['Ironman'] += 1
    elif q1 == 'F':
        counter['Hulk'] += 1
    elif q1 == 'G':
        counter['Wolverine'] += 1  

    q2 = answers[1]
    if q2 == 'A':
        counter['Wonderwoman'] += 1
        counter['Spiderman'] += 1
        counter['Aquaman'] += 1
    elif q2 == 'B':
        counter['Batman'] += 1
        counter['Hulk'] += 1
    elif q2 == 'C':
        counter['Ironman'] += 1
    elif q2 == 'D':
        counter['Wolverine'] += 1

    q3 = answers[2]
    if q3 == 'A':
        counter['Wonderwoman'] += 1
    elif q3 == 'B':
        counter['Batman'] += 1
    elif q3 == 'C':
        counter['Aquaman'] += 1
    elif q3 == 'D':
        counter['Spiderman'] += 1
    elif q3 == 'E':
        counter['Ironman'] += 1
    elif q3 == 'F':
        counter['Hulk'] += 1
    elif q3 == 'G':
        counter['Wolverine'] += 1 

    q4 = answers[3]
    if q4 == 'A':
        counter['Wonderwoman'] += 1
        counter['Hulk'] += 1
        counter['Batman'] += 1
        counter['Aquaman'] += 1
        Wolverin += 1
    elif q4 == 'B':
        counter['Spiderman'] += 1
    elif q4 == 'C':
        counter['Ironman'] += 1

    q5 = answers[4]
    if q5 == 'A':
        counter['Wonderwoman'] += 1
        counter['Hulk'] += 1
        counter['Spiderman'] += 1
    elif q5 == 'B':
        counter['Aquaman'] += 1
    elif q5 == 'C':
        counter['Wolverine'] += 1
    elif q5 == 'D':
        counter['Ironman'] += 1
        counter['Batman'] += 1

    q6 = answers[5]
    if q6 == 'A':
        counter['Hulk'] += 1
    elif q6 == 'B':
        counter['Ironman'] += 1
        counter['Batman'] += 1
    elif q6 == 'C':
        counter['Spiderman'] += 1
        counter['Aquaman'] += 1
    elif q6 == 'D':
        counter['Wolverine'] += 1
        counter['Wonderwoman'] += 1

    q7 = answers[6]
    if q7 == 'A':
        counter['Ironman'] += 1
        counter['Hulk'] += 1
        counter['Wolverine'] += 1
        counter['Aquaman'] += 1
        counter['Spiderman'] += 1
    elif q7 == 'B':
        counter['Batman'] += 1
    elif q7 == 'C':
        counter['Wonderwoman'] += 1

    q8 = answers[7]
    if q8 == 'A':
        counter['Hulk']+= 1
        counter['Ironman'] += 1
    elif q8 == 'B':
        counter['Aquaman'] += 1
        counter['Spiderman'] += 1
    elif q8 == 'C':
        counter['Wonderwoman'] += 1
        counter['Batman'] += 1
        counter['Wolverine'] += 1

    q9 = answers[8]
    if q9 == 'A':
        counter['Hulk'] += 1
        counter['Wonderwoman'] += 1
    elif q9 == 'B':
        counter['Wolverine'] += 1
        counter['Spiderman'] += 1
    elif q9 == 'C':
        counter['Ironman'] += 1
        counter['Batman'] += 1
    elif q9 == 'D':
        counter['Aquaman'] += 1

    q10 = answers[9]
    if q10 == 'A':
        counter['Wonderwoman'] += 1
        counter['Hulk'] += 1
        counter['Wolverine'] += 1
    elif q10 == 'B':
        counter['Batman'] += 1
    elif q10 == 'C':
        counter['Spiderman'] += 1
        counter['Aquaman'] += 1
    elif q10 == 'D':
        counter['Wolverine'] += 1

    return max(counter, key=counter.get) # calculates which superhero user got given a list of the answers from the quiz
 
@app.route('/')
def main(): 
   # return render_template('main.html')
   return render_template('firstQuestion.html')

@app.route('/data')
def data():
    # retrieves questions and possible answers from json file
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
    answers = data['answers'] #retrieves answer input in list format

    hero = superhero(answers)
    return {"hero" : hero} #returns key pair with which superhero the user got

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0',port=3000)

