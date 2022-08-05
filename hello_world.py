from flask import Flask, jsonify, request
  
app = Flask(__name__)
  
  
@app.route('/hello_world', methods=['GET'])
def helloworld():
    if(request.method == 'GET'):
        data = {"message": "Hello World"}
        return jsonify(data)
  
  
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")