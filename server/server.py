from flask import Flask
from flask import request
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
frames = []
targets = []
forest = RandomForestClassifier(criterion='entropy',
                            n_estimators=1, 
                            n_jobs=2)
def add(datapoint, classifier):
    return 0

def getphase(tri):
    return 0

def predict(rep):
    return 0

def train(reps, classification):
    
    for i in range(len(reps)):
        phases = []
        for rep in reps[i]:
            phase = getphase(rep)
            phases.append(phase)

    forest.fit(phases, classification)
    return 0

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/good", methods=('POST',))
def hello21():
    print("request.get_json() ", request.get_json())
    print("reqest.data()", request.data)
    json = (request.data['data']) 
    classification = (request.data['classification']) 
    frames.append(json)
    target.append(classification)
    return json

@app.route("/check", methods=('POST',))
def hello1():
    json = str(request.data['data']) 
    result = predict(json)
    return result




