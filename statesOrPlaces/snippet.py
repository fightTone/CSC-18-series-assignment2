from flask import Flask, jsonify, request
import json



app =Flask(__name__)

with open('state.json') as f:
	data = json.load(f)
@app.route('/', methods = ['GET'])
def index():
	return jsonify({'message' : 'It Works!, add /results or /places or /places&abv for GET or you can also Try using the snippet_req.py for GET, POST, PUT, and DELETE requests'})


@app.route('/results', methods = ['GET'])
def returndata():
	
	# newd=[]
	# for places in data['states']:
	# 	newd.append({'st_name' : places['name']})
	# return jsonify({'st_name' : newd})
	return jsonify({"results" : data})

@app.route('/places', methods = ['GET'])
def returnstates():
	
	newd=[]
	for places in data['states']:
		newd.append({'name' : places['name']})
	return jsonify({"results" : newd})

@app.route('/places&abv', methods = ['GET'])
def restatesnabv():
	
	for places in data['states']:
		del places['area_codes']
	return jsonify({"results" : data})

@app.route('/places=<string:name>', methods = ['GET'])
def retst(name):
	
	stat = [state for state in data['states'] if state['name']==name]
	
	return jsonify({'state' : stat[0]})

@app.route('/places', methods = ['POST'])
def addstate():
	
	stat = {'name':request.json['name'], 'abbreviation':request.json['abbreviation'], 'area_codes':request.json['area_codes']}
	data['states'].append(stat)
	return jsonify({'results': data['states']})

@app.route('/places=<string:name>', methods = ['PUT'])
def editstate(name):
	stat = [places for places in data['states'] if places['name'] == name]
	stat[0]['name'] = request.json['name']
	stat[0]['abbreviation'] = request.json['abbreviation']
	stat[0]['area_codes'] = request.json['area_codes']
	return jsonify({'Places' : stat[0]})

@app.route('/places=<string:name>', methods = ['DELETE'])
def deletestate(name):
	stat = [places for places in data['states'] if places['name'] == name]
	data['states'].remove(stat[0])
	return jsonify({'results' : data['states']})


if __name__ == '__main__':
	app.run(debug = True, port=8080)