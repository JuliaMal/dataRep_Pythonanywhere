#!flask/bin/python
from flask import Flask, url_for, request, redirect, abort, jsonify
from memberDAO import memberDAO


app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def index():
    return "This is a GYM Database"

#get all
# code passed to cmd:
# curl "http://127.0.0.1:5000/members"
@app.route('/members')
def getAll():
    results = memberDAO.getAll()
    return jsonify(results)

#find by ID
@app.route('/members/<int:id>')
def findById(id):
    foundMember = memberDAO.findByID(id)
    return  jsonify(foundMember)
    

#create
# code passed to cmd:
# curl -X POST -H "content-type:application/json" -d "{\"name\":\"Mary\", \"surname\":\"Block\", \"age\":23}" http://127.0.0.1:5000/members
@app.route('/members', methods=['POST'])
def create():
    if not request.json:
        abort(400)

    member = {
        "name": request.json["name"],
        "surname": request.json["surname"],
        "age": request.json["age"]
    }

    #making a tuple
    values = (member['name'], member['surname'], member['age'])
    newId = memberDAO.create(values)
    member['id'] = newId

    return jsonify(member)

#update
# put to cmd:
# curl -X PUT -d "{\"name\":\"Max\", \"age\":35}" -H "content-type:application/json" http://127.0.0.1:5000/members/1
@app.route('/members/<int:id>', methods=['PUT'])
def update(id):
    foundMember = memberDAO.findByID(id)
    if not foundMember:
        abort(404)

    if not request.json:
        abort(400)
    reqJson = request.json

    #check for the intiger type
    if 'age' in reqJson and type(reqJson['age']) is not int:
        abort(400)

    if 'name' in reqJson:
        foundMember['name'] = reqJson['name']
    
    if 'surname' in reqJson:
        foundMember['surname'] = reqJson['surname']
    
    if 'age' in reqJson:
        foundMember['age'] = reqJson['age']
    
    values = (foundMember['name'], foundMember['surname'], foundMember['age'], foundMember['id'])
    memberDAO.update(values)
    return jsonify(foundMember)

#delete
# put to cmd:
# curl -X DELETE http://127.0.0.1:5000/members/1
@app.route('/members/<int:id>', methods=['DELETE'])
def delete(id):
    memberDAO.delete(id)
    return jsonify({"done":True})


if __name__ == '__main__':
    app.run(debug=True)