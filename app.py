from flask import Flask,render_template,request
from main import firebase
from flask import redirect
app = Flask(__name__)
db=firebase.database()
#Global Varible
global i
i=0
selected_Value=[]

data=db.child('quizz').child('questions').get()
def next_Question():
    global i
    i=i+1
    next_Data=data.val()[i]
    print(next_Data)
    return 'pooda'
@app.route('/')
def hello_world():
    try:
        global i
        print('2 hello',i)
        q=data.val()[i]
        question=q['question']
        option_a=q['answers'][0]
        option_b=q['answers'][1]
        option_c=q['answers'][2]
        option_d=q['answers'][3]
        print(q)
        return render_template('index.html',Question=question,Option_a=option_a,Option_b=option_b,Option_c=option_c,Option_d=option_d)
    except:
        return "thank you"
@app.route('/action-submit')
def submit():
    try:
        global i
        i=i+1
        print(i)
        return hello_world()
    except:
        print('thank you')


@app.route('/<selectedValue>', methods=['POST'])
def click():
    selectedValue = request.form['option']
    return print(selected_Value.append(selectedValue))
if __name__ == '__main__':
    app.run()
