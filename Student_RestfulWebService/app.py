import json
from flask import Flask, jsonify, render_template, request, Response


app = Flask(__name__)


with open('Students.JSON') as json_data:
    d = json.load(json_data)
    list_of_students = []
    for data in d['students']:
    	list_of_students.append(data)


@app.route('/', methods =['GET'])
def home():
	return render_template("index.html")

@app.route('/students', methods =['GET'])
def all_students():
	return render_template("index.html",list_data=list_of_students)

@app.route('/students/<string:student_id>', methods =['GET'])
def student_by_id(student_id):
	emp = [students for students in list_of_students if students['studentid'] == student_id]
	return render_template("index.html",list_data=emp)

if __name__ == '__main__':
	 app.run(host='0.0.0.0', port=5000)