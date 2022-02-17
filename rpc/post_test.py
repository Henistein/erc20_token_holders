from flask import Flask, request, jsonify

app = Flask(__name__)

from flask import Flask, request, jsonify

@app.route('/post', methods=['POST'])
def post():
	name = request.args.get('name')
	message = request.args.get('message')
	return f"{name}:{message}"

if __name__ == '__main__':
	app.run()
