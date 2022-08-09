from flask import Flask, jsonify, request, redirect, url_for
import argparse

parser = argparse.ArgumentParser(description='Run simple hello world using Flask')
parser.add_argument('--host', help='Hostname', required = False, default='0.0.0.0')
parser.add_argument('--port', help='Port', required = False, default='5000')
args = parser.parse_args()

  
app = Flask(__name__)
  
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def redirect_all(path):
    return redirect(url_for('hello_world'))
  
@app.route('/helloworld', methods=['GET'])
def hello_world():
    if(request.method == 'GET'):
        data = {"message": "Hello World"}
        return jsonify(data)
  
print(args.host)
print(args.port)
  
if __name__ == '__main__':
    app.run(debug=True, host=args.host, port=int(args.port))