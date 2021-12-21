from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'Name': u'Mom',
        'Contact': u'Call mama back', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Dad',
        'Contact': u'Call papa back', 
        'done': False
    },
    {
        'id': 3,
        'Name': u'Borther',
        'Contact': u'At School', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

contact = {
    'id':tasks[-1]['id'] +1,
    'Name': request.json['Name'],
    'Contact': request.json['Contact'],
    'done':False
}

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)